import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Connect to Gemini (We will hide the real key later for safety)
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Your App's Interface
st.title("Vision AI 👁️")
st.write("Upload an image and ask me about it!")

# Create an upload button and a text box
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
user_question = st.text_input("What would you like to know about this image?")

# 3. The App's Logic
if uploaded_file is not None:
    # Open the image and show it on the screen
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # If the user asks a question, send BOTH the image and question to Gemini
    if user_question:
        response = model.generate_content([user_question, image])
        st.write(response.text)
