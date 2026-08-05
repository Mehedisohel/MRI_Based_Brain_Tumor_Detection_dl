# 🧠 Brain Tumor Detection Using Deep Learning

A web-based Brain Tumor Detection System built using **TensorFlow/Keras**, **VGG16 Transfer Learning**, and **Flask**. The application allows users to upload MRI brain images and predicts the tumor type with a confidence score through an intuitive web interface.

---

# 📌 Features

- 🧠 Brain MRI tumor classification
- 📂 Image upload functionality
- 🤖 VGG16 Transfer Learning model
- 🛡️ Custom classification head with Dropout (50% & 30%) to prevent overfitting
- 📊 Confidence score display
- 🌐 Responsive Flask web application
- 🎨 Modern Bootstrap-based user interface

---

# 🩺 Tumor Classes

The model classifies MRI images into four categories:

- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask

## Deep Learning
- TensorFlow
- Keras
- VGG16 Transfer Learning
- NumPy

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

# 📁 Project Structure

```text
MRI_Based_Brain_Tumor_Detection_dl/
│
├── static/
│   ├── assets/
│   │   ├── WhatsApp Image.jpeg
│   │   ├── img1.jpeg
│   │   ├── img2.jpeg
│   │   ├── img3.jpeg
│   │   └── img3.png
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── Scripts.js
│
├── templates/
│   └── index.html
│
├── .gitattributes
├── .gitignore
├── .python-version
├── Profile
├── README.md
├── main.py
└── requirements.txt
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone [https://github.com/Mehedisohel/MRI_Based_Brain_Tumor_Detection_dl.git]
```

## 2. Navigate to the Project

```bash
cd MRI_Based_Brain_Tumor_Detection_dl
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
python main.py
```

Open your browser and visit:

```text
[http://127.0.0.1:5000]
```

---

# 📂 Dataset

The model was trained on a comprehensive dataset of MRI brain scans. 

> **Note:** The original dataset can be found here: *https://www.kaggle.com/datasets/vinayjayanti/brain-tumor-mris/data*

---

# 🧠 Model Details

| Item | Description |
|------|-------------|
| Model | VGG16 |
| Strategy | Transfer Learning with Fine-Tuning (Block 5 Convolutional Layers) |
| Framework | TensorFlow / Keras |
| Input Size | 128 × 128 |
| Classes | 4 |
| Optimizer | Adam (Learning Rate: 0.00005) |
| Loss Function | Sparse Categorical Crossentropy |

---

# 📊 Performance

| Metric | Value |
|--------|------:|
| Training Accuracy | 98% |
| Test Accuracy | 92% |

---

# 🔄 Prediction Workflow

1. Upload an MRI brain image.
2. Image is preprocessed.
3. The trained VGG16 model performs inference.
4. Predicted tumor class is displayed.
5. Confidence score is shown.

---

# 📷 Screenshots

| Home Page | Prediction Result |
|-----------|-------------------|
| ![Home](static/assets/WhatsApp%20Image%202026-07-08%20at%2012.29.26%20AM.jpeg) | <img width="1920" height="900" alt="image" src="https://github.com/user-attachments/assets/91b595ec-b2b5-479e-a961-01a992df7c43" />

---

# 🌍 Deployment

This project can be deployed on:

- Render
- Railway
- PythonAnywhere

---

# 🔮 Future Improvements

- Grad-CAM visualization
- DICOM image support
- Prediction history
- User authentication
- Cloud deployment
- REST API support

---

# 👨‍💻 Author

- **Mohammad Mehedi Sohel**
- **Intesar Hossain**

B.Sc. in Computer Science & Engineering

---

# 📄 License

This project is intended for educational and research purposes.
