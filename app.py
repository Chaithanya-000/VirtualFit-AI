
import os
import tempfile

import streamlit as st
from PIL import Image
from gradio_client import Client, handle_file

st.set_page_config(
    page_title="VirtualFit AI",
    page_icon="👕",
    layout="wide",
)

st.title("VirtualFit AI")
st.write("AI-powered virtual clothing try-on")

person_col, garment_col = st.columns(2)

with person_col:
    st.subheader("1. Person image")
    person_file = st.file_uploader(
        "Upload a front-facing person photo",
        type=["jpg", "jpeg", "png"],
        key="person",
    )
    if person_file:
        st.image(
            person_file,
            caption="Person preview",
            width="stretch",
        )

with garment_col:
    st.subheader("2. Garment image")
    garment_file = st.file_uploader(
        "Upload a garment photo",
        type=["jpg", "jpeg", "png"],
        key="garment",
    )
    if garment_file:
        st.image(
            garment_file,
            caption="Garment preview",
            width="stretch",
        )

garment_description = st.text_input(
    "Describe the garment",
    placeholder="For example: black short-sleeve T-shirt",
)

if st.button("Generate AI Try-On", type="primary"):
    if not person_file or not garment_file:
        st.error("Please upload both images.")
    elif not garment_description.strip():
        st.error("Please enter a garment description.")
    else:
        try:
            with st.spinner(
                "Generating your try-on image. This may take a few minutes..."
            ):
                with tempfile.TemporaryDirectory() as temp_dir:
                    person_path = os.path.join(temp_dir, "person.png")
                    garment_path = os.path.join(temp_dir, "garment.png")

                    person_image = Image.open(person_file).convert("RGB")
                    garment_image = Image.open(garment_file).convert("RGB")

                    person_image.save(person_path)
                    garment_image.save(garment_path)

                    client = Client("yisol/IDM-VTON")

                    result = client.predict(
                        {
                            "background": handle_file(person_path),
                            "layers": [],
                            "composite": handle_file(person_path),
                        },
                        handle_file(garment_path),
                        garment_description.strip(),
                        True,
                        False,
                        30,
                        42,
                        api_name="/tryon",
                    )

                    output_path = result[0]

                    if not output_path or not os.path.exists(output_path):
                        raise RuntimeError(
                            "The AI service returned no usable output image."
                        )

                    generated_image = Image.open(output_path).convert("RGB")
                    generated_image.load()

                st.subheader("Generated result")
                st.image(
                    generated_image,
                    caption="AI-generated virtual try-on",
                    width="stretch",
                )

                from io import BytesIO

                buffer = BytesIO()
                generated_image.save(buffer, format="PNG")

                st.download_button(
                    "Download result",
                    data=buffer.getvalue(),
                    file_name="virtualfit_result.png",
                    mime="image/png",
                )

        except Exception as error:
            st.error(
                "Try-on generation failed. The hosted AI service may be "
                "busy or unavailable."
            )
            st.code(str(error))
            st.info(
                "Check the error details before retrying. "
                "Do not upload private photographs to an untrusted service."
            )
