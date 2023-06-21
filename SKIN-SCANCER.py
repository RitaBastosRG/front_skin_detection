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
st.markdown(f"""<p style="color:#BB9301;font-size:40px;text-align:center"><strong>🔎 SKIN-SCANCER 🔎</strong></p>""",
              unsafe_allow_html=True)
# Custoum stylling
col1, col2 = st.columns(2)
# col1 picture
image1 = Image.open('assets/abcde-removebg-preview.png').resize((280, 256))
col1.image(image1, use_column_width=True)
# column 2 picture
image = Image.open('assets/Inspection_logo-removebg.png').resize((280, 256))
col2.image(image, use_column_width=True)
st.markdown(f"""<p style="color:#BB9301;font-size:30px"><strong>Check your skin using our website and have the prediction.</strong></p>""", unsafe_allow_html=True)
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
    uploaded_file = st.file_uploader(label='Pick an image to test',type=['png','jpg','jpeg'])
    # st.session_state['uploaded_file'] = uploaded_file
    if uploaded_file is not None:

        image_data = uploaded_file.getvalue()
        st.image(image_data)
        st.write('Processing...🔎')
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
            time.sleep(0.1)
        prediction = response.json()
        pred = prediction['possibility']
        st.markdown(f'<p style="color:#BB9301;font-size:20px">There is {round(pred*100,2)}% probability that your mole falls into one of the three cancer categories (AK, SCC, BCC).</p>',unsafe_allow_html=True)

        if pred*100>50:
            st.markdown('<p style="color:#BB9301;font-size:17px">It is strongly recommended to consult a dermatologist for further evaluation and advice.</p>',unsafe_allow_html=True)
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
