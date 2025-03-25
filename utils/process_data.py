from pathlib import Path

import duckdb
import numpy as np
import pandas as pd


def new_features(data) -> pd.DataFrame:
    """
    Enhances the heart disease dataset with derived features.

    Parameters:
    data (DataFrame): Original heart disease dataset

    Returns:
    DataFrame: Enhanced dataset with new features
    """
    column_translation = {
        "age": "age",
        "sex": "sex",
        "cp": "chest_pain_type",
        "trestbps": "resting_blood_pressure",
        "chol": "cholesterol",
        "fbs": "fasting_blood_sugar",
        "restecg": "resting_ecg_results",
        "thalach": "max_heart_rate",
        "exang": "exercise_induced_angina",
        "oldpeak": "st_depression",
        "slope": "st_slope",
        "ca": "major_vessels",
        "thal": "thalassemia",
        "target": "heart_disease",
    }
    data = data.rename(columns=column_translation)

    data["cardiovascular_risk"] = data.apply(
        lambda row: "High"
        if (row["age"] > 50)
        & (row["cholesterol"] > 240)
        & (row["resting_blood_pressure"] > 140)
        else "Moderate"
        if (row["cholesterol"] > 200) | (row["resting_blood_pressure"] > 130)
        else "Low",
        axis=1,
    )

    bins = [20, 40, 60, 80]
    labels = ["20-39", "40-59", "60+"]
    data["age_group"] = pd.cut(data["age"], bins=bins, labels=labels)

    data["cholesterol_status"] = np.where(data["cholesterol"] > 200, "High", "Normal")

    data["blood_pressure_category"] = pd.cut(
        data["resting_blood_pressure"],
        bins=[0, 120, 140, 200],
        labels=["Normal", "Pre-hypertension", "Hypertension"],
    )

    data["heart_rate_difference"] = data["max_heart_rate"] - (220 - data["age"])

    data["bmi"] = data.apply(
        lambda row: (70 + (row["age"] * 0.3)) / (1.7**2), axis=1
    ).round(1)

    data["angina_risk"] = data.apply(
        lambda row: "Yes"
        if (row["exercise_induced_angina"] == 1) & (row["st_depression"] > 1)
        else "No",
        axis=1,
    )

    data["risk_score"] = (
        (data["age"] / 10)
        + (data["cholesterol"] / 100)
        + (data["resting_blood_pressure"] / 10)
        + data["st_depression"]
    ).round(1)

    data["diabetes_status"] = np.where(
        data["fasting_blood_sugar"] > 120, "Potential Diabetes", "Normal"
    )

    data["activity_level"] = pd.cut(
        data["max_heart_rate"],
        bins=[0, 100, 140, 200],
        labels=["Sedentary", "Moderate", "Active"],
    )

    data["gender_risk"] = data["sex"].map({1: "Male (Higher Risk)", 0: "Female"})

    return data


def process_heart_data() -> None:
    """
    Process the heart disease dataset and store the results in the processed database.
    """
    project_dir = Path(__file__).resolve().parents[1]
    interim_path = project_dir / "data" / "interim" / "db.db"
    processed_path = project_dir / "data" / "processed" / "db_processed.db"

    processed_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with duckdb.connect(str(interim_path)) as conn:
            df = conn.execute("SELECT * FROM heart").fetchdf()

        df_processed = new_features(df)

        with duckdb.connect(str(processed_path)) as conn:
            conn.register("df_processed", df_processed)
            conn.execute("CREATE TABLE heart_processed AS SELECT * FROM df_processed")
            print(f"Data stored in: {processed_path}")

    except Exception as e:
        print(f"Error during process: {str(e)}")
        raise


if __name__ == "__main__":
    process_heart_data()
