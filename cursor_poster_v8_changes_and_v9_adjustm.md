# Poster v8 changes and v9 adjustments
_Exported on 4/29/2026 at 23:02:46 EDT from Cursor (3.2.11)_

---

**User**

I was running claude code till now, it ran out of tokens, hence i want you to continue where it left off. 

Conversation till now

Created a file, ran a command
poster_v8.pptx is ready. Here's a quick map of what changed everywhere.

What's different in v8
A. Motivation — quadrupled body
Hook paragraph (2 sentences)
Stakes paragraph in wine italic: "For a mid-size carrier with 1M subscribers and 25% churn, even a 3% reduction = ~7,500 retained customers/year, worth millions in LTV."
3 chips, each now with a 2-sentence body (not 1 fragment)
B. Data & EDA — class balance restored
Both EDA figures side by side — class balance (left, 42% width) + churn-by-contract (right, 58% width)
"What the data tells us" interpretation block: 4 dense bullets covering imbalance ratio, contract gap (14×), tenure cluster, fiber and electronic-check patterns
C. Methodology — "Why each step" block
Pipeline diagram unchanged
New rationale section instead of generic model legend:
Why stratified split (preserves churn rate)
Why train-only scaling (prevents leakage)
Why threshold tuning (default 0.5 is arbitrary on imbalance)
Why Brier + PR-AUC (calibration + minority-class ranking)
D. Model Comparison — interpretation top + bottom
Above table: 2-line narrative explaining what was done + what Brier captures
Below table: 2-line interpretation explaining why CatBoost wins and why MLP ties LR
ROC/PR figure unchanged size (large)
E. Cost-Aware Analysis — fixed
Cost curve now spans full panel width and gets ~3.7" vertical space (was ~2.8")
Counterfactual reformatted as a horizontal 3-column strip along the bottom: Highest-risk customer → Switch InternetService → predicted churn = 0.82 (-11 pp) with arrows between. No more clipping.
F. What Drives Churn — substantive interpretation
Image + table same
Right-side interpretation block now reads: "These align with industry intuition: short tenure (no commitment yet), no long-term contract (low switching cost), fiber (price-sensitive segment), electronic check (no auto-pay lock-in)..." + an actionable line about contract upsell campaigns
G. Conclusions — 2-column substantive content
LEFT: 4 numbered findings
RIGHT: 3 sub-blocks
Deployment readiness (what to save, recalibration cadence)
Limitations (static snapshot, illustrative cost ratios)
Next steps (stacking, cost-sensitive loss, A/B test)
Layout
ROW1: y=5.8–16.8 (h=11.0)
ROW2: y=17.0–28.9 (h=11.9) — bigger for E's cost curve
ROW3: y=29.1–34.3 (h=5.2)
References: y=34.4–35.8 (h=1.4)
Header text in top-right is now NNDL.39.
Things to verify when you open
✅ Cost curve in E is large and readable
✅ Counterfactual's "-11 pp" line is fully visible (horizontal strip, not stacked card)
✅ Section B has both EDA figures
✅ Section A reads like a real motivation, not bullet fragments
✅ Section G has substantive content (not filler)
⚠️ Verify NNDL.39 displays correctly in the top-right black bar
If anything's still cramped or overflowing, point at the section and I'll output v9.

Fix this and we are good to go

Make this 370k to right(make it small) , make this picture lot bigger like super big.

Created
_build_poster_v9.py
+571
-0
API Error
You're out of extra usage · resets 10:30pm (America/New_York)


Look into it

---

**Cursor**

Reviewing `_build_poster_v9.py` to locate the "370k" element and the image to resize.



Implementing changes: placing a narrow, right-aligned small "~$370K" label and maximizing vertical space for the cost-curve image by tightening the top row and margins.



Running the script to verify it generates `poster_v9.pptx`.



Here’s what was left from the interrupted session and what I changed.

