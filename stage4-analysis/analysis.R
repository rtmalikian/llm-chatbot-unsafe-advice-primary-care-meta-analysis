# analysis.R - documented stub (2026-11-12)
# R and the metafor package are not installed in the build environment for this review.
# The analysis of record is analysis.py (Python, scipy): random-effects GLMM, logit link,
# binomial likelihood, ML estimator, adaptive Gauss-Hermite quadrature (15 nodes).
# This stub records the equivalent R call for reproduction on a machine with R:
#
#   library(metafor)
#   dat <- read.csv("analysis-dataset.csv")
#   p1  <- subset(dat, pool == "P1_primary_bench")
#   res <- rma.glmm(measure = "PLO", xi = events, ni = total, data = p1)
#   summary(res); predict(res, transf = transf.ilogit)
#
# The Hartung-Knapp sensitivity in analysis.py is an inverse-variance logit fit with a
# DerSimonian-Laird tau2 and Hartung-Knapp adjustment (equivalent to rma(..., method="DL",
# test="knha") on escalc(measure="PLO") data).
