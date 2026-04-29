# Telco Customer Churn Prediction — Symposium Presentation Script

---

## Problem

Telecommunications providers lose significant recurring revenue each month to voluntary customer attrition. Predicting which subscribers are at risk before they cancel enables proactive retention campaigns far less expensive than re-acquisition. We address the Telco Customer Churn dataset, a publicly available benchmark comprising 7,043 residential accounts with 30 behavioral, contractual, and service-adoption attributes. With a 26 percent positive-class rate, the dataset exhibits class imbalance that renders accuracy an unreliable selection criterion. We therefore evaluate all systems primarily on area under the precision-recall curve and a business cost function reflecting the asymmetric consequences of missed detections versus unnecessary interventions.

---

## Data

The dataset originates from a US telecommunications carrier, comprising 7,032 accounts from a single observation window after removing eleven records with missing total-charges values. Continuous predictors—tenure in months, monthly recurring charge, and lifetime total charges—were retained without transformation. The 17 categorical attributes, including contract type, internet service tier, and payment method, were one-hot encoded with the alphabetically first level dropped. We applied a stratified 70/15/15 split by churn label to preserve the approximately 26.5 percent minority-class rate across all three partitions. The validation set served exclusively for threshold selection; the test set was withheld until final evaluation.

---

## Methodology

We trained and evaluated four model families. Logistic regression with balanced class weights served as a linear baseline. A three-layer multilayer perceptron trained with binary cross-entropy and a class-ratio positive weight of 2.76 captured nonlinear interactions. CatBoost and XGBoost underwent light grid searches over 36 and 72 candidate configurations, respectively, with validation PR-AUC as the selection criterion. All continuous features were standardized using a scaler fitted exclusively on the training partition. Decision thresholds were selected on the validation set by maximizing F1 on the minority class. SHAP values and a threshold-aware business cost function quantified each model's practical significance.

---

## Results

On the held-out test partition, all four models achieved ROC-AUC scores between 0.826 and 0.841, indicating strong rank-ordering ability. CatBoost and XGBoost each achieved precision-recall AUC of approximately 0.642, outperforming logistic regression (0.591) and the MLP (0.592) on this imbalance-sensitive metric. Brier scores confirmed adequate probability calibration for the boosted ensembles. The business cost analysis, assuming a false-negative cost of 1,500 dollars and a false-positive cost of 50 dollars, found that optimal threshold selection reduced expected cost per customer by 120 to 180 dollars relative to the no-intervention baseline, yielding substantial net value per 1,000 targeted accounts.

---

## Business Decision

We recommend deploying XGBoost or CatBoost as the production churn model, selecting the threshold that minimizes expected financial cost rather than maximizing classification accuracy. With a threshold near 0.30 to 0.35, CatBoost identifies approximately 77 percent of churning customers while maintaining acceptable false-positive volume. At retention-offer economics of 50 dollars per false alarm and 1,500 dollars per missed churner, the optimal operating point recovers substantial net value relative to a passive strategy or a fixed 0.50 cutoff. Counterfactual analysis reveals that contract type and internet service tier carry the greatest individual leverage on predicted churn probability, directly informing product and promotional interventions.

---

## Takeaway

Gradient-boosted ensembles offer meaningful lift over logistic regression and neural-network baselines on this class-imbalanced churn problem, but the operational advantage materializes primarily through cost-aware threshold selection rather than raw discriminative performance alone. SHAP analysis and counterfactual profiling transform outputs into actionable business intelligence, identifying which service attributes most strongly predict defection and what changes would plausibly retain high-risk subscribers. Future work should incorporate temporal customer trajectories, refresh thresholds periodically against live churn rates, and monitor for calibration drift—steps that would position the model as a sustainable and auditable component of a data-driven retention program.