### Continuation summary
`_build_poster_v9.py` was already complete in the repo; the failure was only **API quota**, not the script. I adjusted section **E** to match your notes: **small ~$370K on the right** and a **much taller cost curve**.

### Changes in `_build_poster_v9.py`

1. **`~$370K` — right + small**  
   - Card is **narrow** (`min(2.15", 22% of panel)`), **flush to the right** (`card_x = cx + cw - card_w`).  
   - Main line **`Pt(34)` → `Pt(17)`**; subtitles **`Pt(13/11)` → `Pt(9/8)`**; shorter copy (`net / 1K cust.`, `(thr.-tuned)`).  
   - Paragraph alignment **`CENTER` → `RIGHT`** inside that strip.  
   - Thinner border so it stays a label, not a second focal panel.

2. **Cost table gets width**  
   - Table uses **`cw - card_w - gap`** (~78% of the row instead of 65%), so the optima table is easier to read next to the small KPI strip.

3. **Cost curve — taller (“super big”)**  
   - **`top_row_h`**: `2.30` → **`1.85`**.  
   - Slightly tighter narrative and constraint lines so **`cc_max_h`** grows by roughly **0.7–0.8"** plus **`1.10` → `0.98`** reserved for the counterfactual strip.

### Run locally
Your default `python` on PATH may be MSYS without `pip`/PIL. The script **did run successfully** with:

`py -3 _build_poster_v9.py`

It printed **`Wrote poster_v9.pptx`**.

Open **`poster_v9.pptx`** and check section **E**: the curve should dominate the column and **`~$370K`** should sit small on the **far right**. If you want the KPI even smaller or moved **below** the table instead, say which you prefer and we can tweak once more.

---

**User**

Give more content for this

---

**Cursor**

Reviewing the Motivation section layout so we can add hook content without breaking the poster.



Expanding the hook with two substantive sentences on churn dynamics and operational use of predictions, and adjusting the text box height so the column still fits.



Here’s what was added and how the layout was adjusted.

### New hook content (two extra sentences)
After your original two lines, the poster now includes:

1. **Churn dynamics** — Weak signals (usage, support load, billing friction) often show up **before** cancel, so there is a window to act.  
2. **Operational gap** — Data is usually already there; what’s missing is **usable risk scores** and **thresholds** that match retention economics.

### Layout
- Hook text box height **`1.5" → 2.45"`**, vertical step **`cy += 1.65 → += 2.58`** so four paragraphs don’t clip.  
- Font **`18 → 17 pt`**, line spacing **`1.15 → 1.12`** so section A still clears the wine “stakes” line and the three chips within the same row.

The edit is in ```139:148:d:\Masters\NCSU\Second Semester\ECE542\Telco_Customer_Churn\_build_poster_v9.py```.

Regenerate with `py -3 _build_poster_v9.py`. If you see **Permission denied** on `poster_v9.pptx`, close it in PowerPoint (or another app) and run the script again.

---

**User**

You know what, i have made some changes manually on v9, retain those changes and add this new motivation points there

---

**Cursor**

Updating the build script to load your edited `poster_v9.pptx` and only refresh section A (motivation), preserving the rest of the slide. Reading the full script to implement this.



Refactoring the script so we load your existing `poster_v9.pptx`, remove only column A (motivation), and rebuild section A with the expanded hook—preserving manual edits elsewhere. Default: merge mode; full rebuild only when `POSTER_V9_FULL_REBUILD=1`.



Implementing merge mode: restructuring the file's opening and wrapping sections B–References in `if not merge_a_only:`.



Here’s what was implemented.

### `poster_v9` is now **merge-by-default**
- If **`poster_v9.pptx` exists** and you do **not** set `POSTER_V9_FULL_REBUILD`, the script:
  1. Opens your current `poster_v9.pptx` (keeps your edits in **B–G**, header, etc.).
  2. Clears **only column A, row 1** (Motivation): anything whose **center** lies in that panel, **plus** any shape named `__V9A__*`.
  3. Rebuilds **A** with the full hook (4 sentences), stakes, “Why standard ML…”, and the three chips, and **names** those shapes `__V9A__panel`, `__V9A__hdr`, `__V9A__hook`, … so the next run can remove them cleanly.

