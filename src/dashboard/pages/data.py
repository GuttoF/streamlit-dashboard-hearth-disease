import streamlit as st

from dashboard.components.utils import load_interim_data


def render(data) -> None:
    st.header("Data Explorer")

    if st.checkbox("Show interim data"):
        interim_data = load_interim_data()
        st.dataframe(interim_data)

    st.subheader("Processed Data")
    st.dataframe(data)

    if st.button("Generate Statistical Summary"):
        st.write(data.describe())
