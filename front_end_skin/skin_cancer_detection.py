###Libraries
import streamlit as st
from PIL import Image
import requests #pip install requests
from io import BytesIO
import time

###################Page tab###################
st.set_page_config(
    page_title = 'SKIN-SCANCER',
    page_icon = '🔎',
    layout="centered", # wide
    initial_sidebar_state="collapsed") # collapsed)

# add gradient background
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://images.unsplash.com/photo-1621799754526-a0d52c49fad5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80");
  background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

############# Config the title and picture#############
#Custoum stylling
col1, col2 = st.columns(2)
st.markdown(""" <style> .font {
height: 50px;
font-family: 'Duru Sans';
font-style: normal;
font-weight: 400;
font-size: 36px;
letter-spacing: -0.02em;
color: #824E1E;
} </style> """, unsafe_allow_html=True)
col1.markdown('<p class="font">🔎 Skinscancer 🔎</p>', unsafe_allow_html=True)
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

################# DISCLAIMER ONLY CONTINUES IF THIS BOX IS CHECKED #################

check1 = st.checkbox("I consent to the [Privacy Policy](https://google.com)")
check2 = st.checkbox("I understand that the prediction can be wrong.")

#if check1 and check2 == True:
#    if st.button('Continue') == True:
#    ########################Loading Image related#########
st.subheader('Upload your image')
uploaded_file = st.file_uploader(label='Pick an image to test')
if uploaded_file is not None:
    image_data = uploaded_file.getvalue()
    st.image(image_data)
#########################Side bar################
st.sidebar.header("This project was made by:")
image_size = 50

CREATORS = {
    'Haitao' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1682322545/jooigdwuvxezp0hwguh1.jpg',
    'Ines' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1682322613/rpdiddalk7eqoeobfawr.jpg',
    'Yui' : 'https://avatars.githubusercontent.com/u/99614473?v=4',
    'Rita' : 'https://avatars.githubusercontent.com/u/130187615?v=4',
}

CREATORS_CSS = f"""
#creators {{
    display: flex;
    flex-wrap: wrap;
}}

.creators-card {{
    display: flex;
    flex-direction: column;
}}

.creators-card img {{
    width: {image_size}px;
    height: {image_size}px;
    border-radius: 100%;
    padding: 4px;
    margin: 10px;
    box-shadow: 0 0 4px #eee;
}}

.creators-card span {{
    text-align: center;
}}
"""

# streamlit html injection seems to sensitive to new lines...
# remove that \ and the html gets displayed instead of being interpreted
CREATORS_CARD = """\
    <div class="creators-card">
        <img src="{url}">
        <span>{name}</span>
    </div>
"""

creators = ''.join([CREATORS_CARD.format(name=f'{name.split()[0]}', url=url) for name, url in CREATORS.items()])

CREATORS_HTML = f"""
<style>
{CREATORS_CSS}
</style>
<div id="creators">
    {creators}
</div>
"""

st.sidebar.write(CREATORS_HTML, unsafe_allow_html=True)
###############api#####################
if uploaded_file is not None:
    skin_detection_api_url = 'https://skin-detection-hsuizqzdtq-ew.a.run.app/upload-image'
    files = {'file': BytesIO(image_data)}
    response = requests.post(skin_detection_api_url, files=files)
    'Starting a long computation...'
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
    '...and now we\'re done!'
    prediction = response.json()
    pred = prediction['possibility']
    st.header(f'The probability of being malignant is round({pred})%')
