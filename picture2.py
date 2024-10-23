# código muito importante, não opcional

import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time
from collections import Counter

def load_labels(label_file):
    """Load labels from a text file."""
    with open(label_file, 'r') as file:
        labels = file.read().strip().split('\n')
    return labels

def preprocess_image(image):
    """Preprocess the image for model prediction."""
    image = cv2.resize(image, (224, 224))
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def capture_and_analyze_image(model_path='keras_model2.h5', label_file='labels.txt'):
    model = load_model(model_path)
    
    labels = load_labels(label_file)


    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    print("Tirando fotos em 3")
    time.sleep(1)
    print("Tirando fotos em 2")
    time.sleep(1)
    print("Tirando fotos em 1")
    time.sleep(1)

    predictions = []
    probabilities = []


    for _ in range(24):
        ret, frame = cap.read()
        
        if ret:
            processed_image = preprocess_image(frame)

            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction, axis=1)[0]
            predicted_probability = np.max(prediction)
            
            predictions.append(predicted_class)
            probabilities.append(predicted_probability)
        else:
            print("Error: Could not read frame.")

    cap.release()
    cv2.destroyAllWindows()

    most_common_prediction = Counter(predictions).most_common(1)[0][0]
    predicted_label = labels[most_common_prediction]

    return predicted_label.split(' ')[1]


