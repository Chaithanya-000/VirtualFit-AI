
# VirtualFit AI

AI-Powered Virtual Try-On System

## Overview
VirtualFit AI is a web application that allows users
to upload a person image and a garment image and
generate a virtual try-on result using the pretrained
IDM-VTON model through its hosted Gradio interface.

## Technologies
- Python
- Streamlit
- Pillow
- Gradio Client
- IDM-VTON pretrained model

## Setup
1. Install Python.
2. Create and activate a virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Start the application:

   streamlit run app.py

5. Open http://localhost:8501

## Limitations
- Requires internet access to reach the hosted model.
- Generation depends on the availability of the remote service.
- Output quality depends on the input images and model.
- This prototype does not guarantee accurate clothing fit or sizing.

## Privacy
Uploaded images are sent to the hosted inference service.
Do not upload sensitive or private photographs without
appropriate permission.
