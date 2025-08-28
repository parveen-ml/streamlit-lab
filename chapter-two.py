import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your Chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your Chai")

tea_type = st.radio("Pick your Chai base: ",["Water", "Milk", "Almond Milk"])
st.write(f"Selected base {tea_type}")

flavour = st.selectbox("Choose flavour: ",["Adrak", "Kesar", "Tulsi"])
st.write(f"Selected: {flavour}")

sugar = st.slider("Sugar level (spoon)", 0,5,2)
st.write(f"Selected sugar level: {sugar}")

cups = st.number_input("How many cups: ", min_value=1, max_value=10, step=1)
st.write(f"Selected cups number: {cups}")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Welcome {name} ! Your Chai is on the way")

order_date = st.date_input("Select your order date: ")
st.write(f"Your order date is: {order_date}")