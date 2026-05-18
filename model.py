import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

try:
    model = load_model("model.h5")
except Exception as e:
    print("Model load error:", e)
    model = None

classes = ["No_DR", "Mild", "Moderate", "Severe", "Proliferative_DR"]

def predict_image(img_path):
    try:
        if model is None:
            return "Model Not Loaded", 0

        img = image.load_img(img_path, target_size=(224,224))
        img = image.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        preds = model.predict(img)[0]
        class_idx = np.argmax(preds)

        return classes[class_idx], round(float(np.max(preds))*100,2)

    except Exception as e:
        print("Prediction error:", e)
        return "Error", 0
