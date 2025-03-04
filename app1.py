import json
import requests
import os
from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st

# ✅ Replace this with your actual GitHub Releases download link
model_url = "https://github.com/ssaktar02/AI_plant_diseases_detection_project/releases/download/v1.0/plant_disease_prediction_model.h5"

# Define local model path
model_path = "plant_disease_prediction_model.h5"

# ✅ Check if the model exists locally, if not, download it
if not os.path.exists(model_path):
    st.write("Downloading model from GitHub Releases...")
    response = requests.get(model_url, stream=True)
    with open(model_path, "wb") as model_file:
        for chunk in response.iter_content(chunk_size=8192):
            model_file.write(chunk)
    st.write("Model downloaded successfully!")

# ✅ Load the downloaded model
model = tf.keras.models.load_model(model_path)

# ✅ Loading the class names
class_indices = json.load(open("class_indices.json"))

# Function to Load and Preprocess the Image using Pillow
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array

# Function to Predict the Class of an Image
def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    predicted_class_name = predicted_class_name.replace('_', ' ')
    predicted_class_name = predicted_class_name.replace(',', ' ')
    return predicted_class_name

# Streamlit App UI
st.set_page_config(page_title="Plant Disease Classifier", page_icon="🪴")
st.title('Plant Disease Classifier with Image')

# Sidebar
st.sidebar.markdown("""
<h1>4th Year Btech Project by</h1>
<h2>Ayush Chatterjee</h2>
<h2>Pritam Saha</h2>
<h2>Sandipan Patra</h2>
<h2>Sk Samim Aktar</h2>
""", unsafe_allow_html=True)

# Image Upload and Classification
uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((150, 150))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):
            prediction = predict_image_class(model, uploaded_image, class_indices)
            st.success(f'Prediction: {str(prediction)}')
