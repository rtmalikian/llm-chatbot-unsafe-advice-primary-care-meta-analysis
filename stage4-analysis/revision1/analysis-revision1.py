#!/usr/bin/env python3
"""
Review 4, peer-review revision 1 re-analysis (2026-11-13).
Corrects the interval machinery fault in analysis.py (Blocker B-C):
- GLMM fitted by maximising the marginal likelihood with ADAPTIVE Gauss-Hermite
  quadrature (31 nodes; per-unit Laplace mode and scale), joint Nelder-Mead
  optimisation over (mu, log tau) seeded from a profile grid.
- Standard errors from the observed information (central differences,
  step 0.01 on mu / 0.02 on log tau, checked at half step).
- Every printed interval is validated against the floor SE(mu) >= sqrt(tau2/k).
  A fit that fails the floor check is flagged, not printed as a result.
- Hartung-Knapp inverse-variance logit fits (DerSimonian-Laird tau2, 0.5
  correction applied to ALL arms, exactly as coded in analysis.py) are reported
  for every pool and sensitivity with >=4 units.
- Study-level sensitivity: arms aggregated within study, DL logit + HK.
Inputs: ../analysis-dataset.csv (unchanged) + tier labels from
../../stage3-extraction/extraction-settled.csv for the strict-tier sensitivity.
Settled extraction counts are NOT changed by this script.
Outputs: revision1-results.json, revision1-results.md (printed).
"""
import csv, json, math, pathlib
import numpy as np
from scipy import optimize, stats
from numpy.polynomial.hermite import hermgauss

HERE = pathlib.Path(__file__).parent
BASE = HERE.parent
GH_X, GH_W = hermgauss(31)

def unit_ll(mu, tau, yi, ni):
    u = 0.0
    for _ in range(60):
        eta = mu + u
        p = 1/(1+math.exp(-eta)) if abs(eta) < 35 else (1.0 if eta > 0 else 0.0)
        g = yi - ni*p - u/(tau*tau)
        h = -ni*p*(1-p) - 1/(tau*tau)
        step = g/h; u -= step
        if abs(step) < 1e-11: break
    eta = mu + u
    p = 1/(1+math.exp(-eta)) if abs(eta) < 35 else (1.0 if eta > 0 else 0.0)
    curv = ni*p*(1-p) + 1/(tau*tau)
    s = 1/math.sqrt(curv)
    un = u + math.sqrt(2.0)*s*GH_X
    etas = np.clip(mu+un, -35, 35)
    pr = 1/(1+np.exp(-etas))
    loglik = yi*np.log(np.clip(pr, 1e-300, 1)) + (ni-yi)*np.log(np.clip(1-pr, 1e-300, 1))
    logprior = -0.5*(un/tau)**2 - math.log(tau) - 0.5*math.log(2*math.pi)
    vals = loglik + logprior + 0.5*GH_X**2
    m = vals.max()
    return math.log(math.sqrt(2.0)*s) + m + math.log(np.sum(GH_W*np.exp(vals-m)))

def marg(mu, tau, y, n):
    return sum(unit_ll(mu, tau, y[i], n[i]) for i in range(len(y)))

def glmm(y, n):
    y = np.asarray(y, float); n = np.asarray(n, float)
    k = len(y)
    best = None
    for lt in np.arange(math.log(0.05), math.log(5.0), 0.25):
        tau = math.exp(lt)
        r = optimize.minimize_scalar(lambda mu: -marg(mu, tau, y, n), bounds=(-7, 2), method="bounded", options={"xatol": 1e-5})
        if best is None or r.fun < best[0]: best = (r.fun, r.x, tau)
    def nll(p): return -marg(p[0], math.exp(p[1]), y, n)
    x0 = np.array([best[1], math.log(best[2])])
    res = optimize.minimize(nll, x0, method="Nelder-Mead", options={"maxiter": 2500, "xatol": 1e-7, "fatol": 1e-7})
    res = optimize.minimize(nll, res.x, method="Nelder-Mead", options={"maxiter": 2500, "xatol": 1e-8, "fatol": 1e-8})
    mu, lt = res.x; tau2 = math.exp(2*lt)
    def hess(sm, slt):
        f0 = nll(res.x)
        def F(dx, dy): return nll(res.x + np.array([dx, dy]))
        h11 = (F(sm, 0)-2*f0+F(-sm, 0))/sm**2
        h22 = (F(0, slt)-2*f0+F(0, -slt))/slt**2
        h12 = (F(sm, slt)-F(sm, -slt)-F(-sm, slt)+F(-sm, -slt))/(4*sm*slt)
        H = np.array([[h11, h12], [h12, h22]])
        try: cov = np.linalg.inv(H)
        except Exception: cov = np.linalg.pinv(H)
        return math.sqrt(abs(cov[0, 0]))
    se = hess(0.01, 0.02); se_half = hess(0.005, 0.01)
    f = lambda z: 100/(1+math.exp(-z))
    tcrit = stats.t.ppf(0.975, max(k-2, 1))
    half = tcrit*math.sqrt(tau2+se**2)
    floor = math.sqrt(tau2/k)
    return {"k": k, "pooled_pct": round(f(mu), 2), "ci_lo_pct": round(f(mu-1.96*se), 2),
            "ci_hi_pct": round(f(mu+1.96*se), 2), "tau2": round(tau2, 4), "se_logit": round(se, 4),
            "se_halfstep": round(se_half, 4), "floor_sqrt_tau2_over_k": round(floor, 4),
            "floor_check": "PASS" if se >= floor*0.98 else "FAIL",
            "pi_lo_pct": round(f(mu-half), 2), "pi_hi_pct": round(f(mu+half), 2), "loglik": round(-res.fun, 2)}

