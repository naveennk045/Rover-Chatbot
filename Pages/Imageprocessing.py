import streamlit as st
import sys
import os
from io import BytesIO

# Add the directory containing Models to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Models.OCR import Extract
from Models.Llama import prompt



# ---------STREAMLIT APP SETUP---------

st.title("📸 Image Text Processing & Analysis")
st.caption("🚀 A Streamlit app to process images and analyze text using the Llama model")

# File uploader

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file into BytesIO
    image = BytesIO(uploaded_file.read())
    
    # Extract text from the uploaded image
    detected_text = Extract(image)
    
    st.write("Detected Text:")
    st.write(detected_text)
    
    # Create a prompt for the Llama model based on the detected text
    prompts = f"""
    We have extracted the following text from an image:

    {detected_text}

    Based on this text, let's have a conversation. Start by sharing your thoughts on the main themes and context of the text. Consider what the primary focus might be.

    Next, think about what type of image this text could have been taken from. Reflect on different possibilities such as a book page, a sign, or a chart.

    Discuss any notable terms or patterns you observe in the text and how these might relate to the content or purpose of the image.

    Summarize the text in a few sentences, highlighting the key messages and overall essence.

    Finally, let's explore any ideas you have on how we could improve the text extraction process for better accuracy or clarity.

    Feel free to elaborate on these points, and let's dive into the details together.
    """

    # Get response from Llama model
    response = prompt(prompts)
    
    st.title("Llama Response")   
    st.write(response)
