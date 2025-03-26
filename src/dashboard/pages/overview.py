import streamlit as st

from dashboard.components.metrics import display_key_metrics
from dashboard.components.plots import plot_age_distribution, plot_risk_factors


def render(data) -> None:
    st.header("Overview Dashboard")
    display_key_metrics(data)

    col1, col2 = st.columns(2)
    with col1:
        plot_age_distribution(data)
    with col2:
        plot_risk_factors(data)
