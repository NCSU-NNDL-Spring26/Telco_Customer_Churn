# Telco Customer Churn — Machine Learning Project

Predicting customer churn for a telecommunications provider using the **Telco Customer Churn** dataset. The project follows course expectations: **exploratory analysis**, a **baseline classifier**, and a **custom neural network** trained and evaluated with sound ML practice.

**Dataset:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## Intent

- **Business:** Churn is costly; identifying at-risk customers early supports retention programs.  
- **Technical:** Build reproducible pipelines from raw CSV to calibrated evaluation, compare an interpretable baseline to a **custom fully connected network** (no pretrained foundation model), and report metrics suitable for **imbalanced** binary classification.

For a **detailed narrative of what the team implemented** (design choices, file roles, split of labor vs methodology), see **[`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md)**.

---

## Repository contents

| Item | Description |
|------|-------------|
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | Dataset (place Kaggle download here if missing). |
| `telco_churn_baseline.ipynb` | Logistic regression baseline: cleaning, encoding, metrics, confusion matrix. |
| `telco_churn_neural_network.ipynb` | PyTorch **MLP**, leakage-free scaling, stratified splits, validation-tuned threshold, ROC/PR curves vs logistic regression. |
| `requirements.txt` | Python dependencies. |
| `PROJECT_SUMMARY.md` | Team handoff: full explanation of methodology and history. |

---

## Quick start

### 1. Clone and environment

```bash
git clone <this-repo-url>
cd Telco_Customer_Churn
```

Install packages (use `python` instead of `py -3` if that is your default):

```bash
py -3 -m pip install -r requirements.txt
```

### 2. Run the notebooks

1. Open **`telco_churn_baseline.ipynb`** — establishes the baseline story and exploratory steps.  
2. Open **`telco_churn_neural_network.ipynb`** — neural network phase and comparison using the **recommended** evaluation procedure.

Use **Run All** before exporting tables and figures for presentations or posters.

---

## Methodology at a glance

**Baseline (`telco_churn_baseline.ipynb`):**  
Clean data → one-hot encoding → `StandardScaler` → 70/30 split → logistic regression with `class_weight='balanced'` → accuracy, precision, recall, F1, confusion matrix.

**Neural network (`telco_churn_neural_network.ipynb`):**  
Same feature construction; then **stratified 70/15/15** train/validation/test; **scale using training statistics only**; train a custom **MLP** (128→64, dropout) with weighted BCE and early stopping; choose a **probability threshold on validation** (max F1 for churn); report test metrics plus **ROC-AUC** and **PR-AUC**.

Numbers from the two notebooks are **not** directly comparable row-for-row because the NN notebook uses a different (stricter) evaluation design on purpose.

---

## Course compliance (neural network)

- Architecture is **defined in this repo** (custom MLP).  
- **No** pretrained transformer or “foundation model” is used as the churn predictor.  
- All training and inference code needed to verify that is in the notebooks above.

---

## Contributing

- Keep **`PROJECT_SUMMARY.md`** accurate when you change preprocessing, splits, or models.  
- Prefer small, focused commits; avoid committing secrets or huge binary logs.  
- Coordinate poster / video / symposium assets per the course schedule.


---

## License / data

Dataset usage is subject to **Kaggle** and the original data license. This repository holds project code and a local CSV for coursework; redistribution of the CSV may be restricted — check Kaggle terms.
