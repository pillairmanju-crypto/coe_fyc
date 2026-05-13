import streamlit as st
from PIL import Image
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.title("Image Analyzer")

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

    if r > g and r > b:
        color_name = "Mostly Red"

    elif g > r and g > b:
        color_name = "Mostly Green"

    elif b > r and b > g:
        color_name = "Mostly Blue"

    else:
        color_name = "Mixed Colors"

    if width > 1000 and height > 1000:
        image_type = "High Resolution Image"

    elif width > height:
        image_type = "Landscape Style Image"

    elif height > width:
        image_type = "Portrait Style Image"

    else:
        image_type = "Square Image"

    st.write("Image Type:", image_type)

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
        Paragraph(f"Image Type: {image_type}", styles["BodyText"])
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
