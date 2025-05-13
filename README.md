# Health Calculator App

## Overview

The **Health Calculator App** is a Streamlit-based web application that provides users with personalized health insights, including BMI summary, recommended daily calorie intake, and diet recommendations. By entering basic health parameters, users receive a structured health summary and actionable dietary advice, all powered by generative AI.

---

## Features

- **BMI Calculation & Summary:**  
  Get your BMI category (e.g., underweight, normal, overweight, obese) and a brief explanation of what it means for your health.

- **Recommended Daily Calorie Intake:**  
  Receive an estimated daily calorie range tailored to your profile, with suggestions for weight maintenance, loss, or gain.

- **Diet Recommendations:**  
  Get healthy eating habits, food group suggestions, and a sample meal plan (breakfast, lunch, dinner, and two snacks) based on your age, gender, and diet type.

- **Interactive UI:**  
  - Input fields for age, height, weight, gender, and diet type.
  - Centered "Calculated Health Summary" button.
  - Additional buttons to view BMI summary, calorie intake, and diet recommendations after calculation.

---

## How It Works

1. **User Input:**  
   Enter your age, height (cm), weight (kg), gender, and diet type.

2. **AI-Powered Analysis:**  
   On clicking "Calculated Health Summary," the app sends your data to a generative AI model (Gemini) to generate a structured health report in JSON format.

3. **Results Display:**  
   After calculation, you can view:
   - BMI summary
   - Recommended daily calorie intake
   - Diet recommendations and sample meal plan

4. **Dynamic Updates:**  
   Changing any input parameter clears previous results, ensuring you always see up-to-date advice.

---

## Setup & Usage

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- Gemini API access (Google Generative AI)
- Required Python packages:  
  - `streamlit`
  - `google-generativeai`
  - `python-dotenv`

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

### Running the App

```bash
streamlit run main.py
```

---

## File Structure

```

HealthCalculatorApp/
 ├── main.py
 ├── helper_func.py
 └── ...
```

---

## Customization

- **Prompt Engineering:**  
  The prompt sent to Gemini can be adjusted in `main.py` to refine the AI's responses.
- **UI Tweaks:**  
  Modify Streamlit layout and styling as needed for your use case.

---

## License

This project is for educational and personal use. Please check the Gemini API terms for commercial usage.

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
