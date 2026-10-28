
# VirtualFit AI — Technical Report

## 1. Project Overview
VirtualFit AI is a web application that generates a
virtual clothing try-on preview from a person image
and a garment image.

## 2. Problem Statement
Online shoppers may find it difficult to visualize
how clothing could look before purchasing it.

## 3. Objectives
- Accept person and garment images.
- Generate a virtual try-on result using AI.
- Display and download the generated image.
- Provide a simple web interface.

## 4. Technologies Used
- Python
- Streamlit
- Pillow
- Gradio Client
- IDM-VTON pretrained model
- Streamlit Community Cloud

## 5. System Workflow
The user uploads a person image and a garment image.
The application sends the prepared inputs to the hosted
IDM-VTON inference service through Gradio Client.
The returned generated image is displayed to the user.

## 6. Testing
The application launch and model connection were tested.
Record the actual test inputs, results and errors here.
Include screenshots of successful runs.

## 7. Challenges
- Connecting the application to a hosted AI service.
- Handling image inputs and returned results.
- Depending on remote service availability.

## 8. Limitations
- Requires internet access.
- Depends on the hosted model remaining available.
- Generated clothing may not accurately represent fit,
  size, fabric behavior or real-world appearance.
- Uploaded images are sent to a third-party service.

## 9. Future Improvements
- Better input validation and error messages.
- Additional garment categories.
- Automated tests and performance measurements.
- Improved privacy controls.

## 10. Model and Library References
IDM-VTON:
https://github.com/yisol/IDM-VTON

Streamlit:
https://streamlit.io/

Pillow:
https://python-pillow.org/

Gradio:
https://www.gradio.app/

Review the relevant licenses before redistribution
or commercial use.

## 11. Conclusion
VirtualFit AI demonstrates a prototype that connects
a web interface to a pretrained virtual try-on model.
