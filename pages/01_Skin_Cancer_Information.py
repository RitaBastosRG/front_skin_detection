import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: left; color:#BB9301;'>Prediction Related Informations 📗</h1>", unsafe_allow_html=True)
###################Page tab###################
st.markdown("<h3 style='text-align: center; color:#635520;'>What does skin cancer look like?</h3>", unsafe_allow_html=True)

st.image(Image.open('assets/ABCDE.jpg'))

st.markdown("<h3 style='text-align: center; color:#635520;'>My prediction is that my mole is malignant, what should I do now?</h3>", unsafe_allow_html=True)

expander = st.expander("See more details")

expander.markdown('<p style="color:#1a1814;font-size:17px">When you receive an answer from our model recommending you to <strong>"consult a dermatologist",</strong> please note that this recommendation does <strong>not</strong> automatically mean you have skin cancer.It means that our model detected some similarities to the pictures it was trained on and so you should visit a doctor to make a more in depth examination.</p>',unsafe_allow_html=True)
expander.image(Image.open('assets/doctor.jpg'))