### Full rebuild (optional)
- **`POSTER_V9_FULL_REBUILD=1`** (or `true` / `yes` / `on`): copies **`poster_v3.pptx`** → **`poster_v9.pptx`**, wipes non-`KEEP` shapes, patches **NNDL.39**, rebuilds **the entire poster** (same as before).

### Note about edits **inside A**
- Anything you drew **only** in columns **B–G** is preserved in merge mode.
- **Motivation (A)** is **always** replaced on a normal run, so the script can inject the new text. If you need a one-off that **doesn’t** touch A, don’t run this script or we can add a third mode.

### How to run
```text
py -3 _build_poster_v9.py
```
You should see: `Wrote poster_v9.pptx (section A only — kept your manual edits)` when merge mode is used.

Close `poster_v9.pptx` in PowerPoint if you get a permission error when saving.

---

**User**

I have made few more changes manually, please keep them intact plisss. 

Everything is perfect except the Section F picture which is not visible at all. it should be much larger. Can you alter the section dimensions, contents of the remaining sections to accomodate this section plis? please make this section bigger, as in just the picture, it is okay to have different sections with different dimensions. the idea is to make every section look great. not all of them have to be symmetric.

can you please make that change and create a new poster_v10? dont change poster_v9 now. but try to build on poster_v9 for v10

---

**Cursor**

Creating `_build_poster_v10.py` from the v9 layout, enlarging Section F's image and adjusting the row3 split. Reading the v9 script for layout and Section F.



Creating `_build_poster_v10.py`: copy `poster_v9.pptx` → `poster_v10.pptx`, remove only the bottom band (row 3 + references), and rebuild F (much larger image), G, and REF with asymmetric widths and a taller row 3. Slightly shrinking row 2 to gain vertical space.



Here’s what was added and how it behaves.

### New file: `_build_poster_v10.py`
- **Does not change** `poster_v9.pptx` or `_build_poster_v9.py`.
- Copies **`poster_v9.pptx` → `poster_v10.pptx`**, then **only clears the bottom band** (anything whose **center** is at or below **row 3**, ~y ≥ 28.15″).
- **Leaves rows 1–2 alone** (Motivation through **E**), including your manual tweaks there.

### Layout changes in v10
| Piece | Change |
|--------|--------|
| **Row 2 height** | **11.80 → 11.38″** (frees a bit of vertical space). |
| **Row 3** | Starts at **28.23″**, height **6.58″** (was **5.60″**) so the bottom row is taller. |
| **F vs G width** | **Asymmetric:** **F ≈ 26.9″**, **G ≈ 19.9″** (was ~23.4″ each). |
| **Section F figure** | Plot box **~70%** of the content width (was **46%**), using almost the full content height under the header (`fi_max_h` ~**6.2″**). |

References strip is tightened slightly (`REF_H` computed from the bottom margin) so everything still fits on a **36″** slide.

### Trade-off (important)
Redoing **F / G / References** from the script **replaces any hand edits** you had only in those areas. **A–E** stay as in your `poster_v9.pptx`.

### Command
```bash
py -3 _build_poster_v10.py
```
Output: **`poster_v10.pptx`** (already generated successfully in your project folder).

If you want **G** or **references** to stay exactly as in v9 while only **F** is rebuilt, say so and we can switch the script to a stricter “F-only” delete box (with possible small alignment quirks for **G**).

---

**User**

Okay Now, give me content/ script to prepare for symposium tomorrow

---

**Cursor**

Here’s a tight symposium prep pack you can use as-is or trim onto a notecard.

---

## 30-second version (poster beside you)

