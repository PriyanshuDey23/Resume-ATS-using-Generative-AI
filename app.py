from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import tempfile
import fitz
import io
# Import from prompt.py
from prompt import *


# Load environment variables from .env file
load_dotenv()

# Set up the API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the Gemini model
def get_gemini_response(input,image_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    response = model.generate_content([input, image_content[0], prompt])
    return response.text

# Function to convert image to bytes(The function reads the uploaded file, converts it into bytes, )
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        image_bytes = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": image_bytes}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Function to process PDF files to bytes format (This function is useful for converting PDF pages into images (10 pages) )
def process_pdf(uploaded_file):
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(uploaded_file.read())
            temp_pdf_path = temp_pdf.name

        pdf_document = fitz.open(temp_pdf_path)
        num_pages = pdf_document.page_count
        max_pages = min(10, num_pages)

        pdf_images = []
        for page_num in range(max_pages):
            page = pdf_document[page_num]
            pix = page.get_pixmap()  # Render page to an image
            img = Image.open(io.BytesIO(pix.tobytes("png")))  # Convert to PIL Image for display
            pdf_images.append(img)
        
        pdf_document.close()
        return pdf_images, f"Displayed {max_pages} page(s) from the PDF."
    

# Initialize the Streamlit app
st.set_page_config(page_title="ATS RESUME EXPERT")
st.header(" ATS TRACKING SYSTEM")

# Input Prompt for the user
input_text = st.text_area("Job Description", key="input")

# File uploader for images and PDFs
uploaded_file = st.file_uploader("Upload an Resume file...", type=["jpg", "jpeg", "png", "pdf"])

# Initialize variable for storing image and text content
image = None
content_text = ""

if uploaded_file is not None:
    st.write("File Uploaded Successfully")
    # Process the file based on its type
    if uploaded_file.type == "application/pdf":
        pdf_images, content_text = process_pdf(uploaded_file)
        # Display the image
        for img in pdf_images:
            st.image(img, caption="Page Image from PDF", use_column_width=True)

    elif uploaded_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(uploaded_file)
        # Display the imge
        st.image(image, caption="Uploaded Image", use_column_width=True)
        content_text = "Image content displayed."


# Button to trigger processing and generate response
submit1=st.button("Tell me About the resume")
submit2=st.button("How can i improvise my skills")
submit3=st.button("What are the keywords that are missing")
submit4=st.button("Percentage Match")

    
    

# Submit
if submit1:
    if uploaded_file is not None and input_text:
        # Prepare image data for the model
        image_data = input_image_setup(uploaded_file)
        response=get_gemini_response(input=input_text,image_content=image_data,prompt=PROMPT1)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload resume")

elif submit2:
    if uploaded_file is not None and input_text:
        # Prepare image data for the model
        image_data = input_image_setup(uploaded_file)
        response=get_gemini_response(input=input_text,image_content=image_data,prompt=PROMPT2)
        st.subheader("The Response is ")
        st.write(response)

elif submit3:
    if uploaded_file is not None and input_text:
        # Prepare image data for the model
        image_data = input_image_setup(uploaded_file)
        response=get_gemini_response(input=input_text,image_content=image_data,prompt=PROMPT3)
        st.subheader("The Response is ")
        st.write(response)

elif submit4:
    if uploaded_file is not None and input_text:
        # Prepare image data for the model
        image_data = input_image_setup(uploaded_file)
        response=get_gemini_response(input=input_text,image_content=image_data,prompt=PROMPT4)
        st.subheader("The Response is ")
        st.write(response)



    








