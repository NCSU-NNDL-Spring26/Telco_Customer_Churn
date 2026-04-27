# Project summary — Telco Customer Churn (team handoff)

This document describes **what has been implemented in this repository**, **why design choices were made**, and **how teammates can pick up the work**. It is meant to stay in sync with the notebooks and code; update it when you change the pipeline.

---

## 1. Course context (high level)

The course project asks for:

- Exploratory analysis and understanding of the data  
- A **baseline** model  
- A **custom neural network** (students design and optimize the architecture — **not** a pretrained “foundation model”)  
- Code in the repository so instructors can verify methodology  

External data used only for pretraining a **custom** model may be allowed per instructor guidance; **this repo does not** use pretrained transformers or foundation models for churn prediction.

Team deliverables outside this repo include presentation materials, symposium poster, and recorded updates per the syllabus — coordinate dates on Moodle / course channels.

---

## 2. Problem statement

**Goal:** Predict whether a telecom customer will **churn** (leave) using tabular features such as contract type, tenure, monthly charges, services, and demographics.

**Why it matters:** Retention campaigns are cheaper than acquisition; models rank or score customers so the business can target interventions. Evaluation should reflect **imbalanced** labels (fewer churners than non-churners) and **business tradeoffs** (false negatives vs false positives), not accuracy alone.

---

## 3. Dataset

- **Source:** [Telco Customer Churn on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- **Local file in repo:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`  
- **Target:** `Churn` — `Yes` / `No` (modeled as binary 1 / 0)  
- **Rows:** ~7,000 customers (exact count after cleaning matches dropped rows with invalid `TotalCharges`)

**Do not commit large derived artifacts** unless the team agrees (e.g. saved models); keep the canonical dataset path documented here.

---

## 4. What we built in this repository (chronological)

### 4.1 Baseline notebook — `telco_churn_baseline.ipynb`

**Purpose:** Simple, interpretable baseline aligned with an early project update / video narrative.

**Pipeline:**

1. Load CSV; drop `customerID`.  
2. Coerce `TotalCharges` to numeric; drop rows with missing values after coercion.  
3. Map `Churn` to 0/1.  
4. One-hot encode categoricals with `pandas.get_dummies(..., drop_first=True)`.  
5. **Scale** all features with `StandardScaler` **before** train/test split (`fit_transform` on full feature matrix — see note below).  
6. Train/test split **70% / 30%**, `random_state=42`.  
7. **Logistic regression** with `class_weight='balanced'` to mitigate class imbalance.  
8. Metrics: accuracy, precision, recall, F1, classification report, confusion matrix.

**Note on methodology:** Scaling before splitting leaks test distribution into the scaler statistics. That matches the **original baseline story** for consistency with the submitted update, but it is **not** the recommended procedure for deployment. The neural network notebook uses the corrected order (fit scaler on train only).

---

### 4.2 Neural network notebook — `telco_churn_neural_network.ipynb`

**Purpose:** Satisfy the course requirement for a **custom fully connected network** and compare it to logistic regression using a **deployment-oriented evaluation** (usable procedure, not just default 0.5 threshold).

#### Model architecture (PyTorch)

- Class name in code: **`ChurnMLP`**  
- Structure: hidden layers **128 → 64**, **ReLU**, **Dropout** (0.2), single logit output  
- Loss: **`BCEWithLogitsLoss`** with **`pos_weight = neg/pos`** on the **training** fold so positive class (churn) is weighted similarly in spirit to `class_weight='balanced'` in sklearn  

#### Training

- Optimizer: **Adam**, learning rate `1e-3`, weight decay `1e-4`  
- Mini-batch training; **early stopping** on **validation** loss with patience 30  

#### Evaluation procedure (current version — important for collaborators)

This notebook intentionally **does not** mirror every detail of `telco_churn_baseline.ipynb`, because the goal was a **sound workflow**:

| Step | What we do |
|------|------------|
| Splits | **Stratified** **70% train / 15% validation / 15% test** — preserves churn rate in each split |
| Scaling | **`StandardScaler` fit only on training data**; validation and test are **`transform` only** — avoids leakage |
| Probabilities | LR uses `predict_proba`; MLP uses `sigmoid(logits)` |
| Threshold | Default **0.5 is not assumed** for final class labels. A **threshold is chosen on the validation set** to maximize **F1 score** on the churn class, then applied to the **test** set **once** for reporting |
| Ranking metrics | **ROC-AUC** and **PR-AUC** (average precision) on test for both models — strong for imbalanced classification and for “who to contact first” |
| Plots | Train/val loss, side-by-side confusion matrices, ROC and precision–recall curves |

**Implication:** Test metrics from this notebook **will not numerically match** screenshots taken from an earlier NN version that used 70/30 + scale-before-split + threshold 0.5. That is expected; cite this notebook for the **final methodology** in reports and posters.

---

## 5. Repository layout

| Path | Role |
|------|------|
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | Local copy of the Kaggle dataset |
| `telco_churn_baseline.ipynb` | EDA-style baseline (logistic regression); documents early project stage |
| `telco_churn_neural_network.ipynb` | Custom MLP + logistic comparison with leakage-free preprocessing and threshold tuning |
| `requirements.txt` | Python dependencies (`numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `torch`) |
| `PROJECT_SUMMARY.md` | This handoff document |
| `README.md` | Short project overview and quick start for anyone cloning the repo |

---

## 6. Environment and how to run

1. **Python:** Use a current 3.x install (team members on Windows often use `py -3` if multiple Pythons exist).  
2. **Install dependencies:**

   ```bash
   py -3 -m pip install -r requirements.txt
   ```

3. **Run notebooks** in suggested order:  
   - `telco_churn_baseline.ipynb` — baseline narrative  
   - `telco_churn_neural_network.ipynb` — full NN + comparison  

Execute **Run All** so outputs (metrics, figures) are saved if you commit notebook outputs for grading or the poster.

---

## 7. Results snapshot (illustrative — re-run notebooks for exact numbers)

Earlier runs showed **logistic regression** and the **MLP** performing **similarly** on this dataset: shallow nonlinearities do not always beat a strong linear baseline on one-hot encoded tabular data. The **updated** notebook adds **ROC-AUC / PR-AUC** and **validation-based thresholds** so differences are interpreted correctly.

**Do not hard-code numbers in the poster** — copy from your latest notebook run after pulling main.

---

## 8. Suggested next steps for teammates

- Pull latest `main`, install `requirements.txt`, rerun both notebooks.  
- Export figures (confusion matrices, ROC/PR curves, comparison table) for poster / slides.  
- Align spoken narrative: baseline (simple, interpretable) vs MLP (nonlinear capacity, proper evaluation).  
- If instructors ask for reproducibility: note **random seeds** (`SEED = 42`) in the NN notebook.  
- Optional improvements (only if course time allows): threshold rule tied to **minimum recall** or cost matrix; save `torch` `state_dict` + scaler + threshold as artifacts — not required unless the syllabus asks.

---

## 9. Contact / ownership

Update this file when someone changes splits, metrics, or dependencies. Mention in PR or chat so the rest of the team rebases and reruns notebooks before capturing final numbers.
