import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/1638280/pexels-photo-1638280.jpeg", width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/229493/pexels-photo-229493.jpeg", width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")

name = st.sidebar.text_input('Enter your name')
tea = st.sidebar.selectbox("Choose your Chai",["Masala", "Adrak", "Kesar"])

st.write(f"Welcome {name} and {tea} chai is getting ready")

with st.expander("Show Chai making instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot tea
             """)
    
st.markdown('### Welcome to Chai app')
st.markdown('>Blockquote')
