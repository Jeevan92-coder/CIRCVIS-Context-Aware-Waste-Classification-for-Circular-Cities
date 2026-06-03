"""
Simple Streamlit demo for CIRCVIS.
Runs a single-image uploader, displays the image, performs inference using
`ModelService` (falls back to `MockModelService` if models are not available),
and shows probabilities.

Run:
    pip install -r requirements.txt
    streamlit run frontend/streamlit_app.py

Note: Large model files may make deploys to Streamlit Cloud impractical; use Mock mode
or deploy backend to a host that provides more disk/compute.
"""

from pathlib import Path
import sys
import io
import time

import numpy as np
from PIL import Image
import streamlit as st

# Ensure project root is importable when running from repo root
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import model service from backend package
try:
    from backend.app.services.model_service import ModelService, MockModelService
except Exception:
    # Importing may fail if running outside project root; provide fallback
    ModelService = None
    MockModelService = None

st.set_page_config(page_title="CIRCVIS Demo", layout="centered")
st.title("CIRCVIS — Waste Classification (Streamlit Demo)")

@st.cache_resource
def get_service(use_mock: bool = False):
    if use_mock:
        return MockModelService() if MockModelService is not None else None
    try:
        if ModelService is None:
            return MockModelService() if MockModelService is not None else None
        models_dir = PROJECT_ROOT / "models"
        svc = ModelService(models_dir=str(models_dir))
        if not svc.is_ready():
            # If models not loaded, fall back to mock
            return MockModelService() if MockModelService is not None else svc
        return svc
    except Exception:
        return MockModelService() if MockModelService is not None else None

st.sidebar.header("Options")
use_mock = st.sidebar.checkbox("Force mock mode (fast, no models)", value=False)
service = get_service(use_mock)

# Show service status
if service is None:
    st.error("Model service not available in this environment.")
else:
    try:
        ready = service.is_ready()
    except Exception:
        ready = False
    st.sidebar.write("Models loaded:" , ready)

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns([2, 3])

with col1:
    if uploaded is not None:
        image = Image.open(io.BytesIO(uploaded.read())).convert("RGB")
        st.image(image, caption="Uploaded image", use_column_width=True)
    else:
        st.info("Upload an image (JPG/PNG) to classify")

with col2:
    if uploaded is not None:
        if st.button("Predict"):
            with st.spinner("Running inference..."):
                np_img = np.array(image)
                start = time.time()
                try:
                    result = service.predict_single(np_img)
                except Exception as e:
                    st.error(f"Inference failed: {e}")
                    result = None
                elapsed = time.time() - start

            if result:
                st.subheader(f"Prediction: {result.get('class_name')} ")
                st.metric("Confidence", f"{result.get('confidence'):.2f}")
                st.write(f"Processing time (ms): {result.get('processing_time_ms'):.1f}")

                # Show bars for all classes
                all_classes = result.get("all_classes", {})
                if all_classes:
                    classes = list(all_classes.keys())
                    scores = [all_classes[k] for k in classes]
                    import pandas as pd
                    df = pd.DataFrame({"score": scores}, index=classes)
                    st.bar_chart(df.sort_values("score", ascending=False))
    else:
        st.write("")

st.write("---")
st.caption("Tip: For quick demos use mock mode; for real predictions ensure model files are present in the `models/` folder.")
