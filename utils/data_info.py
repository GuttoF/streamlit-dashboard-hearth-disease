from typing import Dict, Optional, Union

import numpy as np
import pandas as pd


def analyze_data(  # noqa: C901
    df: pd.DataFrame,
    *,
    columns_info: bool = False,
    dtypes_info: bool = False,
    nan_info: bool = False,
    stats_info: bool = False,
    correlation_info: bool = False,
    outlier_info: bool = False,
    target_analysis: bool = False,
    target_col: Optional[str] = None,
) -> Dict[str, Union[Dict, str]]:
    """
    Analyzes a dataset and provides various insights based on the specified options.

    Parameters:
        df (pd.DataFrame): The dataset to analyze.
        columns_info (bool): Whether to include information about the columns.
        dtypes_info (bool): Whether to include information about data types.
        nan_info (bool): Whether to include information about missing values.
        stats_info (bool): Whether to include statistical summaries.
        correlation_info (bool): Whether to include correlation analysis.
        outlier_info (bool): Whether to include outlier detection.
        target_analysis (bool): Whether to include analysis of a target column.
        target_col (Optional[str]): The name of the target column for analysis.

    Returns:
        Dict[str, Union[Dict, str]]: A dictionary containing the analysis results.
    """
    results = {}
    numeric_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    for analysis in [
        ("columns_info", columns_info),
        ("dtypes_info", dtypes_info),
        ("nan_info", nan_info),
        ("stats_info", stats_info),
        ("correlation_info", correlation_info),
        ("outlier_info", outlier_info),
        ("target_analysis", target_analysis),
    ]:
        analysis_name, should_run = analysis

        match (analysis_name, should_run):
            case ("columns_info", True):
                results["columns_info"] = {
                    "total_columns": len(df.columns),
                    "column_names": list(df.columns),
                }

            case ("dtypes_info", True):
                results["dtypes_info"] = df.dtypes.astype(str).to_dict()

            case ("nan_info", True):
                nan_counts = df.isna().sum()
                nan_percentage = (nan_counts / len(df)) * 100
                results["nan_info"] = {
                    "total_nan": nan_counts.sum(),
                    "nan_by_column": nan_counts[nan_counts > 0].to_dict(),
                    "nan_percentage_by_column": nan_percentage[nan_counts > 0]
                    .round(2)
                    .to_dict(),
                }

            case ("stats_info", True):
                stats = {}
                if not numeric_cols.empty:
                    stats["numerical_stats"] = df[numeric_cols].describe().to_dict()
                if not categorical_cols.empty:
                    stats["categorical_stats"] = (
                        df[categorical_cols].describe().to_dict()
                    )
                results["statistics"] = (
                    stats if stats else "No columns available for statistics"
                )

            case ("correlation_info", True):
                if len(numeric_cols) > 1:
                    corr_matrix = df[numeric_cols].corr()
                    results["correlation"] = {
                        "correlation_matrix": corr_matrix.to_dict(),
                        "top_correlations": get_top_correlations(corr_matrix),
                    }
                else:
                    results["correlation"] = (
                        "Not enough numeric columns for correlation analysis"
                    )

            case ("outlier_info", True):
                if not numeric_cols.empty:
                    results["outliers"] = detect_outliers_iqr(df[numeric_cols])
                else:
                    results["outliers"] = "No numeric columns for outlier detection"

            case ("target_analysis", True):
                target_col = target_col or next(
                    (
                        col
                        for col in ["target", "heart_disease", "class", "outcome"]
                        if col in df.columns
                    ),
                    None,
                )

                if target_col and target_col in df.columns:
                    target_counts = df[target_col].value_counts()
                    analysis_result = {
                        "count": target_counts.to_dict(),
                        "percentage": (target_counts / len(df) * 100)
                        .round(2)
                        .to_dict(),
                        "class_balance": (
                            "balanced"
                            if abs(target_counts[0] - target_counts[1]) < 0.1 * len(df)
                            else "imbalanced"
                        ),
                    }

                    if len(target_counts) == 2 and not numeric_cols.empty:
                        analysis_result["mean_values_by_class"] = (
                            df.groupby(target_col)[numeric_cols].mean().to_dict()
                        )

                    results["target_analysis"] = analysis_result
                else:
                    col_msg = f"'{target_col}'" if target_col else "not specified"
                    results["target_analysis"] = (
                        f"Target column {col_msg} not found in dataset"
                    )

    return results


def get_top_correlations(corr_matrix: pd.DataFrame, n: int = 5) -> Dict:
    """Retorna as top n correlações do dataframe usando match case"""
    match corr_matrix:
        case pd.DataFrame() if len(corr_matrix) > 1:
            corr_abs = corr_matrix.abs()
            upper = corr_abs.where(
                np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
            )
            top_pairs = upper.stack().sort_values(ascending=False).head(n)  # type: ignore
            return top_pairs.to_dict()
        case _:
            return {}


def detect_outliers_iqr(df: pd.DataFrame) -> Dict[str, Dict]:
    """Detecta outliers usando match case"""
    outliers = {}

    for col in df.columns:
        match df[col].dtype:
            case np.number:
                q1, q3 = df[col].quantile([0.25, 0.75])
                iqr = q3 - q1
                bounds = {"lower_bound": q1 - 1.5 * iqr, "upper_bound": q3 + 1.5 * iqr}

                col_outliers = df[
                    (df[col] < bounds["lower_bound"])
                    | (df[col] > bounds["upper_bound"])
                ]

                outliers[col] = {
                    **bounds,
                    "num_outliers": len(col_outliers),
                    "outlier_percentage": (len(col_outliers) / len(df)) * 100,
                }
            case _:
                continue

    return outliers
