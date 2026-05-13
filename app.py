import streamlit as st
from PIL import Image
from collections import Counter
import numpy as np

st.set_page_config(page_title="AI Image Analyzer")

st.title("AI Image Analyzer")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    width, height = image.size

    st.subheader("Image Details")

    st.write("Width:", width)
    st.write("Height:", height)
    st.write("Image Mode:", image.mode)
    st.write("Image Format:", image.format)

    rgb_image = image.convert("RGB")

    image_array = np.array(rgb_image)

    pixels = image_array.reshape(-1, 3)

    avg_color = pixels.mean(axis=0)

    r = int(avg_color[0])
    g = int(avg_color[1])
    b = int(avg_color[2])

    st.subheader("Average Color")

    st.write("Red:", r)
    st.write("Green:", g)
    st.write("Blue:", b)

    def detect_main_color(r, g, b):

        if r > g and r > b:
            return "Mostly Red"

        elif g > r and g > b:
            return "Mostly Green"

        elif b > r and b > g:
            return "Mostly Blue"

        elif r > 180 and g > 180 and b > 180:
            return "Mostly White / Bright"

        elif r < 70 and g < 70 and b < 70:
            return "Mostly Black / Dark"

        else:
            return "Mixed Colors"

    main_color = detect_main_color(r, g, b)

    st.write("Dominant Appearance:", main_color)

    st.subheader("Estimated Objects")

    gray = rgb_image.convert("L")

    gray_array = np.array(gray)

    bright_pixels = np.sum(gray_array > 200)
    medium_pixels = np.sum((gray_array > 80) & (gray_array <= 200))
    dark_pixels = np.sum(gray_array <= 80)

    st.write("Bright Areas:", int(bright_pixels))
    st.write("Medium Areas:", int(medium_pixels))
    st.write("Dark Areas:", int(dark_pixels))

    st.subheader("Image Summary")

    st.write(
        "This image is",
        width,
        "x",
        height,
        "pixels with dominant color:",
        main_color
    )
