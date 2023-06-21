import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: left; color:#BB9301;'>Prediction Related Informations 📗</h1>", unsafe_allow_html=True)
###################Page tab###################
st.markdown(f"""<p style=;font-size:25px;text-align:center"><strong>The ABCDE Rule for early detection</strong></p>""",
              unsafe_allow_html=True)
st.image(Image.open('assets/ABCDE.jpg'))

