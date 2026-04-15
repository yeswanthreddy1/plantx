import json
import os
import numpy as np
from PIL import Image

def load_class_names(json_path):
    """Loads class names from a JSON file."""
    if not os.path.exists(json_path):
        return None
    with open(json_path, 'r') as f:
        return json.load(f)

def preprocess_image(image_path, target_size=(224, 224)):
    """
    Loads an image, resizes it, and normalizes it for the CNN model.
    """
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img)
    # Normalize pixel values to [0, 1] as done during DataGen rescale=1./255
    img_array = img_array / 255.0
    # Expand dimensions to match batch format (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
