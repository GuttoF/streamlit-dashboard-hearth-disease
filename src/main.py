import streamlit as st
from typing import Any
from dashboard.components.filters import setup_sidebar_filters
from dashboard.pages import analysis, data, overview

st.set_page_config(
    page_title="Heart Disease Analytics Pro",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data() -> Any:
    from dashboard.components.utils import load_processed_data

    return load_processed_data()


def main():
    df = load_data()
    filtered_df = setup_sidebar_filters(df)

    page = st.sidebar.radio(
        "Navigation", ["Overview", "Analysis", "Data Explorer"], index=0
    )

    if page == "Overview":
        overview.render(filtered_df)
    elif page == "Analysis":
        analysis.render(filtered_df)
    else:
        data.render(filtered_df)


if __name__ == "__main__":
    main()
