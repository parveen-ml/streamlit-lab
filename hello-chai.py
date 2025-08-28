import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")

chai = st.selectbox("Your fav chai: ",["Masala Chai", "Lemon Tea", "Adrak Tea", "Kesar Chai"])

st.write(f"You choose {chai}. Excellent Choice")

st.success("Your chai has been brewed")