“I looked at **IBM Telco churn** with the usual ML stack but focused on what carriers actually care about: **imbalanced labels**, **asymmetric costs**—missing a churner is far worse than a false alarm—and **thresholds**, because 0.5 is arbitrary here. I compared **logistic regression, a small MLP, CatBoost, and XGBoost** with one pipeline: stratified splits, train-only scaling, **threshold tuned on validation**. **CatBoost** came out strongest on **F1, ROC-AUC, and especially calibration** via **Brier**. Under a simple **cost model**, **threshold tuning** drove almost all the dollar lift—models clustered near **~$370K net value per thousand customers**. **SHAP-style importance** lines up with intuition—**tenure, contract, fiber, payment method**. Takeaway: **good probabilities plus the right threshold beat chasing marginal gains from architecture alone.**”

---

## ~2-minute script (walk the poster)

**A – Motivation**  
“Churn is expensive; retention beats acquisition. Standard accuracy ignores imbalance and business costs, so we frame this as **ranking plus decisions**, not just classification.”

**B – Data**  
“**~7K customers**, cleaned features, **~27% churn**—clear imbalance. EDA shows **contract and tenure** patterns that match what we’d expect.”

**C – Method**  
“One **shared pipeline**: stratified split, **scaler fit on train only**, four models, then **threshold on validation**—max F1 here, but we also care about **calibration** for downstream costs.”

**D – Results**  
“**CatBoost** leads on **F1 and Brier**; **MLP doesn’t beat logistic regression** on this small one-hot tabular setup—most signal is already near-linear. **ROC/PR** supports that story.”

**E – Cost-aware**  
“We sweep **thresholds** with illustrative **FN vs FP** costs. **Net value** is similar across models once the threshold is tuned—the important lever is **where you cut**, not only which algorithm wins on accuracy.”

**F – Drivers**  
“**Feature importance**—**tenure, contract type, fiber, charges, electronic check**—matches industry narratives and suggests **targeted retention**, e.g. contract upsell.”

**G – Close**  
“**Deploy**: save model, scaler, threshold; **recalibrate** on a schedule. **Limits**: static snapshot, illustrative costs. **Next**: ensembles, cost-sensitive training, **live A/B** on thresholds.”

Pause after **one** number block (e.g. CatBoost F1 **0.624**, Brier **0.139**, or **~$370K / 1K**) so it sticks.

---

## Numbers worth memorizing (pick 3–4)

| Item | Value |
|------|--------|
| Dataset size | **7,032** customers (after clean); churn **~26.6%** |
| Best model | **CatBoost** — F1 **~0.624**, ROC-AUC **~0.841**, Brier **~0.139** (from your table) |
| Cost narrative | **~$370K** net value / **1,000** customers (order of magnitude; say “illustrative costs”) |
| MLP vs LR | MLP **does not beat** LR on this tabular setup |
| Drivers | **Tenure**, **contract**, **fiber**, **electronic check** (top of your list) |

---

## Likely Q&A (short answers)

**Why CatBoost?**  
“Strong ranking **and** calibrated probabilities on mixed/categorical-heavy tabular data; lowest **Brier** in our comparison.”

**Why didn’t the neural net win?**  
“Small tabular data, heavy **one-hot** encoding—a **linear decision boundary** captures most of it; deeper nets don’t help much without more data or better inductive bias.”

**Is ~$370K real money?**  
“It’s **scenario math**: illustrative **FN/FP** costs and **threshold** choices. The point is **relative** model behavior and **where** to operate the classifier, not a guaranteed revenue claim.”

**What would you deploy?**  
“**CatBoost** + **saved threshold** + **scaler**; **monthly scoring**, **quarterly recalibration**; monitor **drift**.”

**Biggest limitation?**  
“**Cross-sectional** data—no true time series; **costs vary** by segment; we’d validate in **A/B**.”

