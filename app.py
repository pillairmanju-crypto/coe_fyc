import streamlit as st
from PIL import Image
import numpy as np
from transformers import pipeline
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.title("Image Analyzer")

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image)

    width, height = image.size

    image_array = np.array(image)

    avg_color = image_array.mean(axis=(0, 1))

    r = int(avg_color[0])
    g = int(avg_color[1])
    b = int(avg_color[2])

    prediction = classifier(image)[0]

    label = prediction["label"]

    confidence = round(prediction["score"] * 100, 2)

    if r > g and r > b:
        color_name = "Red"

    elif g > r and g > b:
        color_name = "Green"

    elif b > r and b > g:
        color_name = "Blue"

    else:
        color_name = "Mixed"

    st.write("Detected Object:", label)

    st.write("Confidence:", confidence, "%")

    st.write("Width:", width)

    st.write("Height:", height)

    st.write("Dominant Color:", color_name)

    st.write("RGB:", r, g, b)

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(pdf_buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("Image Analysis Report", styles["Title"])
    )

    content.append(
        Paragraph(f"Detected Object: {label}", styles["BodyText"])
    )

    content.append(
        Paragraph(f"Confidence: {confidence}%", styles["BodyText"])
    )

    content.append(
        Paragraph(f"Width: {width}", styles["BodyText"])
    )

    content.append(
        Paragraph(f"Height: {height}", styles["BodyText"])
    )

    content.append(
        Paragraph(f"Dominant Color: {color_name}", styles["BodyText"])
    )

    content.append(
        Paragraph(f"RGB: {r}, {g}, {b}", styles["BodyText"])
    )

    doc.build(content)

    pdf_buffer.seek(0)

    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name="report.pdf",
        mime="application/pdf"
    )