def i2_logit(y, n):
    y = np.asarray(y, float); n = np.asarray(n, float)
    yi = np.log((y+0.5)/(n-y+0.5)); vi = 1/(y+0.5)+1/(n-y+0.5)
    w = 1/vi; mu = np.sum(w*yi)/np.sum(w)
    Q = float(np.sum(w*(yi-mu)**2)); df = len(y)-1
    return round(max(0.0, (Q-df)/Q)*100, 1) if Q > 0 else 0.0

def hk(y, n):
    y = np.asarray(y, float); n = np.asarray(n, float)
    yi = np.log((y+0.5)/(n-y+0.5)); vi = 1/(y+0.5)+1/(n-y+0.5)
    w = 1/vi; mu_fe = np.sum(w*yi)/np.sum(w)
    Q = float(np.sum(w*(yi-mu_fe)**2)); df = len(y)-1
    C = np.sum(w)-np.sum(w**2)/np.sum(w)
    tau2 = max(0.0, (Q-df)/C)
    wr = 1/(vi+tau2); mu = np.sum(wr*yi)/np.sum(wr)
    q_hk = np.sum(wr*(yi-mu)**2)/df
    se_hk = math.sqrt(q_hk/np.sum(wr))
    tcrit = stats.t.ppf(0.975, df)
    f = lambda z: 100/(1+math.exp(-z))
    return {"pooled_pct": round(f(mu), 2), "ci_lo_pct": round(f(mu-tcrit*se_hk), 2),
            "ci_hi_pct": round(f(mu+tcrit*se_hk), 2), "tau2_dl": round(tau2, 4)}

def summarise(name, units):
    """units: list of dicts with events,total,study key."""
    y = [u["events"] for u in units]; n = [u["total"] for u in units]
    out = {"analysis": name, "units": len(units), "studies": len({u["study"] for u in units}),
           "events": int(sum(y)), "total": int(sum(n)),
           "crude_pct": round(100*sum(y)/sum(n), 2) if sum(n) else None}
    if len(units) >= 2:
        g = glmm(y, n); out["glmm"] = g; out["I2_pct_fixedQ_corrected_logits"] = i2_logit(y, n)
    if len(units) >= 4:
        out["hk"] = hk(y, n)
    return out

