"""Business cost analysis for Telco churn models."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SEED = 42
np.random.seed(SEED)
FIG_DIR = "figures"


def expected_cost(y_true, y_proba, threshold, c_fn=1500, c_fp=50):
    """Expected cost per customer at the given classification threshold."""
    y_pred = (y_proba >= threshold).astype(int)
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    return (fn * c_fn + fp * c_fp) / len(y_true)


def _constrained_best(y_proba, thresholds, costs, max_flag_rate=0.20):
    """Return (threshold, flag_rate, cost) minimising cost with flag rate ≤ max_flag_rate.

    Among all thresholds where flag_rate ≤ max_flag_rate, picks the one with
    lowest expected cost (equivalently, the lowest valid threshold because cost
    is monotonically non-increasing as the threshold drops).
    Returns (None, None, None) if no threshold satisfies the constraint.
    """
    best_cost = float("inf")
    best_t = best_rate = None
    for t, c in zip(thresholds, costs):
        rate = float((y_proba >= t).mean())
        if rate <= max_flag_rate and c < best_cost:
            best_cost = c
            best_t = float(t)
            best_rate = rate
    return (best_t, best_rate, best_cost) if best_t is not None else (None, None, None)


if __name__ == "__main__":
    os.makedirs(FIG_DIR, exist_ok=True)

    # Load test predictions saved by the boosted notebook
    pred_df = pd.read_csv(f"{FIG_DIR}/test_predictions.csv")
    y_true = pred_df["y_true"].values

    models = {
        "Logistic Regression": pred_df["lr_proba"].values,
        "CatBoost": pred_df["catboost_proba"].values,
        "XGBoost": pred_df["xgboost_proba"].values,
    }

    nn_pred_path = f"{FIG_DIR}/nn_test_predictions.csv"
    if os.path.exists(nn_pred_path):
        nn_df = pd.read_csv(nn_pred_path)
        models["MLP"] = nn_df["mlp_proba"].values

    # Baseline: predict nobody churns (threshold → 1.0), all churners are FN
    baseline_cost = float(y_true.mean()) * 1500  # c_fn=1500, zero FP

    thresholds = np.arange(0.01, 1.0, 0.01)
    max_flag_rate = 0.20

    # First pass: compute costs and collect results for every model
    model_order = ["Logistic Regression", "MLP", "CatBoost", "XGBoost"]
    all_costs = {}
    results = []

    for model_name in model_order:
        if model_name not in models:
            continue
        y_proba = models[model_name]
        costs = [expected_cost(y_true, y_proba, t) for t in thresholds]
        all_costs[model_name] = costs

        # Unconstrained optimum
        opt_idx = int(np.argmin(costs))
        opt_threshold = float(thresholds[opt_idx])
        opt_cost = float(costs[opt_idx])
        net_value = (baseline_cost - opt_cost) * 1000

        # Constrained optimum (flag rate ≤ max_flag_rate)
        c_t, c_rate, c_cost = _constrained_best(y_proba, thresholds, costs, max_flag_rate)
        c_net = round((baseline_cost - c_cost) * 1000, 2) if c_t is not None else None

        results.append({
            "model": model_name,
            "optimal_threshold": round(opt_threshold, 2),
            "expected_cost_per_customer": round(opt_cost, 2),
            "net_value_per_1000_customers": round(net_value, 2),
            "constrained_threshold": round(c_t, 2) if c_t is not None else None,
            "constrained_flag_rate": round(c_rate, 4) if c_rate is not None else None,
            "constrained_net_value_per_1000": c_net,
        })

    # Identify best constrained model (highest constrained net value)
    valid_constrained = [r for r in results if r["constrained_net_value_per_1000"] is not None]
    best_constrained = max(valid_constrained, key=lambda r: r["constrained_net_value_per_1000"])

    # Build plot: cost curves + vertical capacity line for best constrained model
    fig, ax = plt.subplots(figsize=(10, 6))
    for model_name in model_order:
        if model_name in all_costs:
            ax.plot(thresholds, all_costs[model_name], label=model_name)

    ax.axhline(baseline_cost, color="gray", linestyle="--", lw=1, label="No-model baseline")
    ax.axvline(
        best_constrained["constrained_threshold"],
        color="black", linestyle="--", lw=1.5,
        label="20% capacity limit",
    )
    ax.set_xlabel("Threshold")
    ax.set_ylabel("Expected Cost per Customer ($)")
    ax.set_title("Expected Cost per Customer vs. Classification Threshold")
    ax.legend()
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/cost_curve.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved -> {FIG_DIR}/cost_curve.png")

    results_df = pd.DataFrame(results)
    results_df.to_csv(f"{FIG_DIR}/business_value.csv", index=False)
    print(f"Saved -> {FIG_DIR}/business_value.csv")
    print(results_df.to_string(index=False))
    print(f"\nBest constrained model: {best_constrained['model']} "
          f"(threshold={best_constrained['constrained_threshold']}, "
          f"flag_rate={best_constrained['constrained_flag_rate']:.1%}, "
          f"net_value=${best_constrained['constrained_net_value_per_1000']:,.2f})")

    # Update all_models_comparison.csv with Optimal_Threshold and Net_Value_per_1000
    comp_path = f"{FIG_DIR}/all_models_comparison.csv"
    if not os.path.exists(comp_path):
        print(f"[skip] {comp_path} not found; run boosted notebook first.")
    else:
        all_df = pd.read_csv(comp_path)

        # Normalize "Logistic Regression (baseline)" → "Logistic Regression" and
        # drop it if a canonical "Logistic Regression" row already exists.
        all_df["model"] = all_df["model"].replace(
            "Logistic Regression (baseline)", "Logistic Regression"
        )
        # Keep the Logistic Regression row that has Brier data (from boosted notebook);
        # drop_duplicates keeps first occurrence, so sort Brier-present rows first.
        all_df = (
            all_df.assign(_has_brier=all_df.get("brier", pd.Series(dtype=float)).notna())
            .sort_values("_has_brier", ascending=False)
            .drop_duplicates(subset=["model"], keep="first")
            .drop(columns=["_has_brier"])
        )
        # Restrict to the four required model rows
        required = ["Logistic Regression", "MLP", "CatBoost", "XGBoost"]
        all_df = all_df[all_df["model"].isin(required)].copy()

        # Drop any columns this script manages (safe re-run idempotency)
        _managed = {"Optimal_Threshold", "Net_Value_per_1000", "optimal_threshold", "net_value_per_1000"}
        all_df = all_df.drop(columns=[c for c in all_df.columns if c in _managed], errors="ignore")

        thresh_map = {r["model"]: r["optimal_threshold"] for r in results}
        netval_map = {r["model"]: r["net_value_per_1000_customers"] for r in results}
        all_df["optimal_threshold"] = all_df["model"].map(thresh_map)
        all_df["net_value_per_1000"] = all_df["model"].map(netval_map)

        col_rename = {
            "accuracy": "Accuracy",
            "precision": "Precision",
            "recall": "Recall",
            "f1": "F1",
            "roc_auc": "ROC_AUC",
            "pr_auc": "PR_AUC",
            "brier": "Brier",
            "optimal_threshold": "Optimal_Threshold",
            "net_value_per_1000": "Net_Value_per_1000",
        }
        all_df = all_df.rename(columns=col_rename)

        desired_cols = [
            "model", "Accuracy", "Precision", "Recall", "F1",
            "ROC_AUC", "PR_AUC", "Brier", "Optimal_Threshold", "Net_Value_per_1000",
        ]
        all_df = all_df[[c for c in desired_cols if c in all_df.columns]]

        row_order = ["Logistic Regression", "MLP", "CatBoost", "XGBoost"]
        all_df["_ord"] = all_df["model"].apply(
            lambda m: row_order.index(m) if m in row_order else 99
        )
        all_df = all_df.sort_values("_ord").drop(columns=["_ord"]).reset_index(drop=True)

        all_df.to_csv(comp_path, index=False)
        print(f"Updated -> {comp_path}")
