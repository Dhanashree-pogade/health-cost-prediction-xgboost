import streamlit as st
import pandas as pd
import pickle
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Health Prediction AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.12), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,0.12), transparent 30%),
        linear-gradient(135deg, #f8fafc 0%, #eef2ff 50%, #f0f9ff 100%);
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Hero section */
.hero {
    background: linear-gradient(
        135deg,
        #312e81 0%,
        #4f46e5 45%,
        #0284c7 100%
    );
    padding: 42px 45px;
    border-radius: 28px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 20px 50px rgba(49,46,129,0.25);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
    letter-spacing: -1px;
}

.hero p {
    font-size: 17px;
    opacity: 0.9;
    margin-bottom: 0;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.88);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.8);
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 10px 35px rgba(15,23,42,0.08);
    margin-bottom: 20px;
}

.card-title {
    font-size: 21px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 5px;
}

.card-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 20px;
}

/* Input labels */
label {
    font-weight: 600 !important;
    color: #334155 !important;
}

/* Input boxes */
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div {
    border-radius: 12px !important;
}

/* Button */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    padding: 14px 20px;
    font-size: 16px;
    font-weight: 700;
    color: white;
    background: linear-gradient(135deg, #4f46e5, #0284c7);
    box-shadow: 0 8px 20px rgba(79,70,229,0.25);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(79,70,229,0.35);
}

/* Result */
.result-card {
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(15,23,42,0.10);
    border: 1px solid #e2e8f0;
    margin-top: 20px;
}

.result-icon {
    font-size: 48px;
    margin-bottom: 8px;
}

.result-title {
    font-size: 18px;
    font-weight: 600;
    color: #64748b;
}

.result-value {
    font-size: 42px;
    font-weight: 800;
    color: #4f46e5;
    margin: 5px 0;
}

.info-box {
    background: #eef2ff;
    border-left: 5px solid #4f46e5;
    padding: 15px 18px;
    border-radius: 12px;
    color: #3730a3;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 35px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    model_path = "xgboost.pkl"

    if not os.path.exists(model_path):
        return None

    with open(model_path, "rb") as file:
        return pickle.load(file)


model = load_model()


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🩺 Health Prediction AI</h1>
    <p>
        Intelligent health cost prediction powered by Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# MODEL CHECK
# ---------------------------------------------------------
if model is None:

    st.error(
        "⚠️ Model file not found. Please make sure `xgboost.pkl` "
        "is present in the same folder as `app.py`."
    )

    st.stop()


# ---------------------------------------------------------
# INTRODUCTION
# ---------------------------------------------------------
st.markdown("""
<div class="card">
    <div class="card-title">✨ Enter Patient Information</div>
    <div class="card-subtitle">
        Provide the required details below to generate a prediction.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card-title">👤 Personal Information</div>
    """, unsafe_allow_html=True)

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )


with col2:

    st.markdown("""
    <div class="card-title">🏥 Health Information</div>
    """, unsafe_allow_html=True)

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )

    smoker = st.selectbox(
        "Smoking Status",
        ["No", "Yes"]
    )

    region = st.selectbox(
        "Region",
        ["Southwest", "Southeast", "Northwest", "Northeast"]
    )


# ---------------------------------------------------------
# ENCODING
# ---------------------------------------------------------
sex_encoded = {
    "Female": 0,
    "Male": 1
}

smoker_encoded = {
    "No": 0,
    "Yes": 1
}

region_encoded = {
    "Southwest": 0,
    "Southeast": 1,
    "Northwest": 2,
    "Northeast": 3
}


# ---------------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])

with predict_col2:

    predict_button = st.button(
        "🔮 Generate Prediction"
    )


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
if predict_button:

    input_data = pd.DataFrame(
        [[
            age,
            sex_encoded[sex],
            bmi,
            children,
            smoker_encoded[smoker],
            region_encoded[region]
        ]],
        columns=[
            "Age",
            "Sex",
            "BMI",
            "Children",
            "Smoker",
            "Region"
        ]
    )

    try:

        prediction = model.predict(input_data)[0]

        st.markdown("""
        <div class="result-card">
            <div class="result-icon">🎯</div>
            <div class="result-title">
                Predicted Health Insurance Cost
            </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="result-value">
                ₹ {prediction:,.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="info-box">
            💡 This prediction is generated using the trained
            XGBoost machine learning model.
        </div>
        </div>
        """, unsafe_allow_html=True)

        # -------------------------------------------------
        # INPUT SUMMARY
        # -------------------------------------------------

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">📋 Prediction Summary</div>
            <div class="card-subtitle">
                Information used by the machine learning model
            </div>
        </div>
        """, unsafe_allow_html=True)

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:
            st.metric("Age", f"{age} years")
            st.metric("BMI", f"{bmi:.1f}")

        with summary_col2:
            st.metric("Children", children)
            st.metric("Smoking", smoker)

        with summary_col3:
            st.metric("Sex", sex)
            st.metric("Region", region)

    except Exception as e:

        st.error(
            f"Prediction failed. Please check the model and input format.\n\n"
            f"Error: {e}"
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    <b>Health Prediction AI</b> • Powered by XGBoost & Streamlit<br>
    Machine Learning Prediction System
</div>
""", unsafe_allow_html=True)
