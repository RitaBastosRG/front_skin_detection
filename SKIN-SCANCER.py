# Libraries
import streamlit as st
from PIL import Image
import requests  # pip install requests
from io import BytesIO
import time

###################Page tab###################
st.set_page_config(
    page_title='SKIN-SCANCER',
    page_icon='🔎',
    layout="centered",  # wide
    initial_sidebar_state="collapsed")  # collapsed)

############# Config the title and picture#############
st.markdown(f"""<p style="color:#BB9301;font-size:50px;text-align:center"><strong>🔎 SKIN-SCANCER 🔎</strong></p>""",
              unsafe_allow_html=True)
st.markdown(f"""<p style="color:#BB9301;font-size:30px;text-align:center"><strong>Is your mole cancerous? Find the probability.</strong></p>""", unsafe_allow_html=True)
# Custoum stylling
col1, col2 = st.columns(2)
# col1 picture
image1 = Image.open('assets/abcde-removebg-preview.png').resize((280, 256))
col1.image(image1, use_column_width=True)
# column 2 picture
image = Image.open('assets/Inspection_logo-removebg.png').resize((280, 256))
col2.image(image, use_column_width=True)

################# DISCLAIMER ONLY CONTINUES IF THIS BOX IS CHECKED #################
st.session_state['check1'] = st.checkbox(
    "I have read and agree to the [Privacy Policy](https://skin-scancer.streamlit.app/Privacy_Policy).", value=st.session_state.get('check1', False))
st.session_state['check2'] = st.checkbox(
    "I understand that the prediction can be wrong.", value=st.session_state.get('check2', False))
if st.button('Continue'):
    st.session_state['continue'] = True


if st.session_state.get('check1', False) and st.session_state.get('check2', False) and st.session_state.get('continue', False):
    ########################Loading Image related#########
    st.markdown(f"""<p style="color:#BB9301;font-size:30px"><strong>Upload your image</strong></p>""",
                unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label='Pick an image to test',type=['png','jpg','jpeg'], label_visibility='hidden')
    # st.session_state['uploaded_file'] = uploaded_file
    if uploaded_file is not None:

        image_data = uploaded_file.getvalue()
        st.image(image_data)
        ############api#######################
        skin_detection_api_url = 'https://skin-detection-hsuizqzdtq-ew.a.run.app/upload-image'
        files = {'file': BytesIO(image_data)}
        response = requests.post(skin_detection_api_url, files=files)

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.markdown(
                f'<p>Predicting...🔎 {i+1}/100</P>', unsafe_allow_html=True)
            bar.progress(i + 1)
            time.sleep(0.03)
        prediction = response.json()
        pred = prediction['possibility']
        st.markdown(f'<p style="color:#634E01;font-size:30px">There is <span style="color:red; font-weight: bold;"><strong>{round(pred*100,2)}%</strong></span> probability that your mole is cancerous.</p>',unsafe_allow_html=True)

        if pred*100>50:
            expander = st.expander("Learn more")
            expander.markdown('<p style="color:#634E01;font-size:17px">Your mole might be one of the following cancers:<br> Actinic Keratosis (AK), Squamous Cell Carcinoma (SCC), Basal Cell Carcinoma (BCC).</p>',unsafe_allow_html=True)
            expander.markdown('<p style="color:#634E01;font-size:17px">It is strongly recommended to consult a dermatologist for further evaluation and advice.</p>',unsafe_allow_html=True)
            expander.markdown('''<html>
                              <style>
                                .header {
                                text-align: center;
                                padding: 32px;
                                }
                                .column {
                                float: left;
                                width: 33%;
                                padding: 10px;
                                }
                                .column img {
                                margin-top: 12px;
                                }
                                .row:after {
                                content: "";
                                display: table;
                                clear: both;
                                }
                                </style>
                                <body>
                                <div class="row">
                                <div class="column">
                                <p style="color:#634E01;text-align:center">AK</p>
                                <img src="https://i.ibb.co/KDBk3gS/ISIC-0024800-180.jpg" style="width:100%">
                                </div>
                                <div class="column">
                                <p style="color:#634E01;text-align:center">SCC</p>
                                <img src="https://i.ibb.co/0hsswyY/ISIC-0024372-90.jpg" style="width:100%">
                                </div>
                                <div class="column">
                                <p style="color:#634E01;text-align:center">BCC</p>
                                <img src="https://i.ibb.co/rvx8zKV/ISIC-0028122.jpg" style="width:100%">
                                </div>
                                </div>
                                </body>
                                </html>
                                ''' ,unsafe_allow_html=True)

        else:
            expander = st.expander("Learn more")
            expander.markdown('<p style="color:#634E01;font-size:17px">Your mole might be one of the following benign moles:<br> Melanocytic nevus (NV), Benign keratosis (BKL), Dermatofibroma (DF), Vascular lesion(VASC).</p>',unsafe_allow_html=True)
            expander.markdown('<p style="color:#634E01;font-size:17px">It is likely that your mole is harmless, but keep an eye on how it develops over time. If it grows larger, it is strongly recommended to consult a dermatologist. </p>',unsafe_allow_html=True)
            expander.markdown('''<html>
                              <style>
                                .header {
                                text-align: center;
                                padding: 32px;
                                }
                                .column {
                                float: left;
                                width: 25%;
                                padding: 10px;
                                }
                                .column img {
                                margin-top: 12px;
                                }
                                .row:after {
                                content: "";
                                display: table;
                                clear: both;
                                }
                                </style>
                                <body>
                                <div class="row">
                                <div class="column">
                                <p style="color:#634E01;text-align:center">NV</p>
                                <img src="https://i.ibb.co/yymG6fk/ISIC-0000001.jpg" style="width:100%">
                                </div>
                                <div class="column">
                                <p style="color:#634E01;text-align:center">BKL</p>
                                <img src="https://i.ibb.co/fSWnLbj/ISIC-0012998.jpg" style="width:100%">
                                </div>
                                <div class="column">
                                <p style="color:#634E01;text-align:center">DF</p>
                                <img src="https://i.ibb.co/1ZpD2dR/ISIC-0069303.jpg" style="width:100%">
                                </div>
                                <div class="column">
                                <p style="color:#634E01;text-align:center">VASC</p>
                                <img src="https://i.ibb.co/0t3zZ26/ISIC-0025628.jpg" style="width:100%">
                                </div>
                                </div>
                                </body>
                                </html>
                                ''' ,unsafe_allow_html=True)
        st.markdown('For more information about skin cancers and moles, click [here](https://skin-scancer.streamlit.app/Skin_Cancer_Information)')


#########################Side bar################
st.sidebar.header("This project was made by:")
image_size = 50

CREATORS = {
    'Rita': 'https://avatars.githubusercontent.com/u/130187615?v=4',
    'Haitao': 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1682322545/jooigdwuvxezp0hwguh1.jpg',
    'Yui': 'https://avatars.githubusercontent.com/u/99614473?v=4',
    'Ines': 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1682322613/rpdiddalk7eqoeobfawr.jpg',

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

creators = ''.join([CREATORS_CARD.format(
    name=f'{name.split()[0]}', url=url) for name, url in CREATORS.items()])

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
