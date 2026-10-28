
# VirtualFit AI — System Architecture

```text
+------------------------+
|         User           |
+------------------------+
            |
            v
+------------------------+
|  Streamlit Web App     |
|  app.py                |
+------------------------+
            |
            v
+------------------------+
| Image Upload & Input   |
| Person + Garment       |
+------------------------+
            |
            v
+------------------------+
|     Gradio Client      |
+------------------------+
            |
            v
+------------------------+
| Hosted IDM-VTON Model  |
| AI Image Generation    |
+------------------------+
            |
            v
+------------------------+
| Generated Try-On Image |
+------------------------+
            |
            v
+------------------------+
| Preview & Download     |
+------------------------+
```

## Components

- Frontend: Streamlit
- Image processing: Pillow
- Inference client: Gradio Client
- AI model: IDM-VTON
- Hosting: Streamlit Community Cloud
- Inference: Hosted IDM-VTON service