**Ethics / fairness?**  
“We didn’t stratify by protected attributes; in production you’d **audit** outcomes across segments and **review** intervention design.”

---

## The night before (15 minutes)

1. Say the **30-second** and **2-minute** versions **out loud** once each.  
2. Re-read **one** figure caption (cost curve or ROC/PR) so you can point to the axis labels.  
3. Sleep > cramming numbers.

If you tell me your slot length (e.g. 3 min vs poster-only), I can trim this to a single timed script.

---

**User**

It is all good that you are giving all these jargon like 
imbalanced labels, 
asymmetric costs 
thresholds  
because 0.5 is arbitrary here

logistic regression, a small MLP, CatBoost, and XGBoost, 
threshold tuned on validation 
F1, ROC-AUC, and especially calibration via Brier
$370K net value per thousand customers

 SHAP-style importance


But i dont know shit about all these, can you explain each one of them and connect all the math and dots together. 

---

**Cursor**

Here’s the same story **without** assuming you already know the vocabulary. You can use this to learn the ideas first, then map words like “Brier” and “CatBoost” onto them.

---

## 1. What the model is even doing

- Each **row** = one customer, **features** = things you know (contract, monthly bill, tenure, etc.), **label** = did they churn (yes/no).
- The model outputs a **score between 0 and 1**: “estimated probability this person churns.”
- A **classifier** turns that into yes/no by drawing a **line**: “if score ≥ **t**, predict churn.” That number **t** is the **threshold** (often wrongly fixed at **0.5**).

So: **probability** → **threshold** → **predict churn or not**.

---

## 2. “Imbalanced labels”

- If **73%** stayed and **27%** churned, the data are **imbalanced**: one outcome is rare-ish but important.
- A dumb rule “always predict *stay*” can get **~73% accuracy** and still **never catch a churner**. **Accuracy** counts all mistakes equally, so it hides that failure.
- So people use metrics that care about **the minority class** (churn) and about **errors that matter**, not raw “percent correct.”

**Dot:** imbalance → accuracy misleads → you need better metrics and a sensible threshold.

---

## 3. “Asymmetric costs”

- **False negative (FN):** you said “stay,” they churned → you **missed** someone to retain (expensive).
- **False positive (FP):** you said “churn,” they stayed → maybe an extra call or offer (usually cheaper).
- **Asymmetric** means: **FN and FP are not equally bad** for the business. Your poster uses rough numbers like **big cost per missed churn** vs **small cost per unnecessary alert**.
- Math idea: you’re not minimizing “number of mistakes”; you’re closer to minimizing **expected dollars** (or some weighted loss).

**Dot:** costs → the **best threshold** is usually **not** 0.5 even if the model is good.

---

## 4. Thresholds — why “0.5 is arbitrary”

- **0.5** means: “predict churn if predicted probability ≥ 50%.” That treats **maybe** and **unlikely** symmetrically around half — which has **no special meaning** for your business.
- With **imbalance**, many scores might sit below 0.5 even for risky people, or the opposite — depends on the model.
- With **asymmetric costs**, you might want to **flag more people** (lower threshold → more “churn” predictions) so you **miss fewer** real churners, at the cost of more false alarms.

**Dot:** **tuning the threshold** (often on a **validation** set you didn’t train on) is how you align the model with **costs** and **imbalance**.

---

## 5. The four models in one sentence each

- **Logistic regression:** weighted sum of features + sigmoid → probability. **Linear** boundary in feature space. Simple, interpretable, strong baseline on tabular data.
- **Small MLP (neural net):** stacks of numbers + nonlinearities; can learn **curved** boundaries. On **small, one-hot** tabular data it often doesn’t beat logistic regression much.
- **CatBoost / XGBoost:** **tree ensembles** — many decision trees combined; handle nonlinearities and feature interactions well; often strong on tabular data.

**Dot:** same data, same preprocessing → you’re asking **which shape of decision boundary** fits this dataset best.

---

