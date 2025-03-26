import plotly.express as px  # type: ignore
import streamlit as st

HEALTH_PALETTE = {
    "positive": "#e74c3c",
    "negative": "#3498db",
    "neutral": "#2ecc71",
    "background": "#f8f9fa",
}


def create_age_distribution(df) -> None:
    fig = px.histogram(
        df,
        x="age",
        color="heart_disease",
        nbins=20,
        title="Distribuição de Idade",
        labels={"age": "Idade", "heart_disease": "Doença Cardíaca"},
        barmode="overlay",
        color_discrete_map={
            1: HEALTH_PALETTE["positive"],
            0: HEALTH_PALETTE["negative"],
        },
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        hoverlabel={"bgcolor": HEALTH_PALETTE["background"]},
    )
    st.plotly_chart(fig, use_container_width=True)


def create_gender_pie(df) -> None:
    fig = px.pie(
        df,
        names="sexo",
        title="Distribuição por Sexo",
        color_discrete_sequence=[
            HEALTH_PALETTE["negative"],
            HEALTH_PALETTE["positive"],
        ],
    )
    fig.update_traces(marker={"line": {"color": "#ffffff", "width": 1}})
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)


def create_scatter_plot(df) -> None:
    fig = px.scatter(
        df,
        x="cholesterol",
        y="resting_blood_pressure",
        color="heart_disease",
        trendline="lowess",
        title="Colesterol vs Pressão Arterial",
        labels={
            "cholesterol": "Colesterol (mg/dL)",
            "resting_blood_pressure": "Pressão Arterial (mmHg)",
        },
        color_discrete_map={
            1: HEALTH_PALETTE["positive"],
            0: HEALTH_PALETTE["negative"],
        },
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis={"gridcolor": "#e1e5e9"},
        yaxis={"gridcolor": "#e1e5e9"},
    )
    st.plotly_chart(fig, use_container_width=True)


def create_correlation_heatmap(df) -> None:
    numeric_cols = df.select_dtypes(include=["number"]).columns
    corr = df[numeric_cols].corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlação entre Variáveis",
        color_continuous_scale=[
            "#3498db",
            "#ffffff",
            "#e74c3c",
        ],
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)


def create_boxplot(df) -> None:
    fig = px.box(
        df,
        x="tipo_dor_peito",
        y="max_heart_rate",
        color="heart_disease",
        title="Frequência Cardíaca por Tipo de Dor",
        labels={
            "max_heart_rate": "Frequência Cardíaca Máxima",
            "tipo_dor_peito": "Tipo de Dor",
        },
        color_discrete_map={
            1: HEALTH_PALETTE["positive"],
            0: HEALTH_PALETTE["negative"],
        },
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis={"gridcolor": "#e1e5e9"},
        yaxis={"gridcolor": "#e1e5e9"},
    )
    st.plotly_chart(fig, use_container_width=True)


def create_grouped_bar(df) -> None:
    fig = px.bar(
        df.groupby(["sexo", "heart_disease"]).size().reset_index(name="count"),
        x="sexo",
        y="count",
        color="heart_disease",
        barmode="group",
        title="Prevalência por Sexo",
        labels={"count": "Número de Pacientes", "sexo": "Sexo"},
        color_discrete_map={
            1: HEALTH_PALETTE["positive"],
            0: HEALTH_PALETTE["negative"],
        },
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis={"gridcolor": "#e1e5e9"},
        yaxis={"gridcolor": "#e1e5e9"},
    )
    st.plotly_chart(fig, use_container_width=True)
