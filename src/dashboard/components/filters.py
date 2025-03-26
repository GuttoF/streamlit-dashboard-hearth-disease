from typing import Any

import streamlit as st


def create_filters(df) -> Any:
    st.sidebar.header("Filtros")

    idade_min, idade_max = st.sidebar.slider(
        "Faixa etária",
        min_value=int(df["age"].min()),
        max_value=int(df["age"].max()),
        value=(30, 70),
    )

    sexo = st.sidebar.multiselect(
        "Sexo", options=df["sexo"].unique(), default=df["sexo"].unique()
    )

    tipo_dor = st.sidebar.multiselect(
        "Tipo de dor no peito",
        options=df["tipo_dor_peito"].unique(),
        default=df["tipo_dor_peito"].unique(),
    )

    return df[
        (df["age"].between(idade_min, idade_max))
        & (df["sexo"].isin(sexo))
        & (df["tipo_dor_peito"].isin(tipo_dor))
    ]
