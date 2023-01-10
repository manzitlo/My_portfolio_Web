import streamlit as st
import pandas

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

col1, col2, col3 = st.columns(3)

with col1:
    st.title("Wenzhe Luo")
    st.image("images/photo.png", width=350)
    st.info("""
    The following could tell you what I learned in these few months.

    *Feel free to contact me!*
    """)

with col3:

    st.subheader("github: https://github.com/manzitlo")
    content = """Welcome to my portfolio web...
    My name is Wenzhe Luo."""
    st.info(content)

col4, col5, col6 = st.columns(3)

df = pandas.read_csv("data.csv", sep=";")

with col4:
    for index, row in df[:1].iterrows():
        st.header(f"{index + 1}. {row['title']}")
        st.write(row["description"])
        st.image("images/" + row["image"],width=450)
        st.write(f"[Source Code]({row['url']})")

with col5:
    for index, row in df[1:2].iterrows():
        st.header(f"{index + 1}. {row['title']}")
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source Code]({row['url']})")

with col6:
    for index, row in df[2:].iterrows():
        st.header(f"{index + 1}. {row['title']}")
        st.write(row["description"])
        st.image("images/" + row["image"], width=250)
        st.write(f"[Source Code]({row['url']})")