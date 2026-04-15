import os
import json
import random
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Optional model import depending on environment
try:
    from tensorflow.keras.models import load_model
    import numpy as np
    from utils import preprocess_image
    TENSORFLOW_AVAILABLE = True
except ImportError:
    TENSORFLOW_AVAILABLE = False

from treatment import get_treatment

app = Flask(__name__)

# Configure Uploads
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load Model
MODEL_PATH = os.path.join(app.root_path, 'model', 'crop_disease_model.h5')
CLASS_NAMES_PATH = os.path.join(app.root_path, 'model', 'class_names.json')

model = None
class_names = None

if TENSORFLOW_AVAILABLE and os.path.exists(MODEL_PATH) and os.path.exists(CLASS_NAMES_PATH):
    print("Loading CNN Model...")
    model = load_model(MODEL_PATH)
    with open(CLASS_NAMES_PATH, 'r') as f:
        class_names = json.load(f)
    print("Model loaded successfully.")
else:
    print("WARNING: Model or class names not found, or TensorFlow not installed.")
    print("Running in DEMO MODE. Predictions will be simulated.")
    # For demo mode, extract some sample keys from treatment
    from treatment import TREATMENT_DICT
    demo_classes = list(TREATMENT_DICT.keys())

@app.route('/')
def home():
    """Renders the main UI."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles image upload and prediction."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # --- PREDICTION LOGIC ---
        if model is not None and class_names is not None:
            try:
                # Preprocess
                img_array = preprocess_image(filepath)
                # Predict
                prediction = model.predict(img_array)
                predicted_idx = np.argmax(prediction, axis=1)[0]
                confidence = float(prediction[0][predicted_idx]) * 100
                predicted_class = class_names[predicted_idx]
            except Exception as e:
                return jsonify({'error': f"Prediction error: {str(e)}"}), 500
        else:
            # DEMO MODE
            import time
            time.sleep(1.5) # Simulate processing time
            predicted_class = random.choice(demo_classes)
            confidence = round(random.uniform(70.0, 99.9), 2)
        
        # Get treatment
        treatment = get_treatment(predicted_class)
        
        # Clean up the name for UI
        display_name = predicted_class.replace('___', ' - ').replace('_', ' ')
        
        return jsonify({
            'disease': display_name,
            'original_label': predicted_class,
            'confidence': f"{confidence:.2f}%",
            'treatment': treatment,
            'raw_confidence': confidence
        })
        
    return jsonify({'error': 'Invalid file format. Please upload JPG or PNG.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
