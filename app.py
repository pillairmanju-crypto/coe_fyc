# app.py (Streamlit Black & White Image to PDF Converter)


import streamlit as st
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import tempfile

st.set_page_config(page_title="Image to B&W PDF", layout="centered")

st.title("🖼️ Black & White Image to PDF Converter")
st.write("Upload an image, convert it to black & white, and download it as a PDF.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Convert to black & white
    bw_image = image.convert('L')

    st.subheader("Preview")
    st.image(bw_image, caption="Black & White Image", use_container_width=True)

    # Save temporary black & white image
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    bw_image.save(temp_image.name)

    # Create PDF in memory
    pdf_buffer = BytesIO()

    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter

    c.drawImage(temp_image.name, 50, 200, width=500, preserveAspectRatio=True)

    c.save()

    pdf_buffer.seek(0)

    # Download button
    st.download_button(
        label="📥 Download PDF",
        data=pdf_buffer,
        file_name="black_white_image.pdf",
        mime="application/pdf"
    )
```

---

# requirements.txt

```txt
streamlit
pillow
reportlab
```

---

# Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

# Folder Structure

---

# Deploy on GitHub + Streamlit Cloud

## Step 1: Upload to GitHub

Create a GitHub repository and upload:

* app.py
* requirements.txt

---

## Step 2: Deploy on Streamlit Cloud

Open:

```text
https://share.streamlit.io
```

Then:

1. Sign in with GitHub
2. Select your repository
3. Choose app.py
4. Click Deploy

---

# Features

* Upload image
* Convert image to black & white
* Live preview
* Download as PDF
* Streamlit web interface
* Easy GitHub deployment

---

# GitHub README Example

```md
# Black & White Image to PDF Converter

A Streamlit web app that:
- Uploads images
- Converts them to black & white
- Generates downloadable PDF files

## Installation

pip install -r requirements.txt

## Run

streamlit run app.py
```