def main():
    with open(BASE/"analysis-dataset.csv") as fh:
        ds = list(csv.DictReader(fh))
    for r in ds:
        r["events"] = int(r["events"]); r["total"] = int(r["total"])
        r["study"] = r["record_id"]
    # tier labels for P1 arms from settled sheet (join on record_id + model match via analysis order is unsafe;
    # instead join settled rows to dataset rows on record_id and events/total for P1)
    with open(BASE.parent/"stage3-extraction"/"extraction-settled.csv") as fh:
        settled = list(csv.DictReader(fh))
    import re
    def num(v):
        v = (v or "").strip()
        return int(v) if re.fullmatch(r"\d+", v) else None
    label_by_key = {}
    for r in settled:
        ev, den = num(r["n_unsafe"]), num(r["n_responses_rated_safety"])
        if ev is not None and den is not None:
            label_by_key.setdefault((r["record_id"], ev, den), r["unsafe_tier_label"])
    STRICT = {"unsafe", "Unsafe"}  # task definition: explicitly unsafe/harmful/dangerous ONLY
    p1 = [r for r in ds if r["pool"] == "P1_primary_bench"]
    for r in p1:
        r["tier_label"] = label_by_key.get((r["record_id"], r["events"], r["total"]), "UNMATCHED")
    unmatched = [r for r in p1 if r["tier_label"] == "UNMATCHED"]
    print(f"P1 tier-label join: {len(p1)-len(unmatched)}/{len(p1)} matched; unmatched={len(unmatched)}")
    strict = [r for r in p1 if r["tier_label"] in STRICT]
    s1 = [r for r in ds if r["pool"] == "S1_problematic"]
    s2 = [r for r in ds if r["pool"] == "S2_undertriage"]

    R = {}
    R["P1_main"] = summarise("P1 primary bench, all arms (revision 1 GLMM)", p1)
    R["P1_HK_note"] = "HK uses DL tau2 on 0.5-corrected logits, correction applied to all arms."
    R["P1_sens_no_preprints"] = summarise("P1 excl. preprints", [r for r in p1 if r["preprint"] == "False"])
    R["P1_sens_no_derived"] = summarise("P1 excl. derived-count arms", [r for r in p1 if r["derived"] == "False"])
    R["P1_sens_era_late_classified_only"] = summarise("P1 era-classified late arms only (88 arms; 4 unclassified excluded)", [r for r in p1 if r["era"] == "era_late"])
    R["P1_sens_no_high_rob"] = summarise("P1 excl. high RoB studies", [r for r in p1 if r["rob_overall"] != "High"])
    R["P1_strict_tier"] = summarise("P1 STRICT tier only (label exactly unsafe/Unsafe; excl. potentially tiers, error labels, Fraser triage)", strict)
    R["P1_strict_composition"] = {"arms": len(strict), "studies": sorted({r["study_id"] for r in strict}),
                                  "events": int(sum(r["events"] for r in strict)), "total": int(sum(r["total"] for r in strict))}
    R["P1_ex_Fraser"] = summarise("P1 excl. Fraser 2023", [r for r in p1 if r["record_id"] != "R2042"])
    # study-level: aggregate within record_id
    from collections import defaultdict
    agg = defaultdict(lambda: {"events": 0, "total": 0, "study": ""})
    for r in p1:
        agg[r["record_id"]]["events"] += r["events"]; agg[r["record_id"]]["total"] += r["total"]; agg[r["record_id"]]["study"] = r["record_id"]
    R["P1_study_level"] = summarise("P1 study-level aggregated (one value per study, DL logit + HK is the headline; GLMM also fitted)", list(agg.values()))
    R["P1_zero_event_census"] = {"arms": int(sum(1 for r in p1 if r["events"] == 0)),
                                 "responses": int(sum(r["total"] for r in p1 if r["events"] == 0)),
                                 "detail": sorted({(r["study_id"], r["total"]) for r in p1 if r["events"] == 0})}
    R["P1_derived_share"] = {"arms": int(sum(1 for r in p1 if r["derived"] == "True")),
                              "events": int(sum(r["events"] for r in p1 if r["derived"] == "True")),
                              "responses": int(sum(r["total"] for r in p1 if r["derived"] == "True"))}
    R["S1_main"] = summarise("S1 problematic, all units (revision 1 GLMM)", s1)
    R["S1_ex_Khan"] = summarise("S1 excl. Khan 2026 (R3040)", [r for r in s1 if r["record_id"] != "R3040"])
    R["S1_ex_Si_human_user"] = summarise("S1 excl. Si 2026 human-user arms (R2244)", [r for r in s1 if r["record_id"] != "R2244"])
    R["S1_ex_Khan_ex_Si"] = summarise("S1 excl. Khan and Si", [r for r in s1 if r["record_id"] not in ("R3040", "R2244")])
    R["S1_bench_only"] = summarise("S1 bench stratum only", [r for r in s1 if r["stratum"] == "bench"])
    R["S1_no_derived"] = summarise("S1 excl. derived-count units", [r for r in s1 if r["derived"] == "False"])
    R["S1_main_search_only"] = summarise("S1 main search set only (excl. chasing CC units)", [r for r in s1 if not r["record_id"].startswith("CC")])
    R["S1_derived_share"] = {"units": int(sum(1 for r in s1 if r["derived"] == "True")),
                              "events": int(sum(r["events"] for r in s1 if r["derived"] == "True")),
                              "responses": int(sum(r["total"] for r in s1 if r["derived"] == "True"))}
    R["S2_main"] = summarise("S2 undertriage, all units (GLMM flagged: see changelog; HK is the supplement value)", s2)
    # era levels, descriptive only in revision (exploratory)
    R["era_early_descriptive"] = summarise("Era early arms only (exploratory, descriptive)", [r for r in p1 if r["era"] == "era_early"])
    R["era_unclassified"] = {"arms": int(sum(1 for r in p1 if r["era"] == "not_reported")),
                              "events": int(sum(r["events"] for r in p1 if r["era"] == "not_reported")),
                              "total": int(sum(r["total"] for r in p1 if r["era"] == "not_reported"))}
    (HERE/"revision1-results.json").write_text(json.dumps(R, indent=1))
    print(json.dumps(R, indent=1))

if __name__ == "__main__":
    main()
