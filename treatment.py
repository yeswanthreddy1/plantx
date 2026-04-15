# Disease to Treatment Mapping Dictionary
# Maps the 38 PlantVillage classes to their respective treatments.

TREATMENT_DICT = {
    # Apple
    "Apple___Apple_scab": "Apply fungicides containing captan, myclobutanil, or sulfur. Ensure good air circulation.",
    "Apple___Black_rot": "Remove dead wood, apply fungicide like captan or thiophanate-methyl.",
    "Apple___Cedar_apple_rust": "Remove nearby cedar trees if possible. Apply fungicidal sprays containing myclobutanil.",
    "Apple___healthy": "No treatment needed. Crop is healthy.",

    # Blueberry
    "Blueberry___healthy": "No treatment needed. Crop is healthy.",

    # Cherry
    "Cherry_(including_sour)___Powdery_mildew": "Apply sulfur or potassium bicarbonate sprays. Ensure good pruning for airflow.",
    "Cherry_(including_sour)___healthy": "No treatment needed. Crop is healthy.",

    # Corn
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Use resistant hybrids. Apply foliar fungicides if severe.",
    "Corn_(maize)___Common_rust_": "Apply sulfur-based fungicides or use rust-resistant corn varieties.",
    "Corn_(maize)___Northern_Leaf_Blight": "Use disease-resistant varieties. Apply mancozeb or chlorothalonil base fungicides.",
    "Corn_(maize)___healthy": "No treatment needed. Crop is healthy.",

    # Grape
    "Grape___Black_rot": "Use mancozeb, myclobutanil, or copper fungicides. Practice canopy management.",
    "Grape___Esca_(Black_Measles)": "Remove infected woody parts. No effective chemical cure, focus on prevention and sanitation.",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Apply Bordeaux mixture or copper fungicides. Remove infected debris.",
    "Grape___healthy": "No treatment needed. Crop is healthy.",

    # Orange
    "Orange___Haunglongbing_(Citrus_greening)": "Remove infected trees. Control Asian citrus psyllid with insecticides.",

    # Peach
    "Peach___Bacterial_spot": "Spray copper-based bactericides during leaf drop in fall and before bud swell in spring.",
    "Peach___healthy": "No treatment needed. Crop is healthy.",

    # Pepper, bell
    "Pepper,_bell___Bacterial_spot": "Apply copper sprays combined with mancozeb. Rotate crops.",
    "Pepper,_bell___healthy": "No treatment needed. Crop is healthy.",

    # Potato
    "Potato___Early_blight": "Apply chlorothalonil or mancozeb. Ensure proper crop nutrition.",
    "Potato___Late_blight": "Apply systemic and contact fungicides (e.g., mefenoxam, chlorothalonil). Destroy infected plants immediately.",
    "Potato___healthy": "No treatment needed. Crop is healthy.",

    # Raspberry
    "Raspberry___healthy": "No treatment needed. Crop is healthy.",

    # Soybean
    "Soybean___healthy": "No treatment needed. Crop is healthy.",

    # Squash
    "Squash___Powdery_mildew": "Apply neem oil, sulfur, or potassium bicarbonate. Avoid overhead watering.",

    # Strawberry
    "Strawberry___Leaf_scorch": "Remove infected leaves. Apply copper or captan based fungicides. Keep foliage dry.",
    "Strawberry___healthy": "No treatment needed. Crop is healthy.",

    # Tomato
    "Tomato___Bacterial_spot": "Apply fixed copper sprays regularly. Avoid overhead watering.",
    "Tomato___Early_blight": "Use Mancozeb fungicide spray or chlorothalonil. Rotate crops.",
    "Tomato___Late_blight": "Apply chlorothalonil. Remove infected plants totally as it spreads fast.",
    "Tomato___Leaf_Mold": "Improve air circulation. Apply fungicides such as chlorothalonil or copper.",
    "Tomato___Septoria_leaf_spot": "Apply chlorothalonil or copper fungicides. Remove infected lower leaves.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Spray insecticidal soap, neem oil, or specific miticides.",
    "Tomato___Target_Spot": "Apply chlorothalonil or mancozeb base fungicides. Ensure good airflow.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Control whiteflies using reflective mulches or insecticides. Remove infected plants.",
    "Tomato___Tomato_mosaic_virus": "No chemical cure. Remove and destroy infected plants. Wash hands and tools frequently.",
    "Tomato___healthy": "No treatment needed. Crop is healthy."
}

def get_treatment(disease_name):
    """Returns the treatment suggestion for a given disease name."""
    return TREATMENT_DICT.get(disease_name, "Consult a local agricultural expert for accurate treatment.")
