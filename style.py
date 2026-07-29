import streamlit as st

def apply_global_style():

    st.markdown("""
    <style>

    .block-container{
        max-width:85% !important;
        padding-top:2rem;
        margin-left:auto;
        margin-right:auto;
    }

    </style>
    """, unsafe_allow_html=True)