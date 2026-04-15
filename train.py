import os
import json
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ==========================================
# CONFIGURATION
# ==========================================
# IMPORTANT: Update this path to where you extracted the PlantVillage dataset
DATASET_DIR = "dataset/PlantVillage"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 15
MODEL_SAVE_DIR = "model"

os.makedirs(MODEL_SAVE_DIR, exist_ok=True)

# ==========================================
# 1. DATA PREPARATION (Data Augmentation & Splitting)
# ==========================================
print("Setting up Data Generators...")

# We use validation_split=0.2 to reserve 20% for validation
datagen = ImageDataGenerator(
    rescale=1./255,           # Normalize pixel values
    rotation_range=20,        # Data augmentation
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2      # 80/20 train/val split
)

# Training Set
train_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

# Validation Set
val_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# Save class names for the web app
class_names = list(train_generator.class_indices.keys())
with open(os.path.join(MODEL_SAVE_DIR, 'class_names.json'), 'w') as f:
    json.dump(class_names, f)

NUM_CLASSES = len(class_names)
print(f"Detected {NUM_CLASSES} classes.")

# ==========================================
# 2. BUILD CUSTOM CNN MODEL
# ==========================================
print("Building CNN architecture...")
model = Sequential([
    # Block 1
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
    MaxPooling2D((2, 2)),
    
    # Block 2
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    
    # Block 3
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    
    # Flatten & Dense
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5), # Prevent overfitting
    Dense(NUM_CLASSES, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ==========================================
# 3. TRAINING
# ==========================================
print("Starting training...")
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=val_generator
)

# ==========================================
# 4. SAVE MODEL
# ==========================================
model_path = os.path.join(MODEL_SAVE_DIR, 'crop_disease_model.h5')
model.save(model_path)
print(f"Model saved successfully to {model_path}")
