import streamlit as st
from constants import (
    profitability_cases,
    growth_cases,
    market_entry_cases,
    particulars_cases,
    pricing_cases,
    unconventional_cases,
)


def sideBarComponent():

    st.sidebar.header("List of Cases")
    st.sidebar.markdown("##")
    st.sidebar.markdown("##")

    with st.sidebar:
        with st.expander("Profitability"):
            for case in profitability_cases:
                st.markdown(case)

        with st.expander("Growth"):
            for case in growth_cases:
                st.markdown(case)

        with st.expander("Market Entry"):
            for case in market_entry_cases:
                st.markdown(case)

        with st.expander("Particulars"):
            for case in particulars_cases:
                st.markdown(case)

        with st.expander("Pricing"):
            for case in pricing_cases:
                st.markdown(case)

        with st.expander("Unconventional"):
            for case in unconventional_cases:
                st.markdown(case)
