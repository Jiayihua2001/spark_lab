# spark_lab_gemini.py
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from streamlit_lottie import st_lottie
import requests
# Load API key
load_dotenv()
# 🔑 Set your API key
genai.configure(api_key="AIzaSyBagJYw1qV3L3FX1HINbWit4WHGgyPXhjI")

st.title("✨ 灵感实验室 - Spark Lab (Gemini Edition)")
st.write("Tell me your mood, and I'll spark a creative idea just for you!")

mood = st.selectbox("How are you feeling today?", ["happy", "anxious", "curious", "lonely", "tired", "excited"])

url = "https://assets2.lottiefiles.com/packages/lf20_tll0j4bb.json"
animation = requests.get(url).json()
st_lottie(animation, height=200)

if st.button("Give me inspiration ✨"):
    try:
        prompt = f"""
        You are a warm-hearted creativity guide. When someone tells you they are feeling {mood}, 
        gently offer a short, inspiring activity or idea to spark their imagination. 
        Make it poetic, meaningful, and practical. Only 1-2 sentences.
        """

        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)

        st.success(response.text.strip())

    except Exception as e:
        st.error(f"Something went wrong: {e}")
