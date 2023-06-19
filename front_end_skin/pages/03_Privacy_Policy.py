import streamlit as st

st.header("SKIN-SCANCER Privacy Policy")

privacy_policy = f"""
<ul>
<li style="color:#b08204;font-size:30px"><strong> What data do we collect? </strong></li>
We collect the image information that you upload to our website.

<li style="color:#b08204;font-size:30px"><strong>What data do we not collect? </strong></li>
We do not collect your IP address, personally identifiable browser, nor OS information. We don’t serve any tracking or identifying cookies.

<li style="color:#b08204;font-size:30px"><strong>How do we collect your data?</strong></li>
We collect data when you consent to this privacy policy and upload an image to our website.

<li style="color:#b08204;font-size:30px"><strong>How will we use your data?</strong></li>
We collect your data so that we can process your uploaded data and provide you with the prediction of our Machine Learning model.

<li style="color:#b08204;font-size:30px"><strong> Will your data be stored?</strong></li>
No, we do not store any of your personal data. We will only use your personal data at the time of your usage of our website for the purposes for which we collected your data.

</ul>
"""

st.markdown(privacy_policy, unsafe_allow_html=True)
