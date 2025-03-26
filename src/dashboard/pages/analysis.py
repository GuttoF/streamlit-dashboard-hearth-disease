import plotly.express as px  # type: ignore
import streamlit as st

from dashboard.components.plots import plot_correlation_matrix


def render(df) -> None:
    st.header("Detailed Analysis")

    st.subheader("Feature Relationships")
    plot_correlation_matrix(df)

    st.subheader("Interactive Explorer")
    x_axis = st.selectbox(
        "X-axis Feature",
        options=["age", "resting_blood_pressure", "cholesterol", "max_heart_rate"],
    )

    y_axis = st.selectbox(
        "Y-axis Feature",
        options=[
            "cholesterol",
            "resting_blood_pressure",
            "max_heart_rate",
            "st_depression",
        ],
    )

    fig = px.scatter(df, x=x_axis, y=y_axis, color="heart_disease", trendline="lowess")
    st.plotly_chart(fig, use_container_width=True)
