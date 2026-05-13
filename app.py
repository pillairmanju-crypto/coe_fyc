import streamlit as st
import face_recognition
import numpy as np
from PIL import Image
import os

st.title("Celebrity Face Detector")

known_face_encodings = []
known_face_names = []

celebrity_folder = "celebrities"

for filename in os.listdir(celebrity_folder):

    if filename.endswith(".jpg") or filename.endswith(".png"):

        image_path = os.path.join(
            celebrity_folder,
            filename
        )

        image = face_recognition.load_image_file(
            image_path
        )

        encodings = face_recognition.face_encodings(
            image
        )

        if len(encodings) > 0:

            known_face_encodings.append(
                encodings[0]
            )

            name = os.path.splitext(
                filename
            )[0]

            known_face_names.append(name)

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image)

    image_array = np.array(image)

    uploaded_encodings = face_recognition.face_encodings(
        image_array
    )

    if len(uploaded_encodings) > 0:

        uploaded_face = uploaded_encodings[0]

        matches = face_recognition.compare_faces(
            known_face_encodings,
            uploaded_face
        )

        face_distances = face_recognition.face_distance(
            known_face_encodings,
            uploaded_face
        )

        best_match_index = np.argmin(
            face_distances
        )

        if matches[best_match_index]:

            detected_name = known_face_names[
                best_match_index
            ]

            st.success(
                f"Detected Celebrity: {detected_name}"
            )

        else:

            st.warning(
                "No celebrity match found"
            )

    else:

        st.error(
            "No face detected in image"
        )
