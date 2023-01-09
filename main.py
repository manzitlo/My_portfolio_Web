import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=448)

with col2:
    st.title("Wenzhe Luo")
    st.subheader("github: https://github.com/manzitlo")
    content = """Welcome to my portfolio web...
    My name is Wenzhe Luo."""
    st.info(content)

st.write("""
The following link could tell you what I learned in these few months.

*Feel free to contact me!*
""")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])