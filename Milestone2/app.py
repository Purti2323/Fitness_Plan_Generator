import streamlit as st
from model_api import query_model
from prompt_builder import build_prompt

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="FitPlan AI",
    page_icon="💪",
    layout="wide"
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("💪 FitPlan AI")

page = st.sidebar.radio(
    "Navigation",
    ["Fitness Form", "BMI Result", "AI Workout Plan"]
)

# -----------------------------------
# PAGE 1 FORM
# -----------------------------------

if page == "Fitness Form":

    st.title("Fitness Profile")

    name = st.text_input("Name")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
    "Enter your age", 
    min_value=10, 
    max_value=60, 
    value=25, 
    step=1
    )
    
    height = st.number_input("Height (cm)", min_value=0.0)

    weight = st.number_input("Weight (kg)", min_value=0.0)

    goal = st.selectbox(
        "Goal",
        ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
    )

    fitness_level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    equipment = st.multiselect(
        "Equipment",
        ["Dumbbells", "Yoga Mat", "Resistance Band", "None"]
    )

    if st.button("Submit"):

        if name == "" or height == 0 or weight == 0:

            st.error("Fill all fields")

        else:

            prompt, bmi, bmi_status = build_prompt(
                name,
                gender,
                age,
                height,
                weight,
                goal,
                fitness_level,
                equipment
            )

            st.session_state.prompt = prompt
            st.session_state.bmi = bmi
            st.session_state.bmi_status = bmi_status
            st.session_state.name = name

            st.success("Submitted")

# -----------------------------------
# PAGE 2 BMI RESULT
# -----------------------------------

elif page == "BMI Result":

    if "bmi" not in st.session_state:

        st.warning("Fill form first")

    else:

        st.write("Name:", st.session_state.name)

        st.write("BMI:", round(st.session_state.bmi, 2))

        st.write("Category:", st.session_state.bmi_status)


# -----------------------------------
# PAGE 3 AI WORKOUT PLAN
# -----------------------------------

elif page == "AI Workout Plan":

    st.title("AI Generated Workout Plan")

    if "prompt" not in st.session_state:

        st.warning("Fill form first")

    else:

        if st.button("Generate Plan"):

            with st.spinner("Generating..."):

                result = query_model(
                    st.session_state.prompt
                )

                st.write(result)
