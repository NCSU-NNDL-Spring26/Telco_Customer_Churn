# Peer Review Video — 5-Minute Presentation Script
**Project:** Cost-Aware Customer Churn Prediction for Telecom Industry
**Team 39 (NNDL.39):** Sree Vathsa Kashyap Mydugolam · Srinidhi Shivashankar · Deekshith Anantha
**Course:** ECE 525 · NC State University · AI Student Symposium 2026

> Target length: **~5:00**.  Word count: **~810 words** at a comfortable presenting pace (~165 wpm).
> Stage directions in *italics*. Pause for ~1 second wherever a `[pause]` marker appears.
> Always be pointing at the poster section you are talking about — the poster is your slide deck.

---

## 0:00 — Opening *(face the camera, then turn slightly toward the poster)*

Hello everyone, I'm **Sree Vathsa**, and along with my teammates **Srinidhi Shivashankar** and **Deekshith Anantha**, we present our project — **Cost-Aware Customer Churn Prediction for the Telecom Industry**.

This is poster **NNDL dot 39**, submitted for ECE 525, the Neural Networks and Deep Learning course at NC State.

In the next five minutes I'll walk you through what problem we tackled, how we approached it with four different models, and the one finding that surprised us most — that the *threshold* you pick at deployment ends up mattering more than the *model* you train. `[pause]`

---

## 0:30 — Section A · Motivation & Problem *(point at top-left panel)*

Customer churn — when a paying subscriber leaves a telecom service — is one of the most expensive problems in the industry. Acquiring a new customer costs five to seven times more than retaining one, so any model that can flag risky customers in advance translates directly into revenue.

But it's a deceptively hard problem for three reasons.

**First — imbalanced labels.** Only 26.6% of customers in our dataset actually churn. A trivial model that predicts "no one churns" would still be 73% accurate. So accuracy is the wrong metric here.

**Second — asymmetric cost.** Missing a churner costs about $1,500 in lost lifetime value, while a false alarm is just a $50 retention call. False negatives are roughly 30 times more expensive than false positives. Optimization must reflect that.

**Third — threshold blindness.** Default classifiers cut off at probability 0.5. That cutoff ignores both the imbalance and the asymmetric cost — so a "good" model with the wrong threshold can still be a poor business tool. `[pause]`

---

## 1:30 — Section B · Data & EDA *(move to top-middle panel)*

We used the **IBM Telco Customer Churn dataset** from Kaggle — 7,032 customers, 19 features after cleaning. Demographics, tenure, contract type, services, and monthly and total charges.

The two figures here tell our exploratory story. On the left, the class balance — 5,163 stayed, 1,869 churned, a 1-to-2.76 minority ratio. On the right, churn rate by contract type, which turned out to be the single strongest signal in the data: **month-to-month customers churn at 43%, while two-year contracts churn at only 3%** — a fourteen-times gap. Short tenure, fiber-optic internet, and electronic-check payments showed similarly strong patterns.

---

## 2:10 — Section C · Methodology *(move to top-right panel)*

To make a fair comparison, we ran four models through **one disciplined pipeline**, shown by this flow diagram. Stratified 70-15-15 train, validation, test split — preserving the 27% churn rate in every fold. Standard scaler fit only on the training data — preventing leakage. The same threshold-tuning procedure on validation. The same metrics on test.

This way, any difference between models comes from the model itself, not from preprocessing tricks. `[pause]`

---

## 2:45 — Section D · Results — Model Comparison *(move to middle-left panel; point at the comparison table)*

Here's where the story gets interesting.

We **started with logistic regression** as our baseline — class-weight balanced, simple, interpretable. It scored an F1 of **0.61** and a ROC-AUC of **0.83**. A solid result on tabular data.

We **then built our custom MLP** — 128 to 64 to 1 architecture, ReLU and dropout, weighted binary cross-entropy, Adam optimizer, early stopping. This was the course requirement — a custom neural network we designed ourselves. And surprisingly, **the MLP did not beat logistic regression**. F1 of 0.60. Almost identical.

