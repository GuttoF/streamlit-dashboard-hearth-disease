import streamlit as st
from typing import Any

def setup_sidebar_filters(df) -> Any:
    st.sidebar.header("Filters")

    age_range = st.sidebar.slider(
        "Age Range",
        min_value=int(df["age"].min()),
        max_value=int(df["age"].max()),
        value=(30, 70),
    )

    filtered_df = df[df["age"].between(*age_range)]

    if st.sidebar.checkbox("Advanced Filters"):
        filtered_df = apply_advanced_filters(filtered_df)

    return filtered_df


def apply_advanced_filters(df):
    col1, col2 = st.sidebar.columns(2)

    with col1:
        chest_pain = st.multiselect(
            "Chest Pain Types",
            options=df["chest_pain_type"].unique(),
            default=df["chest_pain_type"].unique(),
        )

    with col2:
        thal = st.multiselect(
            "Thalassemia Types",
            options=df["thalassemia"].unique(),
            default=df["thalassemia"].unique(),
        )

    return df[df["chest_pain_type"].isin(chest_pain) & df["thalassemia"].isin(thal)]
