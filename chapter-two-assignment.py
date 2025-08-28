import streamlit as st
import datetime

st.title("Age Calcutor")
today_date = datetime.date.today()
user_dob = st.date_input("Select your date of birth", max_value=today_date)

st.write(f"todays date is: {today_date}")

user_age = today_date.year - user_dob.year
months = today_date.month - user_dob.month
st.write(f"Your age is {user_age} year and {months} month")