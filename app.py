import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from PIL import Image
import textwrap
import pathlib


#Import the Local Environment
from dotenv import load_dotenv
load_dotenv() #Load the Environment
import os

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

def get_response(user_input, image):
    # Flash can read Images and Extract Information
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!= "":
        response = model.generate_content([user_input, image])
    else:
        response = model.generate_content(image)
    return response.text

#Design the Page
st.header(":red[Image to Text] Application")
user_input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Upload an Image.",type=['jpg','png','jpeg'])
submit = st.button('Submit')


# Display the Image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Uploaded File',use_container_width = True)



# Google Gemini Model and Source the Image extraction
if submit:
    if image is None:
        st.error("Please upload an image before submitting.")
    else:
        response = get_response(user_input, image)
        st.subheader("The Response is:")
        st.write(response)