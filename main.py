from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import gdown


app = Flask(__name__)


MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.h5")
FILE_ID = "1TaIVUUGskqEgM0MK1bYVJnC4b-okuZZz"

os.makedirs(MODEL_DIR, exist_ok=True)


if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

print("Loading model...")
model = load_model(MODEL_PATH)
print("Model loaded successfully!")


class_labels = [
    "notumor",
    "pituitary",
    "meningioma",
    "glioma"
]


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def predict_tumor(image_path):
    IMAGE_SIZE = 128

    img = load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    img_array = img_to_array(img)

    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array, verbose=0)

    predicted_class = np.argmax(predictions)
    confidence = float(np.max(predictions))

    if class_labels[predicted_class] == "notumor":
        result = "No Tumor"
    else:
        result = f"Tumor: {class_labels[predicted_class].capitalize()}"

    return result, confidence


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if "file" not in request.files:
            return render_template("index.html", result="No file selected.")

        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", result="No file selected.")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        result, confidence = predict_tumor(filepath)

        return render_template(
            "index.html",
            result=result,
            confidence=f"{confidence*100:.2f}%",
            file_path=f"/uploads/{file.filename}"
        )

    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=False)