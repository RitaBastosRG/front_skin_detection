import streamlit as st
from PIL import Image
import base64
import numpy as np
import pandas as pd

#Page tab
st.set_page_config(
    page_title = 'Skin Cancer Prediction',
    page_icon = '🔎')
##### Config the theme
#Custoum stylling

page_bg_img = """ <style>
[data-testid="stAppViewContainer"] {background-image: url('RitaBastosRG/front_end_skin/assets/background.jpg')
background-repeat: no-repeat;
background-size: cover;}
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

##############################

#Title and subtitle
st.markdown(""" <style> .font {
font-size:64px; font-weight: 400; font-family: 'Newsreader'; font-style: normal; color: #866B0C;}
</style> """, unsafe_allow_html=True)

st.markdown('<p class="font">Skin Cancer Prediction</p>', unsafe_allow_html=True)
st.markdown("""Check the health of your skin using our website and have the **prediction**.""")

##################################

#Side bar
st.sidebar.header("Prediction Related Informations")
st.sidebar.multiselect('Search between different types of spots', ['Nevus', 'Basal Carcinoma'])
######################################

#Image
image = Image.open('Inspection_logo_2.jpg')
st.image(image, use_column_width=True)
###############################

#Loading Image related
def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)

def main():
    st.header('Upload your image')
    load_image()

# Resize the image
#resized_image = image_data.resize(size)
# Display the resized image
#st.subheader("Resized Image")
#st.image(resized_image, caption="Resized Image")

####### Disclaimer
st.checkbox("I have read and agree to the **Privacy Policy**")
st.checkbox("I understand that this is a prediction and all the results should be taken into account that they can be wrong")
st.button('Continue')


if __name__ == '__main__':
    main()
