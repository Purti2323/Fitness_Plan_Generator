import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="FitPlan AI",
    page_icon="💪",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS (Modern UI)
# -----------------------------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}
.card {
    background-color: #1C1F26;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.4);
}
.stButton>button {
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    color: white;
    border-radius: 8px;
    height: 3em;
    font-weight: 600;
    width: 100%;
}
.result-card {
    background-color: #111827;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------
st.sidebar.title("💪 FitPlan AI")
page = st.sidebar.radio("Navigate", ["🏠 Fitness Form", "📊 BMI Result"])

# -----------------------------------
# PAGE 1: FITNESS FORM
# -----------------------------------
if page == "🏠 Fitness Form":

    st.markdown("<div class='title'>FitPlan AI</div>", unsafe_allow_html=True)
    st.write("### Milestone 1: Fitness Profile & BMI Calculator")
    st.write("")

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name (Required)")

    with col2:
        fitness_level = st.selectbox(
            "Fitness Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

    height_cm = st.number_input("Height in centimeters (Required)", min_value=0.0)
    weight_kg = st.number_input("Weight in kilograms (Required)", min_value=0.0)

    st.subheader("🏋️ Fitness Details")

    goal = st.selectbox(
        "Fitness Goal",
        ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
    )

    equipment = st.multiselect(
        "Available Equipment (Multiple Selection Allowed)",
        ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment"]
    )

    submit = st.button("Calculate BMI")

    st.markdown("</div>", unsafe_allow_html=True)

    if submit:

        # Validation
        if not name.strip():
            st.error("Name is required.")
        elif height_cm <= 0:
            st.error("Height must be greater than zero.")
        elif weight_kg <= 0:
            st.error("Weight must be greater than zero.")
        else:
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)
            bmi = round(bmi, 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"

            # Save in session
            st.session_state["name"] = name
            st.session_state["bmi"] = bmi
            st.session_state["category"] = category

            st.success("BMI Calculated! Go to 'BMI Result' page.")

# -----------------------------------
# PAGE 2: RESULT PAGE
# -----------------------------------
elif page == "📊 BMI Result":

    st.markdown("<div class='title'>Your BMI Report</div>", unsafe_allow_html=True)
    st.write("")

    if "bmi" not in st.session_state:
        st.warning("Please fill the form first.")
    else:
        st.markdown(f"""
        <div class='result-card'>
            <h2>Hello, {st.session_state['name']} 👋</h2>
            <h1>BMI: {st.session_state['bmi']}</h1>
            <h3>Category: {st.session_state['category']}</h3>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()
