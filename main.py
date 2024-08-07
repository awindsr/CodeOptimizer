import streamlit as st
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import pathway as pw

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

# Set Streamlit configuration
st.set_page_config(page_title="Code Optimizer", page_icon="💻")
st.title("Code Optimizer")
st.write("Welcome to Code Optimizer! This app helps you improve your code by providing best coding practices and optimization tips.")

# Prompt templates
context = """You are an expert code reviewer. When provided with a piece of code, you will analyze it and offer suggestions to improve its efficiency, readability, and adherence to best coding practices. The feedback should include specific recommendations, code examples, and explanations.

Example:
User code:
def add(a, b):
return a + b

Feedback:
1. Use type hints for better readability:
def add(a: int, b: int) -> int:
    return a + b

2. Ensure proper indentation and consistent spacing:
def add(a: int, b: int) -> int:
    return a + b

3. Add a docstring to explain the function's purpose:
def add(a: int, b: int) -> int:
    \"\"\"Returns the sum of a and b.\"\"\"
    return a + b

Provide similar feedback for the code given by the user."""

# Input text area for user code
user_code = st.text_area("Enter your code here:", key="input", placeholder="Input your code here")

# Function to get recommendations
def get_recommendations(code):
    prompt = context + "\n\nUser code:\n" + code
    response = model.invoke(prompt)
    return response.content

# Function to convert feedback to JSON using Pathway
def get_json(content):
    prompt = """Please convert the given content into a JSON object with keys as numbers and each key containing the recommendation details such as 'Description', 'Example', and 'Explanation'. Follow this example:

{
    "1": {
        "Description": "Use type hints for better readability",
        "Example": "def add(a: int, b: int) -> int: return a + b",
        "Explanation": "Type hints improve code readability and help catch errors during development."
    },
    "2": {
        "Description": "Ensure proper indentation and consistent spacing",
        "Example": "def add(a: int, b: int) -> int: return a + b",
        "Explanation": "Consistent spacing and indentation enhance code readability."
    }
}

Here is the content:
"""
    response = model.invoke(prompt + content)
    return response.content

# Define Pathway schema for JSON data
class RecommendationSchema(pw.Schema):
    Description: str
    Example: str
    Explanation: str

# Button to get recommendations and convert to JSON using Pathway
if st.button("Get Recommendations"):
    feedback = get_recommendations(user_code)
    st.write("### Feedback")
    st.write(feedback)

    json_feedback = get_json(feedback)
    try:
        json_data = json.loads(json_feedback)
        st.write("### JSON Feedback")
        st.json(json_data)

        # Convert JSON data to Pathway table
        recommendations = [RecommendationSchema(**v) for v in json_data.values()]
        table = pw.Table(recommendations)
        
        # Save the table as JSON Lines format
        pw.io.jsonlines.write(table, "recommendations.jsonl")
        st.write("The recommendations have been saved as 'recommendations.jsonl'.")
    except json.JSONDecodeError as e:
        st.write("### Error in JSON conversion")
        st.write(json_feedback)

    st.write("This app is created to help developers improve their code by following best practices and optimization techniques.")
    st.markdown("Made with ❤️ by awindsr (https://awindsr.codes)")
