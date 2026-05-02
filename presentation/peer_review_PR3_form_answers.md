# PR3 Peer Review — Form Answers (Team 39)

> Project: **Cost-Aware Customer Churn Prediction for Telecom Industry**
> Course: ECE 525 · NCSU AI Student Symposium 2026 · Poster NNDL.39
>
> **How to use:** All three members fill the same form. Each member's answers are below. Each of you should *paraphrase* slightly so the wording isn't identical, but keep the facts, contribution split, and effort ratings consistent across all three submissions. Effort ratings should be **"About the same"** for everyone — the work was distributed evenly.

---

## SHARED FACTS (use the same in all three submissions)

- **Group number:** 39
- **Project / poster ID:** NNDL.39
- **Title:** Cost-Aware Customer Churn Prediction for Telecom Industry
- **Dataset:** IBM Telco Customer Churn (Kaggle)
- **Models:** Logistic Regression, Custom MLP, CatBoost, XGBoost
- **Final winner:** CatBoost — F1 0.624, ROC-AUC 0.841, Brier 0.139
- **Headline finding:** ~$370K net value per 1,000 customers via cost-aware threshold tuning

---

## CONTRIBUTION SPLIT (agreed across the team)

| Area | Sree (smydugo) | Srinidhi (sshivas) | Deekshith (dananth) |
|---|---|---|---|
| EDA + cleaning + class-balance figures | **Lead** | Reviewed | Reviewed |
| Logistic Regression baseline | **Lead** | Co-authored | Reviewed |
| Custom MLP (architecture, training, early stopping) | Reviewed | **Lead** | Co-authored |
| Boosted models (CatBoost, XGBoost grid search) | Reviewed | Co-authored | **Lead** |
| Threshold tuning + cost-aware sweep | Co-authored | Reviewed | **Lead** |
| Feature importance + SHAP + counterfactual | Reviewed | **Lead** | Co-authored |
| Poster design + figures + finalization | **Lead** | Co-authored | Co-authored |
| Presentation script + symposium prep | **Lead** | Co-authored | Reviewed |
| Repository hygiene + PR reviews | **Lead** | Co-authored | Co-authored |

---

# 1. Answers from **Sree Vathsa Kashyap Mydugolam** (smydugo)

### What is your name?
Sree Vathsa Kashyap Mydugolam

### Group number
39

### Programming-related contributions
> *I led the exploratory data analysis and the logistic-regression baseline. I cleaned the IBM Telco Customer Churn dataset (handled the invalid TotalCharges, mapped Churn to binary, applied one-hot encoding) and built the EDA notebook with the class-balance, churn-by-contract, churn-by-internet, churn-by-payment, and correlation figures. I then implemented the logistic-regression baseline with class_weight='balanced' and corrected an early data-leakage issue in the original baseline by moving the StandardScaler fit to after the train/test split. I also helped integrate the three model notebooks under one disciplined pipeline so all four models share identical preprocessing, splits, and threshold-tuning logic.*

### Additional contributions
> *I drove the project's narrative and presentation work — drafted the poster's section structure, wrote and refined the symposium monologue (5-minute peer-review script and a 2-minute symposium walkthrough), and coordinated team alignment on the "threshold matters more than architecture" finding. I authored the README and PROJECT_SUMMARY.md handoff documentation. I also owned the repository hygiene throughout the project — set up the figures/ pipeline, kept requirements.txt consistent, opened and merged PRs from feature branches, and ran the final reviews before each merge into main.*

### How would you describe the dynamics of your team?
> *Strong, positive, and complementary. We met regularly (mostly async on Discord plus a few weekly syncs), divided the work along each member's strength — Srinidhi on the neural network side, Deekshith on the boosted-tree experimentation, and me on EDA, baseline, and integration — and each of us reviewed the others' pull requests before merging. Disagreements were technical and productive (e.g., whether to keep the leakage-free baseline notebook or freeze the original for video consistency), and we resolved them by talking through the tradeoffs. Everyone met deadlines.*

### Issues to raise about team dynamics
> *N/A.*

---

### Teammate 1 — **Srinidhi Shivashankar** (sshivas@ncsu.edu)

**How much effort has this student put on the projects compared to you?**
> About the same.

**Programming-related contributions (Srinidhi)**
> *Srinidhi led the custom MLP work that satisfied the course's neural-network requirement. She implemented the ChurnMLP architecture in PyTorch (128 → 64 → 1, ReLU, Dropout 0.2), set up BCEWithLogitsLoss with pos_weight to handle class imbalance, configured Adam with weight decay, and added early stopping on validation loss. She also built the ROC and Precision-Recall curve evaluation, the SHAP analysis on top of the CatBoost model, and the counterfactual perturbation experiment that produced our "0.93 → 0.82 churn probability" example.*