## 6. “Threshold tuned on validation”

- **Train:** model learns parameters.
- **Validation:** holdout data used to pick **hyperparameters** and **threshold** without peeking at the final **test** set.
- You pick **t** (e.g. maximize **F1** on validation) so the operating point is chosen **honestly**, not by staring at test scores.

**Dot:** train → tune **t** on val → **then** report numbers on test.

---

## 7. F1, ROC-AUC, Brier — what they measure

Think of three questions:

| Metric | Plain question |
|--------|----------------|
| **F1** | At **one** chosen threshold, balance of **precision** (of those predicted churn, how many really churned?) and **recall** (of all churners, how many did we catch?). Single snapshot; depends on **t**. |
| **ROC-AUC** | Across **all** thresholds: how well does the model **rank** churners above non-churners? **0.5** = random; **1** = perfect ranking. **Does not** require picking one **t**; it’s about **ordering**. |
| **Brier score** | How close predicted probabilities are to **0/1 outcomes** (mean squared error of probabilities). **Lower** = better **calibration** in a probability sense: “when it says 30%, churn happens ~30% of the time” **on average** over many cases. |

**Calibration** (what **Brier** reflects): not just “who’s riskier,” but “are the **numbers** trustworthy as probabilities?”

**Dot:** ROC-AUC ≈ **ranking quality**; Brier ≈ **probability honesty**; F1 ≈ **one operating point** quality.

---

## 8. “~$370K net value per thousand customers”

- You define **value** from confusion matrix at a threshold: true positives/false positives/false negatives × **dollar weights** (illustrative).
- **Sweep** many thresholds; **pick** one that maximizes **net value** on validation (or similar rule).
- **Per 1,000 customers** just scales the arithmetic so the number isn’t tied to full dataset size.

**Dot:** this connects **threshold** + **costs** → **one dollar story**, not a promise of real revenue — it’s **scenario math** to show **why threshold matters**.

---

## 9. “SHAP-style importance”

- **SHAP** (and simpler **feature importance** from trees) answers: **which inputs** push predictions most?
- Your plot lists things like **tenure, contract, fiber, electronic check** — meaning the model leans on those when scoring risk.

**Dot:** metrics say **how good** the model is; importance says **what it’s looking at** — links to **business actions** (contracts, payment method, etc.).

---

## 10. One chain that ties the math together

1. **Labels imbalanced** → don’t trust accuracy alone.  
2. **Costs asymmetric** → **wrong threshold** wastes money even with a good ranker.  
3. **Tune threshold on validation** → pick an operating point that matches **metrics or dollars** you care about.  
4. **ROC-AUC** checks **separation** of churn vs not; **Brier** checks **probabilities**; **F1** checks **one slice** at your threshold.  
5. **Tree models** (e.g. CatBoost) often win on tabular **ranking + calibration** here; **MLP** doesn’t add much on small one-hot data vs **logistic regression**.  
6. **Importance** connects scores to **interpretable levers** (tenure, contract, …).  
7. **$370K / 1K** is the **same threshold–cost story** in money units for the symposium slide.

---

## Tiny glossary (cheat sheet)

| Phrase | Remember as |
|--------|----------------|
| Imbalanced | Rare-ish churn class; accuracy lies. |
| Asymmetric costs | Missing churn ≠ false alarm in dollars. |
| Threshold | Cutoff on probability; 0.5 is just a default. |
| Validation tuning | Choose threshold without cheating on test. |
| F1 | Precision/recall mix at **one** cutoff. |
| ROC-AUC | Ranking quality across cutoffs. |
| Brier | How honest probabilities are (lower better). |
| CatBoost / XGBoost | Strong tabular tree ensembles. |
| SHAP-style importance | Which features drive the score. |

If you want, next step we can walk **one** metric (e.g. F1 or Brier) with a **2×2 confusion table** and fake numbers so it becomes muscle memory for tomorrow.

