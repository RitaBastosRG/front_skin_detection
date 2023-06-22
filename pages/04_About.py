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
            <!DOCTYPE html>
            <html>
            <style>
            .button {
            border: none;
            color: black;
            padding: 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            }

            .button3 {border-radius: 8px;}

            </style>
            <head>
            <title>Font Awesome Icons</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            </head>
            <body>
            <h2 style='text-align: left; color:#BB9301;'>Team Members:</h2>
                        <ul stype='font-size:5;'>
                        <li><a href = 'https://github.com/RitaBastosRG')><button style="font-size:18px" class= "button button3"><i class="fa fa-github"></i> Rita Bastos</button></a> <a href = 'https://www.linkedin.com/in/rita-bastos-rg/')><button style="font-size:18px" class= "button button3"><i class="fa fa-linkedin" style="color:#0077B5"></i> Rita Bastos</button></a></li>
                        <li><a href = 'https://github.com/HelloSunPKU2023')><button style="font-size:18px" class= "button button3"><i class="fa fa-github"></i> Haitao Sun</button></a> </li>
                        <li><a href = 'https://github.com/yt50')><button style="font-size:18px" class= "button button3"><i class="fa fa-github" ></i> Yui Takeuchi-Schöpe</button></a> <a href = 'https://www.linkedin.com/in/yui-takeuchi-sch%C3%B6pe/')><button style="font-size:18px" class= "button button3"><i class="fa fa-linkedin" style="color:#0077B5"></i> Yui Takeuchi-Schöpe</button></a></li>
                        <li><a href = 'https://github.com/InesBelhadjSoulami')><button style="font-size:18px" class= "button button3"><i class="fa fa-github"></i> Ines Bel Hadj Soulami</button></a> <a href = 'https://www.linkedin.com/in/in%C3%A8s-bel-hadj-soulami-361b77195')><button style="font-size:18px" class= "button button3"><i class="fa fa-linkedin" style="color:#0077B5"></i>  Ines Bel Hadj Soulami</button></a></li>
                        </ul>
                        ''', unsafe_allow_html=True)
