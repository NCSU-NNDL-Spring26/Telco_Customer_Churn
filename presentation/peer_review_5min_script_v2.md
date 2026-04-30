# Peer Review Video — 5-Minute Script  (v2 — Trimmed)
**Project:** Cost-Aware Customer Churn Prediction for Telecom Industry
**Team 39 (NNDL.39):** Sree Vathsa Kashyap Mydugolam · Srinidhi Shivashankar · Deekshith Anantha
**Course:** ECE 525 · NC State University · AI Student Symposium 2026

> **Why this exists.** v1 ran ~8 min for the team. v2 is **~480 words → ~4:45 spoken** at a slow, clear pace (~100 wpm) — leaving 15 seconds of buffer. Keep the story arc, drop the long sentences.
>
> Stage directions in *italics*. Pause briefly at every `[pause]`.

---

## 0:00 — Opening *(face camera)*

Hi, we're **Team 39 — Sree Vathsa, Srinidhi, and Deekshith**. Our project is **Cost-Aware Customer Churn Prediction for the Telecom Industry**. Poster NNDL.39 for ECE 525.

In five minutes, I'll walk you through what we built and the one finding that surprised us — that the **threshold** you pick at deployment matters more than the **model** you train. `[pause]`

---

## 0:25 — Section A · Motivation *(point top-left)*

Customer churn is one of the most expensive problems in telecom. Acquiring a new customer costs **5 to 7 times more** than retaining one.

The problem is hard for three reasons:

- **Imbalanced** — only **27% of customers churn**, so accuracy is misleading.
- **Asymmetric cost** — missing a churner costs about **$1,500**; a false alarm costs **$50**. False negatives are **30 times worse**.
- **Threshold blindness** — the default 0.5 cutoff ignores both. `[pause]`

---

## 1:15 — Section B · Data & EDA *(point top-middle)*

We used the **IBM Telco Customer Churn dataset** from Kaggle — **7,032 customers, 19 features**.

The strongest signal is contract type: **month-to-month customers churn at 43%, two-year contracts at 3%** — a fourteen-times gap. Tenure, fiber-optic internet, and electronic-check payment show similar patterns.

---

## 1:45 — Section C · Methodology *(point top-right)*

We ran **four models** through one disciplined pipeline. Stratified 70-15-15 split. Scaler fit only on training data. Same threshold tuning. Same metrics. So any difference comes from the model itself, not preprocessing.

---

## 2:10 — Section D · Model Comparison *(point middle-left, table)*

This is where the story gets interesting.

We **started with logistic regression** — F1 of **0.61**, ROC-AUC **0.83**. A strong baseline.

We **then built our custom MLP**, the course requirement — and **it didn't beat logistic regression**. F1 of 0.60. That's a meaningful finding: on small one-hot tabular data, the boundary is already mostly linear.

So we **moved to gradient-boosted trees**. **CatBoost won** — F1 **0.624**, ROC-AUC **0.841**, and the **lowest Brier score, 0.139**. Brier measures calibration — CatBoost's probabilities are trustworthy, not just its rankings. `[pause]`

---

## 3:15 — Section E · Cost-Aware Analysis *(point middle-right, $370K card)*

Here's the finding that drives our title.

We translated probabilities into dollars by sweeping the threshold under realistic costs — **$1,500 per miss, $50 per false alarm**.

**Every model recovered about $370,000 of net value per 1,000 customers** when the threshold was tuned. The architecture-to-architecture gap is less than 1%. **The threshold matters more than the model.**

Our **counterfactual** ties this to action — for the highest-risk customer at 0.93 probability, switching internet from fiber to none drops it to 0.82. The model points to a specific lever per customer. `[pause]`

---

## 4:15 — Sections F & G · Drivers + Conclusions *(sweep across bottom)*

Feature importances confirm the EDA — tenure, contract, fiber, electronic check.

**Conclusions:** CatBoost is strongest. The MLP is a meaningful negative result. **Cost-aware threshold tuning is the dominant lever.** Counterfactuals turn probabilities into actions.

**Limitations:** static dataset, illustrative cost ratios. **Next steps:** stacking, cost-sensitive loss in MLP, A/B test the threshold.

---

## 4:50 — Closing *(face camera)*

Thanks. Team 39, AI Student Symposium 2026.

---

## Quick delivery tips

- **3 numbers to memorize:** 27% churn · 30× cost ratio · $370K per 1,000.
- **The pivot beat is D → E** ("Here's the finding that drives our title"). Pause before it.
- **Always be pointing.** The poster is your slide deck.
- **Time yourself** — if you finish under 4:30, slow down. If over 5:10, drop the limitations sentence in G.
