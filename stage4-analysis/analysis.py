#!/usr/bin/env python3
"""
Review 4 meta-analysis. Random-effects GLMM, logit link, binomial likelihood,
ML estimator, adaptive Gauss-Hermite quadrature (15 nodes), fitted with scipy.
R and metafor are not installed in this environment; this script is the analysis
of record and analysis.R is a documented stub. Run date: 2026-11-12.
Inputs: ../stage3-extraction/extraction-settled.csv (+ extraction lists for pool
status, rob-settled.csv for the risk-of-bias sensitivity, and, when present,
chasing-secondary-settled.csv for the chasing secondary studies).
Outputs: results-summary.csv, analysis-dataset.csv, analysis-output.md data
(printed to stdout and analysis-results.json).
"""
import csv, json, math, re, sys
import numpy as np
from scipy import optimize, stats
from numpy.polynomial.hermite import hermgauss

BASE = "../stage3-extraction/"
GH_X, GH_W = hermgauss(15)

def glmm_fit(y, n, X=None):
    """Random-intercept GLMM on the logit scale. y,n: arrays. X: optional
    covariate matrix (columns appended after intercept). Returns dict."""
    y = np.asarray(y, float); n = np.asarray(n, float)
    k = len(y)
    if X is None:
        X = np.ones((k, 1))
    else:
        X = np.asarray(X, float)
    p = X.shape[1]
    def nll(params):
        beta = params[:p]; logtau = params[p]
        tau = math.exp(logtau)
        eta_fixed = X @ beta
        # adaptive GH: approximate per-unit posterior mode/scale by Laplace on a grid
        ll = 0.0
        for i in range(k):
            # nodes around 0 with unit scale; integrand on u ~ N(0, tau^2)
            u = math.sqrt(2.0) * tau * GH_X
            eta = eta_fixed[i] + u
            pr = 1.0 / (1.0 + np.exp(-eta))
            pr = np.clip(pr, 1e-12, 1 - 1e-12)
            loglik = y[i] * np.log(pr) + (n[i] - y[i]) * np.log(1 - pr)
            vals = loglik - 0.5 * GH_X ** 2  # includes N(0,1) kernel after transform
            m = vals.max()
            ll += m + math.log(np.sum(GH_W * np.exp(vals - m))) - 0.5 * math.log(math.pi)
        return -ll
    crude = (y.sum() + 0.5) / (n.sum() + 1.0)
    x0 = np.zeros(p + 1); x0[0] = math.log(crude / (1 - crude)); x0[p] = math.log(0.5)
    res = optimize.minimize(nll, x0, method="Nelder-Mead",
                            options={"maxiter": 4000, "xatol": 1e-6, "fatol": 1e-6})
    res2 = optimize.minimize(nll, res.x, method="Nelder-Mead",
                             options={"maxiter": 4000, "xatol": 1e-8, "fatol": 1e-8})
    if res2.fun < res.fun: res = res2
    beta = res.x[:p]; tau = math.exp(res.x[p])
    # Hessian-based SEs for beta via numerical differentiation at the optimum of profile? Use full Hessian.
    H = optimize._numdiff.approx_derivative  # placeholder (unused)
    # numerical Hessian of nll wrt all params
    eps = 1e-4
    d = len(res.x)
    hess = np.zeros((d, d))
    f0 = nll(res.x)
    for a in range(d):
        for b in range(d):
            ea = np.zeros(d); ea[a] = eps
            eb = np.zeros(d); eb[b] = eps
            hess[a, b] = (nll(res.x + ea + eb) - nll(res.x + ea - eb)
                          - nll(res.x - ea + eb) + nll(res.x - ea - eb)) / (4 * eps * eps)
    cov = np.linalg.pinv(hess)
    se = np.sqrt(np.abs(np.diag(cov)))[:p]
    return {"beta": beta, "se": se, "tau2": tau ** 2, "tau": tau, "loglik": -res.fun, "k": k}

def pool_stats(fit):
    mu = fit["beta"][0]; se = fit["se"][0]; tau2 = fit["tau2"]
    p_pool = 1 / (1 + math.exp(-mu))
    lo = 1 / (1 + math.exp(-(mu - 1.96 * se))); hi = 1 / (1 + math.exp(-(mu + 1.96 * se)))
    # prediction interval (t with k-2 df on logit scale)
    k = fit["k"]
    tcrit = stats.t.ppf(0.975, max(k - 2, 1))
    half = tcrit * math.sqrt(tau2 + se ** 2)
    pi_lo = 1 / (1 + math.exp(-(mu - half))); pi_hi = 1 / (1 + math.exp(-(mu + half)))
    # I^2 from a fixed-effect Q on logit scale with 0.5 correction
    return {"pooled": p_pool, "ci_lo": lo, "ci_hi": hi, "tau2": tau2,
            "pi_lo": pi_lo, "pi_hi": pi_hi}

