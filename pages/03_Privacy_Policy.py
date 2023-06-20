import streamlit as st

# page_bg_img = '''
# <style>
# .stApp {
#   background-image: url("https://images.unsplash.com/photo-1621799754526-a0d52c49fad5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80");
#   background-size: cover;
# }
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)
font_color='#BB9301'

st.markdown("<h1 style='text-align: center; color:#BB9301;'>SKIN-SCANCER Privacy Policy 🔏</h1>", unsafe_allow_html=True)


privacy_policy = f"""
<ul>
<li style="color:{font_color};font-size:30px"><strong> What data do we collect? </strong></li>
We collect the image information that you upload to our website.

<li style="color:{font_color};font-size:30px"><strong>What data do we not collect? </strong></li>
We do not collect your IP address, personally identifiable browser, nor OS information. We don’t serve any tracking or identifying cookies.

<li style="color:{font_color};font-size:30px"><strong>How do we collect your data?</strong></li>
We collect data when you consent to this privacy policy and upload an image to our website.

<li style="color:{font_color};font-size:30px"><strong>How will we use your data?</strong></li>
We collect your data so that we can process your uploaded data and provide you with the prediction of our Machine Learning model.

<li style="color:{font_color};font-size:30px"><strong> Will your data be stored?</strong></li>
No, we do not store any of your personal data. We will only use your personal data at the time of your usage of our website for the purposes for which we collected your data.

</ul>
"""

st.markdown(privacy_policy, unsafe_allow_html=True)
