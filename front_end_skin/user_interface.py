###Libraries
import streamlit as st
from PIL import Image
import requests #pip install requests

###################Page tab###################
st.set_page_config(
    page_title = 'Skin Cancer Prediction',
    page_icon = '🔎',
    layout="centered", # wide
    initial_sidebar_state="collapsed") # collapsed)
##Code to try to change background using CSS
#with st.echo():
#    CSS = """
#    h1 {
#        color: red;
#    }
#    .stApp {
#        background-image: url(https://images.app.goo.gl/EmA51RExsJyJhWAW9);
#        background-size: cover;
#    }
#    """
#    if st.checkbox('Inject CSS'):
#        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

############# Config the title and picture#############
#Custoum stylling
col1, col2 = st.columns(2)
st.markdown(""" <style> .font {
height: 50px;
font-family: 'Quando';
font-style: normal;
font-weight: 400;
font-size: 36px;
letter-spacing: -0.02em;
color: #B69578
} </style> """, unsafe_allow_html=True)
col1.markdown('<p class="font">Skin Cancer Prediction</p>', unsafe_allow_html=True)
#col1 picture
image1 = Image.open('assets/abcde.jpg')
col1.image(image1, use_column_width=True)

#column 2 picture
image = Image.open('assets/Inspection_logo.jpg')
col2.image(image, use_column_width=True)
## trying to change the style of next subheader
#st.markdown(""" <style> .font {
#position: absolute;
#height: 32px;
#font-family: 'Inria Serif';
#font-style: normal;
#font-weight: 200;
#font-size: 16px;
#line-height: 160%;
#color: #603D1E;
#} </style> """, unsafe_allow_html=True)
#st.markdown('<p class="font"> Check your skin using our website and have the **prediction**.</p>', unsafe_allow_html=True)
st.subheader('Check your skin using our website and have the **prediction**.')

####### Disclaimer
st.checkbox("I have read and agree to the **Privacy Policy**")
st.checkbox("I understand that this is a prediction and all the results should be taken into account that they can be wrong")
st.button('Continue')

########################Loading Image related#########
def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
def main():
    st.subheader('Upload your image')
    load_image()

if __name__ == '__main__':
    main()

#########################Side bar###############
st.sidebar.header("Prediction Related Informations")
st.sidebar.radio("**Search between different types of skin lesions**", ['Nevus', 'Basal Carcinoma', 'Other'])

with st.sidebar.expander("Click to read more"):
    st.write(" Basal cell carcinoma (BCC) is the most common form of skin cancer and the most frequently occurring form of all cancers. In the U.S. alone, an estimated 3.6 million cases are diagnosed each year.")
    st.write("These are some **warning** signs you should take into account")
    st.image(Image.open('assets/BCC_image.jpg'))

###############api##############
#params = dict()

#skin_detection_api_url = 'http://127.0.0.1:8000/predict'
#response = requests.get(skin_detection_api_url, params=params)

#(json?html?)prediction = response.json()

#pred = prediction[]
