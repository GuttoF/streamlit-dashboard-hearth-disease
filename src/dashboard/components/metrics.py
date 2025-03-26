import streamlit as st


def display_key_metrics(df) -> None:
    cols = st.columns(4)

    metrics = [
        ("Total Patients", len(df)),
        ("Heart Disease %", f"{df['heart_disease'].mean() * 100:.1f}%"),
        ("Avg Age", f"{df['age'].mean():.1f} years"),
        ("Avg Cholesterol", f"{df['cholesterol'].mean():.1f} mg/dL"),
    ]

    for col, (label, value) in zip(cols, metrics):
        col.metric(label, value)