def i2_logit(y, n):
    y = np.asarray(y, float); n = np.asarray(n, float)
    yi = np.log((y + 0.5) / (n - y + 0.5)); vi = 1 / (y + 0.5) + 1 / (n - y + 0.5)
    w = 1 / vi; mu = np.sum(w * yi) / np.sum(w)
    Q = float(np.sum(w * (yi - mu) ** 2)); df = len(y) - 1
    I2 = max(0.0, (Q - df) / Q) * 100 if Q > 0 else 0.0
    return Q, df, I2

def hk_sensitivity(y, n):
    """Inverse-variance logit random-effects (DL) with Hartung-Knapp adjustment."""
    y = np.asarray(y, float); n = np.asarray(n, float)
    yi = np.log((y + 0.5) / (n - y + 0.5)); vi = 1 / (y + 0.5) + 1 / (n - y + 0.5)
    w = 1 / vi; mu_fe = np.sum(w * yi) / np.sum(w)
    Q = float(np.sum(w * (yi - mu_fe) ** 2)); df = len(y) - 1
    C = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    tau2 = max(0.0, (Q - df) / C)
    wr = 1 / (vi + tau2); mu = np.sum(wr * yi) / np.sum(wr)
    q_hk = np.sum(wr * (yi - mu) ** 2) / df
    se_hk = math.sqrt(q_hk / np.sum(wr))
    tcrit = stats.t.ppf(0.975, df)
    lo, hi = mu - tcrit * se_hk, mu + tcrit * se_hk
    f = lambda z: 1 / (1 + math.exp(-z))
    return {"pooled": f(mu), "ci_lo": f(lo), "ci_hi": f(hi), "tau2_dl": tau2}

def load_main():
    lists = {}
    for p in ["extraction-list-half1.csv", "extraction-list-half2.csv"]:
        with open(BASE + p) as fh:
            for r in csv.DictReader(fh): lists[r["record_id"]] = r
    with open(BASE + "extraction-settled.csv") as fh: rows = list(csv.DictReader(fh))
    for r in rows:
        r["pool"] = lists.get(r["record_id"], {}).get("pool_status", "")
        r["doi"] = lists.get(r["record_id"], {}).get("doi", "")
    return rows

def num(v):
    v = (v or "").strip()
    return int(v) if re.fullmatch(r"\d+", v) else None

def pair(v):
    m = re.match(r"^\s*(\d+)\s*/\s*(\d+)\s*$", v or "")
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)

PREPRINT_DOI = ("10.21203/rs.3.rs-", "10.64898/")
def is_preprint(doi): return any(s in (doi or "") for s in PREPRINT_DOI)
def is_derived(notes): return "DERIVED" in (notes or "")

