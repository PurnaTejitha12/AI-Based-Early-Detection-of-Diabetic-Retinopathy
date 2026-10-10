from pathlib import Path

import numpy as np
from PIL import Image
import tensorflow as tf


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "dr_model.keras"

# Change this to match your model's training input size.
IMAGE_SIZE = (224, 224)

# Change these labels to match your training class order.
CLASS_NAMES = [
    "No DR",
    "Mild DR",
    "Moderate DR",
    "Severe DR",
    "Proliferative DR",
]

_model = None


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

def load_model():
    global _model

    if _model is None:
        if not MODEL_PATH.is_file():
            raise FileNotFoundError(
                f"Trained model not found: {MODEL_PATH}. "
                "Update MODEL_PATH to your actual trained model."
            )

        _model = tf.keras.models.load_model(
            str(MODEL_PATH),
            compile=False
        )

    return _model


# --------------------------------------------------
# IMAGE PREPROCESSING
# --------------------------------------------------

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")

    image = image.resize(
        IMAGE_SIZE,
        Image.Resampling.LANCZOS
    )

    image = np.asarray(image, dtype=np.float32)

    # IMPORTANT:
    # Match preprocessing to your model's training pipeline.
    # This normalization is only appropriate if the model
    # was trained with RGB pixel values scaled to [0, 1].
    image = image / 255.0

    return np.expand_dims(image, axis=0)


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

def predict_image(image_path):
    model = load_model()
    image = preprocess_image(image_path)

    output = model.predict(image, verbose=0)
    output = np.asarray(output)

    if output.ndim != 2 or output.shape[0] != 1:
        raise ValueError(
            f"Unexpected model output shape: {output.shape}"
        )

    scores = output[0]

    if len(scores) == 1:
        # Binary model: assumes the single output is the
        # probability of DR, produced by a sigmoid.
        dr_probability = float(scores[0])

        if not 0 <= dr_probability <= 1:
            raise ValueError(
                "Single-output model must return a sigmoid probability."
            )

        probabilities = np.array([
            1.0 - dr_probability,
            dr_probability
        ])

        labels = ["No DR", "DR Detected"]

    elif len(scores) == len(CLASS_NAMES):
        # Multiclass model.
        # If model outputs logits, apply softmax.
        if (
            np.any(scores < 0)
            or np.any(scores > 1)
            or not np.isclose(np.sum(scores), 1.0, atol=1e-3)
        ):
            scores = tf.nn.softmax(scores).numpy()

        probabilities = scores
        labels = CLASS_NAMES

    else:
        raise ValueError(
            f"Model returned {len(scores)} outputs, but "
            f"{len(CLASS_NAMES)} class labels are configured."
        )

    predicted_index = int(np.argmax(probabilities))

    prediction = labels[predicted_index]
    confidence = float(probabilities[predicted_index]) * 100.0

    return prediction, confidence