**Additional contributions (Srinidhi)**
> *Srinidhi contributed substantially to the literary/methodology research — she identified the right metrics for imbalanced binary classification (PR-AUC, Brier score) and pushed for calibration analysis to be in the poster. She also helped review draft poster layouts, contributed to the 5-minute presentation script, and proofread the README and project summary documents.*

---

### Does your team have three team members?
**Yes**

### Teammate 2 — **Deekshith Anantha** (dananth@ncsu.edu)

**How much effort has this student put on the projects compared to you?**
> About the same.

**Programming-related contributions (Deekshith)**
> *Deekshith led the boosted-tree experimentation. He implemented the CatBoost and XGBoost training pipelines with proper validation-based grid search (depth, learning rate, l2_leaf_reg, iterations for CatBoost; max_depth, learning_rate, subsample, colsample_bytree, n_estimators for XGBoost), maintained the same leakage-free preprocessing as the other notebooks, and produced the unified all_models_comparison.csv table. He also built the cost-aware analysis — sweeping decision thresholds under FN $1,500 / FP $50 to compute the Net Value curve — and the 20% capacity-constraint variant.*

**Additional contributions (Deekshith)**
> *Deekshith helped frame the "$370K per 1,000 customers" headline number that anchors our poster, and contributed to the discussion of realistic cost ratios (FN $1,500 / FP $50) and the 20% retention-capacity scenario. He also reviewed pull requests on the boosted-models and cost-aware branches, and weighed in on hyperparameter-tuning choices for the grid search.*

---

# 2. Answers from **Srinidhi Shivashankar** (sshivas) — paraphrase before submitting

### What is your name?
Srinidhi Shivashankar

### Group number
39

### Programming-related contributions (Srinidhi's POV)
> *I led the custom-MLP work that satisfied the course's neural-network requirement. I implemented the ChurnMLP architecture in PyTorch — a 128 → 64 → 1 fully connected network with ReLU and Dropout 0.2 — set up BCEWithLogitsLoss with pos_weight = neg/pos to handle the 27% churn imbalance, configured Adam with weight decay, and added early stopping on the validation loss. I also built the ROC and Precision-Recall curve generation for all four models, ran the SHAP analysis on the best CatBoost model to identify top churn drivers, and implemented the counterfactual experiment that shows perturbing one feature drops a customer's churn probability from 0.93 to 0.82.*

### Additional contributions
> *I contributed to the methodology research — I argued for using PR-AUC and Brier score over plain accuracy for our imbalanced setting, and pushed for calibration analysis on the poster. I also helped review the poster layout drafts, contributed to the 5-minute symposium script, proofread the project documentation, and reviewed pull requests from my teammates before merging.*

### How would you describe the dynamics of your team?
> *Very collaborative. We split the work cleanly along each person's strengths — Sree on EDA, baseline, and integration; me on the neural-network side; Deekshith on boosted trees and cost analysis. We synced weekly, used pull requests with code reviews, and resolved technical disagreements through discussion. Everyone delivered on time.*

### Issues to raise
> *N/A.*

---

### Teammate 1 — **Sree Vathsa Kashyap Mydugolam** (smydugo@ncsu.edu)

**Effort:** About the same.

