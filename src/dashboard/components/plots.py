import plotly.express as px # type: ignore
import streamlit as st


def plot_age_distribution(df) -> None:
    fig = px.histogram(
        df,
        x="age",
        color="heart_disease",
        nbins=20,
        title="Age Distribution by Heart Disease",
        labels={"age": "Age", "heart_disease": "Heart Disease"},
        barmode="overlay",
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_risk_factors(df) -> None:
    fig = px.box(
        df,
        x="cardiovascular_risk",
        y="cholesterol",
        color="heart_disease",
        title="Cholesterol by Risk Level",
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_correlation_matrix(df) -> None:
    numeric_cols = df.select_dtypes(include=["number"]).columns
    corr = df[numeric_cols].corr()

    fig = px.imshow(corr, text_auto=True, aspect="auto", title="Correlation Matrix")
    st.plotly_chart(fig, use_container_width=True)