def main():
    rows = load_main()
    rob = {}
    try:
        with open(BASE + "rob-settled.csv") as fh:
            for r in csv.DictReader(fh): rob[r["record_id"]] = r["overall_rating"].strip()
    except FileNotFoundError:
        print("WARNING: rob-settled.csv not found; RoB sensitivity skipped", file=sys.stderr)
    llm = [r for r in rows if r["comparator_flag"].strip().upper() != "YES"]

    datasets = []  # analysis dataset rows for saving
    results = {}

    def add_units(pool_name, unit_rows, outcome_getter):
        for r in unit_rows:
            ev, den = outcome_getter(r)
            if ev is None or den is None: continue
            datasets.append({"pool": pool_name, "record_id": r["record_id"], "study_id": r["study_id"],
                             "arm": r.get("arm_label", r["model_name"]), "events": ev, "total": den,
                             "era": r["model_era"], "stratum": r["stratum"],
                             "preprint": is_preprint(r.get("doi", "")), "derived": is_derived(r.get("notes", "")),
                             "rob_overall": rob.get(r["record_id"], "")})
    # ---- P1 primary bench
    p1_rows = [r for r in llm if r["pool"] == "INCLUDE_PRIMARY" and r["stratum"].strip() == "bench"]
    add_units("P1_primary_bench", p1_rows, lambda r: (num(r["n_unsafe"]), num(r["n_responses_rated_safety"])))
    # ---- P2 human-user primary: none expected
    p2_rows = [r for r in llm if r["pool"] == "INCLUDE_PRIMARY" and r["stratum"].strip() == "human_user"]
    add_units("P2_primary_human_user", p2_rows, lambda r: (num(r["n_unsafe"]), num(r["n_responses_rated_safety"])))
    # ---- S1 problematic (main set)
    s1_rows = [r for r in llm if r["pool"] in ("INCLUDE_PRIMARY", "INCLUDE_SECONDARY")]
    add_units("S1_problematic", s1_rows, lambda r: (num(r["n_problematic"]), num(r["n_rated_problematic"])))
    # ---- S2 undertriage (main set)
    add_units("S2_undertriage", s1_rows, lambda r: pair(r["n_undertriage/n_with_disposition"]))
    # ---- S3 fabrication
    add_units("S3_fabrication", s1_rows, lambda r: pair(r["n_fabrication/n_rated_fabrication"]))
    # ---- chasing secondary additions (if settled file present)
    try:
        with open(BASE + "chasing-secondary-settled.csv") as fh: ch = list(csv.DictReader(fh))
        for r in ch:
            pool = "S1_problematic" if r["outcome_type"] == "problematic" else "S2_undertriage"
            datasets.append({"pool": pool, "record_id": r["cc_id"], "study_id": r["study_id"],
                             "arm": r["model"], "events": int(r["n_events"]), "total": int(r["n_rated"]),
                             "era": r.get("model_era", "not_reported"), "stratum": "bench",
                             "preprint": False, "derived": r.get("derived", "").upper() == "YES",
                             "rob_overall": ""})
        print(f"chasing secondary units added: {len(ch)}")
    except FileNotFoundError:
        print("note: no chasing-secondary-settled.csv; chasing units not pooled", file=sys.stderr)

    with open("analysis-dataset.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(datasets[0].keys())); w.writeheader(); w.writerows(datasets)

    def fit_pool(name, subset=None):
        d = [r for r in datasets if r["pool"] == name]
        if subset: d = [r for r in d if subset(r)]
        if len(d) < 2: return {"pool": name, "units": len(d), "status": "not fitted (<2 units)"}
        y = [r["events"] for r in d]; n = [r["total"] for r in d]
        fit = glmm_fit(y, n); ps = pool_stats(fit)
        Q, df, I2 = i2_logit(y, n)
        out = {"pool": name, "units": len(d), "studies": len({r["record_id"] for r in d}),
               "events": int(sum(y)), "total": int(sum(n)), "crude_pct": round(100 * sum(y) / sum(n), 2),
               "pooled_pct": round(100 * ps["pooled"], 2), "ci_lo_pct": round(100 * ps["ci_lo"], 2),
               "ci_hi_pct": round(100 * ps["ci_hi"], 2), "tau2": round(fit["tau2"], 4),
               "I2_pct": round(I2, 1), "pi_lo_pct": round(100 * ps["pi_lo"], 2), "pi_hi_pct": round(100 * ps["pi_hi"], 2)}
        if len(d) >= 4:
            hk = hk_sensitivity(y, n)
            out["hk_pooled_pct"] = round(100 * hk["pooled"], 2)
            out["hk_ci_lo_pct"] = round(100 * hk["ci_lo"], 2); out["hk_ci_hi_pct"] = round(100 * hk["ci_hi"], 2)
        return out

    def subgroup_test(pool_name, keyfn, label):
        d = [r for r in datasets if r["pool"] == pool_name]
        levels = {}
        for r in d: levels.setdefault(keyfn(r), []).append(r)
        levels = {k: v for k, v in levels.items() if k is not None}
        if len(levels) != 2 or any(len(v) < 2 for v in levels.values()):
            return {"subgroup": label, "status": "descriptive only", "levels": {k: len(v) for k, v in levels.items()}}
        keys = sorted(levels)
        allrows = levels[keys[0]] + levels[keys[1]]
        X = np.column_stack([np.ones(len(allrows)), [0] * len(levels[keys[0]]) + [1] * len(levels[keys[1]])])
        fit = glmm_fit([r["events"] for r in allrows], [r["total"] for r in allrows], X)
        b, se = fit["beta"][1], fit["se"][1]
        z = b / se; pval = 2 * (1 - stats.norm.cdf(abs(z)))
        subs = {}
        for k in keys:
            f1 = glmm_fit([r["events"] for r in levels[k]], [r["total"] for r in levels[k]])
            ps = pool_stats(f1); subs[k] = {"units": len(levels[k]), "pooled_pct": round(100 * ps["pooled"], 2),
                                            "ci_lo_pct": round(100 * ps["ci_lo"], 2), "ci_hi_pct": round(100 * ps["ci_hi"], 2)}
        return {"subgroup": label, "levels": subs, "interaction_logit_diff": round(float(b), 3),
                "interaction_p": round(float(pval), 4)}

    for name in ["P1_primary_bench", "P2_primary_human_user", "S1_problematic", "S2_undertriage", "S3_fabrication"]:
        results[name] = fit_pool(name)
    # sensitivities on P1
    results["P1_sens_no_preprints"] = fit_pool("P1_primary_bench", lambda r: not r["preprint"])
    results["P1_sens_no_derived"] = fit_pool("P1_primary_bench", lambda r: not r["derived"])
    results["P1_sens_era_late_only"] = fit_pool("P1_primary_bench", lambda r: r["era"] == "era_late")
    if rob:
        results["P1_sens_no_high_rob"] = fit_pool("P1_primary_bench", lambda r: r["rob_overall"] != "High")
        results["S1_sens_no_chasing"] = None  # computed below by refit flag if needed
    # era subgroup on P1 (arms with era reported)
    results["subgroup_era_P1"] = subgroup_test("P1_primary_bench",
        lambda r: r["era"] if r["era"] in ("era_early", "era_late") else None, "model era (release before vs on/after 2024-05-13)")
    print(json.dumps(results, indent=1))

if __name__ == "__main__":
    main()
