import streamlit as st
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import tempfile

st.set_page_config(page_title="Black and White PDF Converter")

st.title("Black and White Image to PDF Converter")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    bw_image = image.convert("L")

    st.image(bw_image, caption="Black and White Preview")

    temp_image = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    bw_image.save(temp_image.name)

    pdf_buffer = BytesIO()

    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)

    pdf.drawImage(
        temp_image.name,
        50,
        200,
        width=500,
        preserveAspectRatio=True
    )

    pdf.save()

    pdf_buffer.seek(0)

    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name="black_white_image.pdf",
        mime="application/pdf"
    )
