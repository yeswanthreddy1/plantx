# PlantX: Crop Disease Detection System 🌱

A comprehensive ML-powered web application that detects plant diseases from leaf images using a Custom Convolutional Neural Network (CNN).

## Features
- **Custom CNN Model**: Trained from scratch on the PlantVillage dataset.
- **Premium UI**: Dark-themed, glassmorphism UI with drag-and-drop file upload.
- **Treatment Suggestions**: Provides immediate actionable feedback, such as exact pesticide or care routines.
- **Demo Mode**: Run the web app even before compiling/training the model locally just to test the UI.

## Tech Stack
- **Machine Learning**: TensorFlow / Keras
- **Backend API**: Flask (Python)
- **Frontend**: Vanilla JS, HTML, CSS
- **Dataset**: [PlantVillage Kaggle Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)

---

## 🛠️ Step 1: Model Training (Google Colab Recommended)

1. Open Google Colab and upload the `notebooks/train_colab.ipynb` file.
2. Upload your Kaggle `kaggle.json` inside Colab to download the dataset automatically.
3. Run all cells to process the images and train the custom CNN model.
4. After training finishes, it will output two files:
   - `crop_disease_model.h5`
   - `class_names.json`
5. Download these files and place them into the `model/` folder in this local repository.

*(Alternatively, you can run `python train.py` locally if you downloaded the dataset and have a capable GPU)*

---

## 🖥️ Step 2: Running the Web App Locally

1. Open your terminal in this repository.
2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to: `http://localhost:5000`

> **Note on Demo Mode:** If you start `app.py` *before* adding the `.h5` model to the `model/` folder, the app will run in "Demo Mode", simulating predictions so you can test the frontend UI immediately.

---

## 📁 Folder Structure

```
├── app.py                     # Main Flask Server
├── train.py                   # Local Training Script (Custom CNN)
├── treatment.py               # Treatment Suggestion Dictionary
├── utils.py                   # Image Preprocessing scripts
├── requirements.txt           # Python packages
├── README.md                  # This file
├── model/                     # Place generated .h5 and .json here
├── dataset/                   # Local dataset directory (not committed to git)
├── notebooks/
│   └── train_colab.ipynb      # Google Colab notebook for GPU training
├── static/
│   ├── css/
│   │   └── style.css          # UI styles
│   └── js/
│       └── app.js             # Form handling & async fetches
└── templates/
    └── index.html             # UI HTML
```
