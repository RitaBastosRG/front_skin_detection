###Libraries
import streamlit as st
from PIL import Image
import requests #pip install requests
from io import BytesIO
import time

###################Page tab###################
st.set_page_config(
    page_title = 'Skinscancer',
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
check1 = st.checkbox("I consent to upload my image and agree to the **Privacy Policy**")
check2 = st.checkbox("I understand that this is a prediction and all the results should be taken into account that they can be wrong")

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
if st.sidebar.checkbox('Show creators'):
    image_size = 50

    TEACHERS = {
        'Haitao' : 'https://images.unsplash.com/photo-1534254910684-68bdc1d69cf7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
        'Ines' : 'https://images.unsplash.com/photo-1534254910684-68bdc1d69cf7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
        'Yui' : 'https://images.unsplash.com/photo-1534254910684-68bdc1d69cf7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
        'Rita' : 'https://lh3.googleusercontent.com/pw/AJFCJaWoe3AVsk9WImvGxO7Dd_ZwUnEtcnIgCdwGPFwjlZBy3rxLoj0zc6nbC12wYePTEY-Uj5xugu0xilP2W_cGU4ZZa2H_OdPCLpkGYcppQmxWoWHcq7VRkNTlKw69hoXrEvtyXn50tRtHevpHn5wLWo1delp0DETHoZ4qh1hWFXZkDxk0l3z2wcUlmWQFKTmtZawG-az3lMHfdkhxtZKzQk4ogd_s1uC_yw9naW0uzMRt4BciNE6fsPyrzW2EGmksgi-M-X6xYyRdPnEnhIj6Ps4b3rez8wDn0dxjAMcaQSqKFY-6JhX146QM2KOfSJ-UyafgNs_wbCpM-GDzizo8vaRBNLjaM1af69mBA1jvecwFCZEYpWzgQ7miuIfAz_gmKEdqF9qNUjoMrv8MSujMIcQ85HuHUgDZ44zelQWvfWo7cNfFErSdY49TC2_G7gx8gW18Xs2AzS_33POZqmkj4c2K5w410qC_OIaJd6ikAZLc-H88w4P_wZWpfrCnZ9jdc_vQ-2gT98MyVAeGx57VeevxSqFRdslhdN9EwLr44QvCxWgjbamt9SmE3oSyrMl6tscAJowNsSya6X6cO7DxfXATEe--vGX7RZaJsHFzZODEwMg0_CmZhACLjio2zAPolTjTM0DP1a6rXmxBU0n2RY7aWKjbkjO8Mry5SDwXQ_iGLWc5yU6bOpLMz1XHjjakzoPdGHbU5_Smhv3ejGe8_-wdFtZ3PpzOSS-R9oT-jFw4S7TocQOmACvfhpPPrCw0zYJl0sAbfExS8JE7PHWlPjJXPhbYjxd9WofnbD3HVNKDsaWq2r6s2-TE87EinhGUvAOvmL24lcLBjwnURFMCqLGJc4xhuinPE0F22ZUYQx8i3Qb0EvdA-1cekpvTC_iHZSs-g__b7Ig3H_tgmixaXemy8PeH1P7cE_LKa2bpL7ibzMeKnszoKhEYAfAfjpC7Kmrf7X-TMd325D93lSnupxMeNCcnJDmWHzSzNZFeMX-vpX40x0tO_2k4pARI7171wuNab5x7pwPBA6TahN8OWLkz853hlnT1Xpy-O8EysKz43US2lcC1RK93DFW6FZaEF5Ar1IRmkJersC7CTu6ysIIsQQYBIW9je8Urs56bhJdnew=w710-h947-s-no?authuser=0',
    }

    TEACHER_CSS = f"""
    #teachers {{
        display: flex;
        flex-wrap: wrap;
    }}

    .teacher-card {{
        display: flex;
        flex-direction: column;
    }}

    .teacher-card img {{
        width: {image_size}px;
        height: {image_size}px;
        border-radius: 100%;
        padding: 4px;
        margin: 10px;
        box-shadow: 0 0 4px #eee;
    }}

    .teacher-card span {{
        text-align: center;
    }}
    """

    # streamlit html injection seems to sensitive to new lines...
    # remove that \ and the html gets displayed instead of being interpreted
    TEACHER_CARD = """\
        <div class="teacher-card">
            <img src="{url}">
            <span>{name}</span>
        </div>
    """

    teachers = ''.join([TEACHER_CARD.format(name=f'{name.split()[0]}', url=url) for name, url in TEACHERS.items()])

    TEACHER_HTML = f"""
    <style>
    {TEACHER_CSS}
    </style>
    <div id="teachers">
        {teachers}
    </div>
    """

    st.sidebar.write(TEACHER_HTML, unsafe_allow_html=True)
###############api#####################
if uploaded_file is not None:
    skin_detection_api_url = 'https://skin-detection-hsuizqzdtq-ew.a.run.app/upload-image'
    files = {'file': BytesIO(image_data)}
    response = requests.post(skin_detection_api_url, files=files)
    prediction = response.json()
    pred = prediction['possibility']
    if st.header(f'The probability of being malignant is round({pred})%'):
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
        st.success('This is a success!')
