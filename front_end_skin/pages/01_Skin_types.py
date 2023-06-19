import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: left; color:#BB9301;'>Prediction Related Informations 📗</h1>", unsafe_allow_html=True)
###################Page tab###################
st.set_page_config(
    page_title = 'SKIN-SCANCER',
    page_icon = '🔎',
    layout="centered", # wide
    initial_sidebar_state="collapsed") # collapsed)

st.header("Prediction Related Informations")
choice = st.radio("**Search between different types of skin lesions**", ['Nevus', 'Basal Carcinoma', 'Other'])
if choice == "Basal Carcinoma":
    with st.expander("Click to read more"):
        st.write(" Basal cell carcinoma (BCC) is the most common form of skin cancer and the most frequently occurring form of all cancers. In the U.S. alone, an estimated 3.6 million cases are diagnosed each year.")
        st.write("These are some **warning** signs you should take into account")
        st.image(Image.open('assets/BCC_image.jpg'))
elif choice == "Nevus":
    with st.expander("Click to read more"):
        st.write("Nevus is a **bening** growth on the skin that is formed by a cluster of melanocytes (cells that make a substance called melanin, which gives color to skin and eyes). A nevus is usually dark and may be raised from the skin. Also called mole.")
        st.image(Image.open('assets/nevus.jpg'))