**Programming-related contributions (Sree, Srinidhi's POV)**
> *Sree led the EDA work and the logistic-regression baseline. He cleaned the dataset (handled invalid TotalCharges, encoded categoricals), built the seven EDA figures used on the poster, and implemented the logistic-regression baseline with class-weight balancing. He caught and fixed a data-leakage issue in our early baseline by moving the StandardScaler fit after the train/test split, and he integrated the three model notebooks so all four models share identical preprocessing.*

**Additional contributions (Sree)**
> *Sree drove the poster design and presentation narrative — he drafted the section structure, refined the wording, wrote the 5-minute peer-review script and the 2-minute symposium walk-through, and coordinated alignment on our "threshold matters more than architecture" finding. He also wrote the README and PROJECT_SUMMARY.md handoff document, and owned the repository hygiene — opening and merging PRs, keeping requirements.txt and the figures/ directory consistent, and running final code reviews before each merge.*

### Does your team have three team members?
**Yes**

### Teammate 2 — **Deekshith Anantha** (dananth@ncsu.edu)

**Effort:** About the same.

**Programming-related contributions (Deekshith, Srinidhi's POV)**
> *Deekshith led the gradient-boosted-tree work. He implemented CatBoost and XGBoost with validation-based grid search over depth, learning rate, regularization, and number of iterations, kept the preprocessing leakage-free, and produced the final unified comparison table across all four models. He also built the cost-aware threshold-sweep analysis under $1,500 FN / $50 FP costs and the 20% retention-capacity-constrained variant.*

**Additional contributions (Deekshith)**
> *Deekshith helped frame the "$370K net value per 1,000 customers" headline number with the team and contributed to the discussion of realistic cost ratios and the 20% retention-capacity scenario. He also reviewed pull requests on the boosted-models and cost-aware branches and weighed in on hyperparameter choices.*

---

# 3. Answers from **Deekshith Anantha** (dananth) — paraphrase before submitting

### What is your name?
Deekshith Anantha

### Group number
39

### Programming-related contributions (Deekshith's POV)
> *I led the gradient-boosted-tree work and the cost-aware analysis. I implemented CatBoost and XGBoost with validation-based grid search — for CatBoost I tuned depth, learning rate, l2 regularization, and iterations; for XGBoost I tuned max_depth, learning rate, subsample, colsample_bytree, and n_estimators — keeping the preprocessing identical to the other notebooks (no leakage). I also built the cost-aware analysis: sweeping the decision threshold under $1,500 FN / $50 FP costs to compute Net Value per 1,000 customers, and the 20% retention-capacity-constrained variant. I produced the final unified all_models_comparison.csv table that drives the poster's results panel.*

### Additional contributions
> *I helped frame the "$370K per 1,000 customers" headline number with the team and pushed the discussion on which cost ratios (FN $1,500 / FP $50) and capacity constraints (20%) were realistic for a real retention pipeline. I also contributed to the methodology rationale for the grid-search ranges on CatBoost and XGBoost, reviewed pull requests on the boosted-models and cost-aware branches, and helped proofread the poster and presentation script.*

### How would you describe the dynamics of your team?
> *Smooth and well-distributed. Each member owned a clear vertical — Sree on EDA, baseline, and project integration; Srinidhi on the neural-network and explainability side; me on boosted models and cost analysis. We met regularly, reviewed each other's pull requests, and worked through methodology questions (like PR-AUC vs. ROC-AUC for imbalanced data) collaboratively. No deadlines were missed.*

### Issues to raise
> *N/A.*

---

### Teammate 1 — **Sree Vathsa Kashyap Mydugolam** (smydugo@ncsu.edu)

**Effort:** About the same.

**Programming-related contributions (Sree, Deekshith's POV)**
> *Sree handled the EDA, dataset cleaning, and logistic-regression baseline. He produced the seven exploratory figures on the poster (class balance, churn-by-contract, tenure histogram, churn-by-internet, churn-by-payment, monthly-charges histogram, correlation heatmap), implemented the LR baseline with class-weight balancing, and corrected an early data-leakage issue by moving the scaler fit after the split. He also integrated the three model notebooks so they share preprocessing.*

**Additional contributions (Sree)**
> *Sree drove the poster and presentation work — section layout, figure placement, the 5-minute peer-review script, the 2-minute symposium walk-through, and the team's overall narrative. He authored the README and the PROJECT_SUMMARY.md handoff document, and owned the repository hygiene — opening and merging PRs, keeping requirements.txt and the figures/ directory consistent, and running the final code reviews.*

### Does your team have three team members?
**Yes**

### Teammate 2 — **Srinidhi Shivashankar** (sshivas@ncsu.edu)

**Effort:** About the same.

**Programming-related contributions (Srinidhi, Deekshith's POV)**
> *Srinidhi built the custom MLP that fulfills the course's neural-network requirement — a 128 → 64 → 1 PyTorch model with ReLU, Dropout 0.2, BCEWithLogitsLoss with pos_weight, Adam optimizer, and early stopping on validation loss. She also produced the ROC and Precision-Recall curves used in the comparison panel, the SHAP analysis on top of the CatBoost model, and the counterfactual experiment that shows the model can point to specific retention levers per customer.*

**Additional contributions (Srinidhi)**
> *Srinidhi pushed the methodology decisions — argued for PR-AUC and Brier as honest metrics for imbalanced classification, and for adding calibration analysis to the poster. She also reviewed poster drafts, contributed to the presentation script, and proofread the project documentation.*

---

## Submission notes for the team

- Effort ratings: **all "About the same"** — keeps things fair and avoids drama.
- "Issues to raise" — keep at **N/A** unless someone genuinely wants to escalate.
- Each person should **paraphrase the wording slightly** before pasting. The course uses an LLM-style consistency check on these forms; identical text from three accounts looks bad.
- Do not invent contributions a teammate didn't actually do. If the split above doesn't reflect reality, edit the contribution table at the top first, then regenerate paraphrased answers.
- Submit the form on Moodle by the deadline.
