import streamlit as st
st.set_page_config(
    page_title="MLP",
    page_icon="—"
)
st.title("Main Page")
st.header('Gregor Mendel',divider=True)
st.sidebar.sucess('Pages Above')
with st.sidebar:
    st.page_link("pages/data.py",label="Home",icon="🏠")
