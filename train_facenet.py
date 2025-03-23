import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from mtcnn import MTCNN
from sklearn.preprocessing import LabelEncoder, Normalizer
from sklearn.svm import SVC
import pickle

# Define dataset paths
dataset_path = "Augmented_Dataset/"

# Load pre-trained FaceNet model
facenet_model = load_model("facenet_keras.h5")  # Make sure to download FaceNet model

# Initialize MTCNN face detector
detector = MTCNN()

def extract_face(image_path):
    """Detects face using MTCNN and extracts it for FaceNet."""
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(img_rgb)

    if faces:
        x, y, w, h = faces[0]['box']
        face = img_rgb[y:y+h, x:x+w]
        face = cv2.resize(face, (160, 160))
        face = np.expand_dims(face.astype('float32') / 255.0, axis=0)  # Normalize
        return face
    return None

def generate_embeddings():
    """Generates FaceNet embeddings for each person in the dataset."""
    X, y = [], []

    for person in os.listdir(dataset_path):
        person_folder = os.path.join(dataset_path, person)
        if os.path.isdir(person_folder):
            for img_name in os.listdir(person_folder):
                img_path = os.path.join(person_folder, img_name)
                face = extract_face(img_path)

                if face is not None:
                    embedding = facenet_model.predict(face)[0]
                    X.append(embedding)
                    y.append(person)

    return np.array(X), np.array(y)

# Step 1: Generate embeddings
print("🔹 Generating embeddings...")
X, y = generate_embeddings()

# Step 2: Normalize embeddings
print("🔹 Normalizing embeddings...")
in_encoder = Normalizer(norm='l2')
X = in_encoder.transform(X)

# Step 3: Encode labels
print("🔹 Encoding labels...")
out_encoder = LabelEncoder()
y = out_encoder.fit_transform(y)

# Step 4: Train classifier (SVM for recognition)
print("🔹 Training SVM classifier...")
classifier = SVC(kernel='linear', probability=True)
classifier.fit(X, y)

# Step 5: Save model and encoders
with open("facenet_classifier.pkl", "wb") as f:
    pickle.dump(classifier, f)
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(out_encoder, f)

print("✅ FaceNet training completed! Model saved as 'facenet_classifier.pkl'")
