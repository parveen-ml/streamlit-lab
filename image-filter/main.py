import streamlit as st
import cv2
import numpy as np

st.title("Welcome to image filter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    img_resized = cv2.resize(img, (1080, 720))
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    st.image(img_rgb, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Gray"):
            gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
            st.image(gray, caption="Grayscale", use_container_width=True)
            st.success("Gray filter applied")

    with col2:
        if st.button("Blur"):
            blur = cv2.GaussianBlur(img_resized, (15, 15), 0)
            st.image(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB), caption="Blurred", use_container_width=True)
            st.success("Blur filter applied")

    with col3:
        if st.button("Edge"):
            edges = cv2.Canny(img_resized, 100, 200)
            st.image(edges, caption="Edges", use_container_width=True)
            st.success("Edge filter applied")
