# ♻️ CIRCVIS — Context-Aware Waste Classification for Circular Cities

AI-powered waste classification platform built for smart and circular city ecosystems.  
CIRCVIS combines computer vision, FastAPI services, and a lightweight frontend to classify municipal waste into multiple recyclable categories in real time.

---

## 🚀 Features

- 🧠 AI-based waste classification using deep learning
- ♻️ Detects 7 waste categories:
  - Plastic
  - Organic
  - Metal
  - Glass
  - Textile
  - Paper/Cardboard
  - Miscellaneous
- 📤 Image upload prediction
- 📷 Camera capture support
- 🌐 URL-based image prediction
- 🔄 Batch image inference
- ⚡ FastAPI backend with REST APIs
- 🖥️ Lightweight frontend dashboard
- 🐳 Dockerized deployment support
- 📊 Prediction logging & analytics support

---

## 🏗️ System Architecture

```text
User Input
   │
   ├── Upload Image
   ├── Camera Capture
   ├── Image URL
   └── Batch Images
        │
        ▼
FastAPI Backend
        │
        ▼
Deep Learning Model Inference
        │
        ▼
Waste Category Prediction
        │
        ▼
Frontend Dashboard / API Response
```

---

## 📂 Project Structure

```text
CIRCVIS/
│
├── backend/                # FastAPI backend services
├── frontend/               # Static frontend pages & assets
├── models/                 # Trained AI models
├── data/                   # Training & preprocessing scripts
│
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.bat
│
├── API_DOCUMENTATION.md
├── QUICK_START_GUIDE.md
└── PROJECT_SUMMARY.md
```

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- Python
- Uvicorn

### Machine Learning
- TensorFlow / Keras
- EfficientNetB0
- ResNet50

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- Docker
- Docker Compose

---

# 🧪 API Endpoints

## Health Check

```bash
GET /health
```

---

## Single Image Prediction

```bash
POST /api/predict
```

### Example

```bash
curl -X POST -F "file=@image.jpg" \
http://localhost:8000/api/predict
```

---

## Batch Prediction

```bash
POST /api/predict-batch
```

---

## Base64 Prediction

```bash
POST /api/predict-base64
```

---

## URL Prediction

```bash
POST /api/predict-url
```

---

## Available Models

```bash
GET /api/models
```

---

## Supported Classes

```bash
GET /api/classes
```

---

# ⚡ Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/Jeevan92-coder/CIRCVIS-Context-Aware-Waste-Classification-for-Circular-Cities.git
```

## 2. Navigate to Project

```bash
cd CIRCVIS-Context-Aware-Waste-Classification-for-Circular-Cities
```

## 3. Create Virtual Environment

```powershell
python -m venv venv
```

## 4. Activate Environment

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

## 6. Start Backend

```powershell
python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Streamlit demo (optional)

You can run a simple interactive demo using Streamlit. This is useful for quick demos and interactive exploration, but note that Streamlit Community Cloud may not be suitable for very large model files.

1. Install dependencies (includes `streamlit`):

```powershell
pip install -r requirements.txt
```

2. Run the demo locally:

```powershell
streamlit run frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

3. Open the demo in your browser:

```text
http://localhost:8501
```

Deployment note: To publish on Streamlit Community Cloud, push the repository to GitHub and create a new app pointing to `frontend/streamlit_app.py`. If your repository includes large model files, consider using the mock mode (toggle in the sidebar) or host the model files on object storage and modify the app to download them at startup.


# 🌐 Access Application

```text
http://localhost:8000
```

---

# 🐳 Docker Deployment

## Build & Run

```bash
docker compose up --build
```

---

# 📊 Model Information

Primary production model:

```text
models/circvis_model.keras
```

Additional experimental checkpoints:

- EfficientNetB0
- ResNet50
- Fine-tuned checkpoints

---

# ⚠️ Important Notes

- If trained models are missing, the backend may switch to mock inference mode.
- Large model files are managed using Git LFS.
- Static frontend assets are served directly by FastAPI.

---

# 🔍 Troubleshooting

## Port already in use

Change the running port:

```bash
--port 8080
```

---

## Missing dependencies

Reinstall requirements:

```bash
pip install -r requirements.txt
```

---

## Model loading errors

Verify model files exist inside:

```text
models/
```

---

# 📈 Future Improvements

- Real-time webcam inference
- Mobile deployment
- Edge AI optimization
- Smart recycling recommendations
- IoT smart-bin integration
- Cloud deployment pipeline

---

# 🤝 Contributing

Pull requests and improvements are welcome.

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

Meher Jeevan  
AI/ML & Smart City Systems Developer
