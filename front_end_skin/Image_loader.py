import streamlit as st
from PIL import Image

###############################
#Loading Image related
def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)

def main():
    st.header('Upload your image')
    load_image()
##########
#Display progress and status
#with st.spinner(text='In progress'):
 #   time.sleep(5)
  #  st.success('Done')
#st.progress(progress_variable_1_to_100)



###########Display progress and status
progress_bar = col2.progress(0)
for perc_completed in range(100):
    time.sleep(5)
    progress_bar.progress(perc_completed+1)
