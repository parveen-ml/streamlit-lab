import streamlit as st

st.title("Hello Programmer")
st.subheader("How are you doing")
st.text("Welcome to the app")
st.write("Choose your fav. programming language")

lang = st.selectbox("Your fav. language: ", ["Python", "Java", "CPP", "JavaScript"])

st.success(f"You choose {lang}. Excellent choice")