This is itself a meaningful finding. On small one-hot tabular data — about 7,000 rows and 30 features — a linear decision boundary is already most of the signal. Nonlinear capacity adds very little.

So we **moved to gradient-boosted trees — XGBoost and CatBoost**. CatBoost emerged as our strongest classifier — F1 of **0.624**, ROC-AUC of **0.841**, and importantly the **lowest Brier score, 0.139**. Brier measures calibration: when CatBoost says "70% chance of churn," it means 70%. That's not just rank quality, that's *trustworthy probabilities*. `[pause]`

---

## 3:50 — Section E · Cost-Aware Analysis *(move to middle-right panel; point at $370K card and cost curve)*

But here's the finding that drives our title.

We translated those model probabilities into dollars. We swept the decision threshold under realistic costs — $1,500 for a missed churner, $50 for a false alarm — and computed the net business value at each threshold.

What we found: **every one of our four models converges to about $370,000 of net value per 1,000 customers** when the threshold is properly tuned. The architecture-to-architecture gap is less than 1%. The threshold matters more than the model.

And our **counterfactual analysis**, shown in the strip below, ties this back to action. For our highest-risk customer at 0.93 churn probability, perturbing one feature — switching internet service from fiber-optic to none — drops the prediction to 0.82. The model points to a *specific retention lever* for each customer.

---

## 4:30 — Section F · What Drives Churn  + Section G · Conclusions *(point at feature importance, then conclusions)*

CatBoost's feature importances confirm the EDA — tenure, contract type, fiber-optic, and electronic-check payments dominate, all aligned with industry intuition.

So our **conclusions**: CatBoost is the strongest classifier; the custom MLP is a meaningful negative result; **cost-aware threshold tuning is the dominant lever**; and counterfactuals turn probabilities into actions.

**Limitations:** the dataset is a static snapshot, and our cost ratios are illustrative — real numbers vary by segment. **Next steps:** stacking ensembles, cost-sensitive loss directly inside MLP training, monthly recalibration, and a live A/B test of the threshold.

---

## 5:00 — Closing *(face camera again)*

Thank you for your time. We'd love to discuss this with you in person at the symposium. *(short pause)* This is Team 39, ECE 525, AI Student Symposium 2026.

---

## Delivery checklist

- [ ] Practice once with a stopwatch — aim for 4:50, not exactly 5:00, to leave room for natural pauses.
- [ ] Memorize three numbers cold: **27% churn**, **30× cost ratio**, **$370K per 1,000 customers**.
- [ ] Always point at the poster section you're talking about. The pointing is what makes the video feel like a poster walk-through, not a narrated slideshow.
- [ ] The pivot moment is Section D → Section E ("But here's the finding that drives our title"). Pause briefly before that line — it's your "wow" beat.
- [ ] Keep the camera and the poster both in frame so the reviewer can follow what you're indicating.
- [ ] Speak slightly slower than you think you need to. Aim for ~165 words per minute, not 200.

## Likely peer-review questions and 1-line answers

| Question | Answer |
|---|---|
| Why didn't your MLP beat logistic regression? | Small one-hot dataset (~7K rows, ~30 features) — the decision boundary is already mostly linear. Nonlinearity needs more data or richer features. |
| Why CatBoost over XGBoost? | They tie on PR-AUC, but CatBoost wins on F1 and Brier — better-calibrated probabilities, which matter for cost-aware thresholding. |
| What happens if cost ratios change? | Re-tune the threshold on validation under the new ratio. The model itself doesn't need retraining. |
| How would you deploy this? | Save the CatBoost model, the fitted scaler, and the chosen threshold (0.31 for max-F1). Score new customers monthly; recalibrate threshold quarterly. |
| Why include the 20% capacity constraint? | Real retention teams have limited bandwidth — the constrained scenario is closer to operational reality. |
| Are the cost numbers realistic? | They're illustrative ($1500 LTV, $50 outreach). The methodology — sweep threshold, pick optimum on validation — applies for any real cost ratio. |
