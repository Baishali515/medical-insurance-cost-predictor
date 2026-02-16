import streamlit as st
import pickle
import base64
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Medical Insurance Predictor",
    page_icon="💊",
    layout="centered"
)

# ---------------- LOAD MODEL WITH CACHE ----------------
@st.cache_resource
def load_model():
    try:
        with open("model/final_insurance_model.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("Model file not found. Please check model folder.")
        return None

model = load_model()

# ---------------- CUSTOM CSS (WHITE + BLUE PREMIUM THEME) ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    background-attachment: fixed;
}

/* Main Container */
.block-container {
    background: rgba(255, 255, 255, 0.95);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

/* Title */
h1 {
    color: #0d47a1 !important;
    text-align: center;
    font-weight: 700;
}

/* Subheading */
h3 {
    color: #1565c0 !important;
    text-align: center;
}

/* Labels */
label {
    color: #0d47a1 !important;
    font-weight: 500;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #1565c0, #42a5f5);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
}

.stButton>button:hover {
    background: linear-gradient(45deg, #0d47a1, #1976d2);
    transform: scale(1.02);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #e3f2fd;
}

/* Sidebar Text Color */
[data-testid="stSidebar"] * {
    color: black !important;
}
            /* Reduce top padding of sidebar */
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0px;
}
            /* Top Left Fixed Logo */
.top-logo {
    position: fixed;
    top: 5px;   /* ← This is what you wanted to adjust */
    left: 20px;
    z-index: 999;
}



</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="top-logo">
        <img src="logo.png" width="90">
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- SIDEBAR ----------------

# ✅ LOGO ADDED AT TOP LEFT

st.sidebar.markdown(
    "<h2 style='text-align:left; color:#0d47a1;'>📌 About Project</h2>",
    unsafe_allow_html=True
)

st.sidebar.write("""
🔹 This end-to-end Machine Learning project predicts 
medical insurance charges using health & demographic data.

🔹 Built to estimate insurance premiums based on 
risk factors like BMI & smoking.
""")

st.sidebar.markdown(
    "<p style='color:black; font-weight:600;'>👩‍💻 Developed by: Baishali Dash</p>",
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.title("🩺 Medical Insurance Cost Predictor")
st.markdown("### Enter your details to estimate insurance charges")
st.divider()

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 25)
    bmi = st.slider("BMI", 10.0, 50.0, 25.0)
    children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox(
        "Region",
        ["northwest", "southeast", "southwest", "northeast"]
    )

# ---------------- DATA PREPARATION ----------------
input_data = {
    "age": age,
    "bmi": bmi,
    "children": children,
    "sex_male": 1 if sex == "male" else 0,
    "smoker_yes": 1 if smoker == "yes" else 0,
    "region_northwest": 1 if region == "northwest" else 0,
    "region_southeast": 1 if region == "southeast" else 0,
    "region_southwest": 1 if region == "southwest" else 0
}

input_df = pd.DataFrame([input_data])

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Insurance Cost") and model is not None:

    with st.spinner("Calculating insurance cost..."):
        prediction = model.predict(input_df)[0]

    st.markdown(f"""
    <div style="
        background: linear-gradient(45deg, #1565c0, #42a5f5);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: black;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
        💰 Estimated Insurance Cost <br><br>
        ₹ {prediction:,.2f}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction > 20000:
        st.error("⚠ High Risk Category")
    elif prediction > 10000:
        st.warning("⚠ Moderate Risk Category")
    else:
        st.success("✅ Low Risk Category")

        


st.divider()
st.caption("© 2026 Baishali Dash | Built using Streamlit & Machine Learning")
import streamlit as st
import pickle
import base64
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Medical Insurance Predictor",
    page_icon="💊",
    layout="centered"
)

# ---------------- LOAD MODEL WITH CACHE ----------------
@st.cache_resource
def load_model():
    try:
        with open("model/final_insurance_model.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("Model file not found. Please check model folder.")
        return None

model = load_model()

# ---------------- CUSTOM CSS (WHITE + BLUE PREMIUM THEME) ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    background-attachment: fixed;
}

/* Main Container */
.block-container {
    background: rgba(255, 255, 255, 0.95);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

/* Title */
h1 {
    color: #0d47a1 !important;
    text-align: center;
    font-weight: 700;
}

/* Subheading */
h3 {
    color: #1565c0 !important;
    text-align: center;
}

/* Labels */
label {
    color: #0d47a1 !important;
    font-weight: 500;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #1565c0, #42a5f5);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
}

.stButton>button:hover {
    background: linear-gradient(45deg, #0d47a1, #1976d2);
    transform: scale(1.02);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #e3f2fd;
}

/* Sidebar Text Color */
[data-testid="stSidebar"] * {
    color: black !important;
}
            /* Reduce top padding of sidebar */
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0px;
}
            /* Top Left Fixed Logo */
.top-logo {
    position: fixed;
    top: 5px;   /* ← This is what you wanted to adjust */
    left: 20px;
    z-index: 999;
}



</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="top-logo">
        <img src="logo.png" width="90">
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- SIDEBAR ----------------

# ✅ LOGO ADDED AT TOP LEFT

st.sidebar.markdown(
    "<h2 style='text-align:left; color:#0d47a1;'>📌 About Project</h2>",
    unsafe_allow_html=True
)

st.sidebar.write("""
🔹 This end-to-end Machine Learning project predicts 
medical insurance charges using health & demographic data.

🔹 Built to estimate insurance premiums based on 
risk factors like BMI & smoking.
""")

st.sidebar.markdown(
    "<p style='color:black; font-weight:600;'>👩‍💻 Developed by: Baishali Dash</p>",
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.title("🩺 Medical Insurance Cost Predictor")
st.markdown("### Enter your details to estimate insurance charges")
st.divider()

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 25)
    bmi = st.slider("BMI", 10.0, 50.0, 25.0)
    children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox(
        "Region",
        ["northwest", "southeast", "southwest", "northeast"]
    )

# ---------------- DATA PREPARATION ----------------
input_data = {
    "age": age,
    "bmi": bmi,
    "children": children,
    "sex_male": 1 if sex == "male" else 0,
    "smoker_yes": 1 if smoker == "yes" else 0,
    "region_northwest": 1 if region == "northwest" else 0,
    "region_southeast": 1 if region == "southeast" else 0,
    "region_southwest": 1 if region == "southwest" else 0
}

input_df = pd.DataFrame([input_data])

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Insurance Cost") and model is not None:

    with st.spinner("Calculating insurance cost..."):
        prediction = model.predict(input_df)[0]

    st.markdown(f"""
    <div style="
        background: linear-gradient(45deg, #1565c0, #42a5f5);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: black;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
        💰 Estimated Insurance Cost <br><br>
        ₹ {prediction:,.2f}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction > 20000:
        st.error("⚠ High Risk Category")
    elif prediction > 10000:
        st.warning("⚠ Moderate Risk Category")
    else:
        st.success("✅ Low Risk Category")

        


st.divider()
st.caption("© 2026 Baishali Dash | Built using Streamlit & Machine Learning")