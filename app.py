import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load model (adjust path if needed)
@st.cache_resource
def load_my_model():
    return load_model("models/circvis_model.keras")

model = load_my_model()

st.title("♻️ CIRCVIS Waste Classification")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((224, 224))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    st.subheader("Prediction:")
    st.write(prediction)
