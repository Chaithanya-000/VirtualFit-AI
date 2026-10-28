
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


## 6. Testing and Evidence

The application was tested locally and deployed using
Streamlit Community Cloud.

- Application launch: Successful
- Hosted IDM-VTON connection: Tested successfully
- Virtual try-on generation: Successful in the tested run
- Live deployment: Working

### Screenshots

1. `screenshots/01-app-interface.png` — Main application interface.
2. `screenshots/02-uploaded-images.png` — Uploaded person and garment images.
3. `screenshots/03-generated-result.png` — Generated virtual try-on result.

### Live Demo

https://virtualfit-ai-dgygyygpff6yveh8nyargt.streamlit.app/

Formal automated tests and performance benchmarks have
not yet been implemented.


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

## 10. AI Model, API, Datasets and Libraries

### AI Model
- IDM-VTON pretrained virtual try-on model.
- Official repository: https://github.com/yisol/IDM-VTON
- The model is accessed through a hosted inference service.
- The application does not train or fine-tune the model.

### API / Inference Service
- Gradio Client connects to the public `yisol/IDM-VTON`
  Gradio Space.
- Inference endpoint used: `/tryon`.
- Inputs include a person image, garment image and
  garment description.
- Output: generated virtual try-on image.

### Datasets
- No training dataset is downloaded, packaged or used
  directly by this application.
- Person and garment images are supplied by the user
  for inference.

### Third-Party Libraries and Services
- Streamlit — web application interface.
- Pillow — image loading, conversion and saving.
- Gradio Client — communication with the hosted model.
- Streamlit Community Cloud — application deployment.
- Python standard library — temporary files and image buffers.

### Licensing and Attribution
The IDM-VTON repository states that its code and checkpoints
are licensed under CC BY-NC-SA 4.0. Review the applicable
license conditions before redistribution or commercial use.

This project integrates a pretrained third-party model and
does not claim ownership of that model.

## 11. Conclusion
VirtualFit AI demonstrates a prototype that connects
a web interface to a pretrained virtual try-on model.
