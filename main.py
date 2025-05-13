import streamlit as st
from helper_func import get_gemini_response
import json
import re # Added for more robust JSON extraction

st.set_page_config(
    page_title="Health Calculator",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Health Calculator")
st.write("This is a simple health calculator that provides information about your calorie intake and expenditure.")
st.write("You can use this calculator to track your daily calorie intake and expenditure, and to get an estimate of your body mass index (BMI).")
st.write("Please enter your details below:")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Insert your age", min_value=0, max_value=120, value=25, step=1)
    st.write("The current age is ", age)

with col2:
    height = st.number_input("Insert your height in cm", min_value=0.0, max_value=300.0, value=170.0, step=0.1)
    st.write("The current height is ", height)

with col3:
    weight = st.number_input("Insert your weight in kg", min_value=0.0, max_value=300.0, value=70.0, step=0.1)
    st.write("The current weight is ", weight)

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox(
        "Select your gender",
        options=["Male", "Female"]
    )
    st.write("The current gender is ", gender)  

with col2:
    diet_type = st.selectbox(
        "Select your diet type",
        options=["Vegetarian", "Non-Vegetarian"]
    )
    st.write("The current diet type is ", diet_type)


prompt = f'''Age:{age}
Height: {height}
Weight: {weight}
Gender: {gender}
Diet Type : {diet_type}
Based on this information, do the following in clearly sectioned format:
1. Health Summary
Mention the BMI category (e.g., underweight, normal, overweight, obese) without showing the formula or calculation.
Briefly describe what that BMI category means in terms of general health.
2. Recommended Daily Calorie Intake
Provide an estimated daily calorie range for maintaining a healthy weight.
Mention if adjustments should be made for weight loss or gain.
3. Diet Recommendations
Suggest healthy eating habits and food groups to focus on.
Include a sample meal plan (breakfast, lunch, dinner, 2 snacks).
Consider the person’s age and gender when giving suggestions.
make a JSON of it
but it should be in the format
{{
  "health_summary": {{
    "bmi_category": "",
    "description": ""
  }},
  "recommended_daily_calorie_intake": {{
    "calories_intake_range": ""
  }},
  "diet_recommendations": {{
    "healthy_habits_and_food_groups": [],
    "sample_meal_plan": {{
      "breakfast": "",
      "snack1": "",
      "lunch": "",
      "snack2": "",
      "dinner": ""
    }}
  }}
}}
'''

# Track parameters in session state
params = {
    "age": age,
    "height": height,
    "weight": weight,
    "gender": gender, 
    "diet_type": diet_type
}

if "last_params" not in st.session_state:
    st.session_state["last_params"] = params
elif st.session_state["last_params"] != params:
    # If any parameter changed, clear the response and update params
    st.session_state.pop("health_response", None)
    st.session_state["last_params"] = params

# Center the "Get Health Summary" button
button_col1, button_col2, button_col3 = st.columns([1,2,1])

# Add vertical space before the button
st.write("")
st.write("")

# Center the "Get Health Summary" button with better column ratios
button_col1, button_col2, button_col3 = st.columns([2, 1, 2])
with button_col2:
    get_summary_clicked = st.button("Calculated Health Summary")

if get_summary_clicked:
    with st.spinner("Generating response..."):
        print("Prompt:", prompt)
        response = get_gemini_response(prompt)
        st.success("Response generated successfully!")
        # Clean up response as before
        response = response[7:]
        tick = response[-1]
        while(tick != '}'):
            response = response[:-1]
            tick = response[-1]
        response = json.loads(response)
        st.session_state['health_response'] = response  # Store in session_state

# Only show the three buttons if the response exists
if 'health_response' in st.session_state:
    response = st.session_state['health_response']
    col1, col2, col3  = st.columns(3, gap="medium")
    with col1:
        submit1 = st.button("Get BMI Summary")
    with col2:
        submit2 = st.button("Get Recommended Daily Calorie Intake")
    with col3:
        submit3 = st.button("Get Diet Recommendations")

    if submit1:
        st.subheader("BMI Summary")
        st.write(f"BMI Category: {response['health_summary']['bmi_category']}")
        st.write(f"Description: {response['health_summary']['description']}")
    if submit2:
        st.subheader("Recommended Daily Calorie Intake")
        st.write(f"Calories Intake Range: {response['recommended_daily_calorie_intake']['calories_intake_range']}")
    if submit3:
        st.subheader("Diet Recommendations")
        st.write(f"Healthy Habits and Food Groups: {', '.join(response['diet_recommendations']['healthy_habits_and_food_groups'])}")
        st.write("Sample Meal Plan:")
        st.write(f"Breakfast: {response['diet_recommendations']['sample_meal_plan']['breakfast']}")
        st.write(f"Snack 1: {response['diet_recommendations']['sample_meal_plan']['snack1']}")
        st.write(f"Lunch: {response['diet_recommendations']['sample_meal_plan']['lunch']}")
        st.write(f"Snack 2: {response['diet_recommendations']['sample_meal_plan']['snack2']}")
        st.write(f"Dinner: {response['diet_recommendations']['sample_meal_plan']['dinner']}")