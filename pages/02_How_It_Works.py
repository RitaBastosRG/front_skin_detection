import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color:#BB9301;'>Wanna know <br>how our model works? 🔎</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:#BB9301;font-size: 1em;'>Here are summaries and visualizations of SKIN-SCANCER's performance.</p>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color:#BB9301;'>📁 Dataset</h1>", unsafe_allow_html=True)


img= Image.open(open("assets/download.png", 'rb'))
mal = Image.open(open("assets/malignant.png", 'rb')).resize((280, 256))
ben = Image.open(open("assets/benign.png", 'rb')).resize((280, 256))
performance = Image.open(open("assets/Model Performance.png", 'rb'))

st.markdown(f'''The dataset we used to train and test our model is
                  [ISIC 2019 Skin Lesion images for classification](https://www.kaggle.com/datasets/salviohexia/isic-2019-skin-lesion-images-for-classification)
                  available on Kaggle.''', unsafe_allow_html=True)
# Custoum stylling
col1, col2 = st.columns(2)
# col1 picture
col1.image(mal, use_column_width=True)
# column 2 picture
col2.image(ben, use_column_width=True)

expander = st.expander("See details")

expander.markdown(f'''
                  There are 8 categories of skin cancers or moles in the dataset:
                  <ul>
                  <li><strong>Malignant (Cancerous)</strong>
                    <ul>
                    <li>MEL: Melanoma</li>
                    <li>BCC: Basal cell carcinoma</li>
                    <li>AK: Actinic keratosis</li>
                    <li>SCC: Squamous cell carcinoma</li>
                    </ul>
                  </li>
                  <li><strong>Benign (Harmless)</strong>
                    <ul>
                    <li>NV: Melanocytic nevus</li>
                    <li>BKL: Benign keratosis (solar lentigo / seborrheic keratosis / lichen planus-like keratosis)</li>
                    <li>DF: Dermatofibroma</li>
                    <li>VASC: Vascular lesion</li>
                    </ul>
                  </li>
                  <hr>

               ''', unsafe_allow_html=True)
expander.markdown('The dataset is imbalanced. We augumented the data to tackle the imbalance.')

expander.image(img)

st.markdown("<h2 style='text-align: left; color:#BB9301;'>🦾 Model</h1>", unsafe_allow_html=True)
st.markdown(f'''We used a pretrained model (<i>Resnet50</i>) for this project.''', unsafe_allow_html=True)

expander2 = st.expander("See details")
expander2.markdown(f'''<i>Resnet50</i> is a Convolutional Neural Network model with 50 layers. <br>
                  We adjusted the model to our specific tasks, shown as below: <br>
                    <ol type="1">
                    <li>Pretrained model</li>
                    <li>Input layer</li>
                    <li>Random zoom layer</li>
                    <li>Non-trainable layer</li>
                    <li>Flattening layer</li>
                    <li>Dense layer</li>
                    <li>Dropout layer</li>
                    <li>Prediction layer</li>
                    </ol>
                   Optimizer is Adam with learning rate of 1e-6.
                    <hr>


               ''', unsafe_allow_html=True)
expander2.markdown('Model Performance:')
expander2.image(performance)
