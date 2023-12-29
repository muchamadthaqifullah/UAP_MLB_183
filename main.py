import os
import time

import cv2
import numpy as np
from keras.models import load_model
import streamlit as st
from PIL import Image


def is_image(file):
    return file.type.startswith('image/')


def predict_rps(img_path):
    model = load_model('rps.h5')

    temp_img = Image.open(img_path)
    img = cv2.cvtColor(np.array(temp_img), cv2.COLOR_BGR2RGB)
    img = np.expand_dims(
        cv2.resize(
            img, model.layers[0].input_shape[0][1:3]
            if not model.layers[0].input_shape[1:3]
            else model.layers[0].input_shape[1:3]
        ).astype('float32') / 255,
        axis=0
    )

    start = time.time()
    prediction = model.predict(img)
    labels = np.argmax(prediction).astype(np.int32)
    runtime = round(time.time() - start, 4)
    class_list = {'paper': 0, 'rock': 1, 'scissors': 2}

    response = {
        'label': list(class_list.keys())[labels],
        'time': runtime,
        'image': temp_img,
        'accuracy': round(prediction.max() * 100, 2)
    }

    return response


def save_uploaded_file(uploaded_file, folder="."):
    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder, 'images.png')
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return filepath


if __name__ == '__main__':
    st.title("Ujian Akhir Praktikum")
    final_response = None
    with st.sidebar:
        st.title('Select Models')

        images = st.file_uploader("Choose Files", type=['jpg', 'png', 'jpeg'])
        file_path = None

        if images is not None:
            if is_image(images):
                file_path = save_uploaded_file(images, folder='uploads')
                st.info(f"File saved to: {file_path}")
            else:
                st.warning("Please upload a valid image file.")

        if st.button('Submit'):
            if file_path is not None:
                final_response = predict_rps(file_path)

            else:
                st.warning("Please upload Images")

    if final_response is not None:
        st.title("RPS Prediction")
        st.image(final_response['image'], caption=f'the prediction result is {final_response["label"]}', width=300)
        st.info(f'Accuracy: {final_response["accuracy"]} % | Prediction time: {final_response["time"]} Second')