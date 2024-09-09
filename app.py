import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.title("Image to Sketch converter")

uploaded_file=st.file_uploader("choose an image...",type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image=np.array(Image.open(uploaded_file))
    grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    invererted=255-grey_image
    blur=cv2.GaussianBlur(invererted,(21,21),0)
    invererted_blur=255-blur
    sketch=cv2.divide(grey_image,invererted_blur,scale=256.0)

    st.image(image,caption='Original Image',use_column_width=True)
    st.image(sketch,caption='Sketch',use_column_width=True)

    result=Image.fromarray(sketch)

    st.download_button(
        label="Download Sketch",
        data=result.tobytes(),
        file_name="sketch.png",
        mime="image/png"
    )