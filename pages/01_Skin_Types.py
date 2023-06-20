import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: left; color:#BB9301;'>Prediction Related Informations 📗</h1>", unsafe_allow_html=True)
###################Page tab###################
col1, col2, col3 = st.columns(3)

with col1:
   st.markdown(f"""<p style="color:#BB9301;font-size:30px"><strong>Nevus</strong></p>""", unsafe_allow_html=True)
   st.write("Nevus is a **bening** growth on the skin that is formed by a cluster of melanocytes (cells that make a substance called melanin, which gives color to skin and eyes). A nevus is usually dark and may be raised from the skin. Also called mole.")
   st.image(Image.open('assets/nevus.jpg'))

with col2:
   st.markdown(f"""<p style="color:#BB9301;font-size:30px"><strong>Basal cell carcinoma (BCC)</strong></p>""", unsafe_allow_html=True)
   st.write(" Basal cell carcinoma (BCC) is the most common form of skin cancer and the most frequently occurring form of all cancers. In the U.S. alone, an estimated 3.6 million cases are diagnosed each year.")
   st.write("These are some **warning** signs you should take into account")
   st.image(Image.open('assets/BCC_image.jpg'))

with col3:
   st.header("Other")
   st.image(Image.open("https://images.unsplash.com/photo-1626668011660-051379e9b211?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"))
