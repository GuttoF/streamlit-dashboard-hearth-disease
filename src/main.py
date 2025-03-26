import pandas as pd
import streamlit as st

from dashboard.components.filters import create_filters
from dashboard.components.plots import (
    create_age_distribution,
    create_boxplot,
    create_correlation_heatmap,
    create_gender_pie,
    create_grouped_bar,
    create_scatter_plot,
)

st.set_page_config(
    page_title="Análise de Doenças Cardíacas", page_icon="❤️", layout="wide"
)


@st.cache_data
def load_data() -> pd.DataFrame:
    from dashboard.components.utils import load_processed_data

    return load_processed_data()


def main() -> None:
    st.title("Análise Completa de Doenças Cardíacas")

    df = load_data()
    filtered_df = create_filters(df)

    st.header("Indicadores Principais")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Pacientes", len(filtered_df))
    col2.metric(
        "Com Doença Cardíaca", f"{filtered_df['heart_disease'].mean() * 100:.1f}%"
    )
    col3.metric("Idade Média", f"{filtered_df['age'].mean():.1f} anos")
    col4.metric(
        "Pressão Arterial Média",
        f"{filtered_df['resting_blood_pressure'].mean():.1f} mmHg",
    )

    st.header("Análise Demográfica")
    col1, col2 = st.columns(2)
    with col1:
        create_age_distribution(filtered_df)
    with col2:
        create_gender_pie(filtered_df)

    st.header("Relações Clínicas")
    col1, col2 = st.columns(2)
    with col1:
        create_scatter_plot(filtered_df)
    with col2:
        create_correlation_heatmap(filtered_df)

    st.header("Comparações")
    col1, col2 = st.columns(2)
    with col1:
        create_boxplot(filtered_df)
    with col2:
        create_grouped_bar(filtered_df)

    if st.checkbox("Mostrar dados filtrados"):
        st.dataframe(filtered_df)


if __name__ == "__main__":
    main()
