# ⚡️ RPS Images⚡️

## Overview Problems
Masalah yang ditemukan dari project ini yaitu bagaimana cara membuat model dengan akurasi yang baik dari dataset RPS yang telah diberikan.

![image 1](Images/Gambar-tiap-kelas.png)

## Overview Dataset
Dataset ini sudah tersedia pada link google drive yang dibagikan kepada praktikan, dataset dibagi menjadi 85% training, 15% validation.<br>link url untuk download dataset: https://drive.google.com/drive/folders/16ugqhXnjkhJS6xmP3D_PA2_Mj-nTHQdD?usp=drive_link

## Preprocessing and Modeling
Pada bagian preprocessing data di rescale 1/255 lalu rotasi, zoom, shear, shift dengan masing-masing 20%, random flip

Untuk model kami menggunakan model _MobileNetV2_ dan ini adalah ilustrasi bagaimana _MobileNetV2_ bekerja

![image 2](Images/Mobilenetv2-architecture.png)

Summary Model:

![image 3](Images/Summary.png)

Graph accuracy dan loss model:

![image 4](Images/Acc&Loss-Graph.png)

Classifcation Report Model:

![image 5](Images/Classification-Report.png)

## Prediction and Deployment

Prediksi yang diambil yaitu 10 gambar acak dari testing dan melihat bagaimana model dapat memprediksi gambar dengan baik, berikut ini adalah hasilnya:

![image 6](Images/Predict.png)

Deployment ini menggunakan streamlit dan dapat dilihat sebagai berikut :

![image 7](Images/Tampilan.png)

![image 8](Images/Hasil-prediksi.png)
