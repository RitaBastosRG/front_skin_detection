import streamlit as st
from PIL import Image



st.markdown("<h1 style='text-align: center; color:#BB9301;'>About SKIN-SCANCER 🔎</h1>", unsafe_allow_html=True)
img = Image.open('assets/Inspection_logo-removebg.png').resize((280, 256))
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(img)

with col3:
    st.write(' ')


about = f"""
<p>
SKIN-SCANCER is an application designed and developed by a team of Le Wagon Data Science batch #1271 students to help users with their mole concerns. <br>
The goal of the application is to raise awareness of skin cancer and to guide users to make a right decision, such as consulting a dermatologist or keeping an eye on the development of the mole.
</p>
"""


st.markdown(about, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color:#BB9301;'>GitHub link:</h2>", unsafe_allow_html=True)
#st.markdown(f"https://github.com/RitaBastosRG/skin_detection_1271 <br> https://github.com/RitaBastosRG/front_skin_detection"
#, unsafe_allow_html=True)
# Add Link to your repo
'''
    [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/RitaBastosRG/skin_detection_1271)

'''
st.markdown("<br>",unsafe_allow_html=True)

st.markdown('''
            <h2 style='text-align: left; color:#BB9301;'>Team Members:</h2>
            <ul stype='font-size:5;'>
            <li><a [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&labe (https://github.com/RitaBastosRG)>Rita Bastos</a></li>
            <li><a href='https://github.com/HelloSunPKU2023'>Haitao Sun</a></li>
            <li><a href='https://github.com/yt50'>Yui Takeuchi-Schöpe</a></li>
            <li><a href='https://github.com/InesBelhadjSoulami'>Ines Bel Hadj Soulami</a></li>
            </ul>
            ''', unsafe_allow_html=True)
