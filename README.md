AI Plant Disease Detection & Chatbot Assistant

📌 Overview

This is a Streamlit-based web application that allows users to:

Detect plant diseases using image classification.

Ask a chatbot questions about plant diseases.

The app is built using TensorFlow, Streamlit, Google Generative AI (Gemini), and OpenAI APIs.

📂 Project Structure

/plant_disease_detection_project
│── /venv                # Virtual environment (optional)
│── /models              # Folder for storing models (if needed)
│── app.py               # Main Streamlit application
│── class_indices.json   # Mapping of class indices to disease names
│── requirements.txt     # Dependencies for the project
│── README.md            # Project documentation

🛠 Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/ssaktar02/AI_plant_diseases_detection_project.git
cd AI_plant_diseases_detection_project

2️⃣ Set Up a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Required Packages

pip install -r requirements.txt

🚀 How to Run the Application

streamlit run app.py

This will launch the web app in your default browser.

🌱 Features

1️⃣ Plant Disease Detection (Image Upload)

Users upload an image of a plant leaf.

The app processes the image and predicts the disease using a pre-trained deep learning model.

Model is automatically downloaded from GitHub Releases if not found locally.

2️⃣ Chatbot Q&A (AI-Powered Assistant)

Users can ask questions about plant diseases.

The chatbot is powered by Google Gemini AI (Google Generative AI API).

Provides informative answers related to plant health, disease prevention, and treatment.

🛠 Technical Details

🔹 Machine Learning Model

The disease detection model is a Convolutional Neural Network (CNN).

Trained on a dataset of plant leaf images with different diseases.

The model is stored as plant_disease_prediction_model.h5 and fetched from GitHub Releases when needed.

🔹 Image Processing

Uses PIL (Pillow) for image loading and resizing.

Images are normalized and preprocessed before being fed into the model.

🔹 Chatbot (Google Generative AI)

Integrated using Google Gemini API.

Accepts natural language questions and generates plant disease-related responses.

🌍 Deployment Options

Run locally with Streamlit.

Deploy on Streamlit Cloud:

Go to Streamlit Cloud

Connect the GitHub repository

Set app.py as the main file

Deploy 🚀

🏗 Future Enhancements

✅ Add a treatment suggestion feature for each detected disease.
✅ Support multiple languages in the chatbot.
✅ Improve model accuracy with a larger dataset.

🤝 Contributing

Pull requests are welcome! Please open an issue first for major changes.

📝 License

This project is licensed under the MIT License.

📞 Contact

Developer: Sk Samim Aktar

GitHub: ssaktar02

Email: [your-email@example.com]
