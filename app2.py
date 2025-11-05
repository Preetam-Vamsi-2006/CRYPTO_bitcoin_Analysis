
import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from PIL import Image

# ------------------------
# Load trained model
# ------------------------
model_path = 'random_forest_model.pkl'
with open(model_path, 'rb') as file:
    model_rf = pickle.load(file)

# ------------------------
# Prediction function
# ------------------------
def predict_btc_price(input_data):
    prediction = model_rf.predict(input_data)
    return prediction[0]

# ------------------------
# Streamlit App
# ------------------------
st.set_page_config(page_title="BTC Price Predictor", page_icon="💰", layout="centered")

# ------------------------
# Custom Vibrant Black Theme
# ------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        background-image: linear-gradient(160deg, #000000, #1a1a1a, #2c2c2c);
        color: white;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f, #161616, #1f1f1f);
        padding-top: 150px; /* visually pushes the sidebar down */
        color: white;
        box-shadow: inset 0 0 15px rgba(0,255,204,0.2);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #00ffcc;
        text-align: center;
    }

    p, div, span {
        color: #f0f0f0;
    }

    .stButton>button {
        background-color: #00ffcc;
        color: black;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #ff0080;
        color: white;
    }

    .crypto-tagline {
        text-align: center;
        font-size: 18px;
        color: #cccccc;
        font-style: italic;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# Header Section with Image
# ------------------------
st.title("💰 Bitcoin Price Prediction Dashboard")

# Insert your crypto-themed image (replace with your path)
IMAGE_PATH = r"C:\Users\golla\AVSCODE\CapstoneProjectsAll\CRYPTO ANALYSIS\bitcoin.png"  # Example: local image
try:
    image = Image.open(IMAGE_PATH)
    st.image(image, use_column_width=True)
except Exception:
    st.warning("⚠️ Crypto image not found — please add crypto_banner.jpg in the same directory.")

# Eye-catching crypto lines
st.markdown(
    """
    <p class="crypto-tagline">
        🚀 *Predict the next Bitcoin move using Machine Learning!* <br>
        "Trade smart. Analyze better. Let AI guide your crypto insights." 💹
    </p>
    """,
    unsafe_allow_html=True
)

# ------------------------
# Sidebar Inputs (Visually Lowered)
# ------------------------
st.sidebar.title("📊 Input Market Features")

usdt_close = st.sidebar.number_input('USDT Close Price', min_value=0.0, format="%.2f")
usdt_volume = st.sidebar.number_input('USDT Volume', min_value=0.0, format="%.2f")
bnb_close = st.sidebar.number_input('BNB Close Price', min_value=0.0, format="%.2f")
bnb_volume = st.sidebar.number_input('BNB Volume', min_value=0.0, format="%.2f")

# Create dataframe for prediction
input_data = pd.DataFrame({
    'USDT_Close': [usdt_close],
    'USDT_Volume': [usdt_volume],
    'BNB_Close': [bnb_close],
    'BNB_Volume': [bnb_volume]
})

# ------------------------
# Prediction Button
# ------------------------
if st.button('🔮 Predict BTC Close Price'):
    predicted_price = predict_btc_price(input_data)
    st.success(f"💸 **Predicted BTC Close Price:** ${predicted_price:,.2f}")
    st.balloons()

# ------------------------
# Footer
# ------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#999;'>© 2025 CryptoML Labs | Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
