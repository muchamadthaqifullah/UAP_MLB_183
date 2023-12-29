# RPS Classification

## Overview Problems
Permasalahan dari project ini yaitu bagaimana cara membuat model dengan akurasi bagus dari dataset RPS

![image 1](Images/Gambar-tiap-kelas.png)

## Overview Dataset
Dataset ini sudah tersedia pada website tensorflow, dataset dibagi menjadi 70% training, 25% validation, 5% testing.<br>link url untuk download dataset: https://drive.google.com/drive/folders/16ugqhXnjkhJS6xmP3D_PA2_Mj-nTHQdD?usp=drive_link

## Preprocessing and Modeling
Pada bagian preprocessing data di rescale 1/255 lalu rotasi, zoom, shear, shift dengan masing-masing 20%, random flip dan fill nearest setelah rotasi dan shift

Untuk model kami menggunakan model _MobileNet_ dan ini adalah ilustrasi bagaimana _MobileNet_ berkerja

![image 2](Images/Mobilenetv2-architecture.png)

Summary Model:

![image 3](Images/Summary.png)

Graph accuracy dan loss model:

![image 4](Images/Train&Loss-Graph.png)

Evaluate Model:

![image 5](Images/Classification-Report.png)

## Prediction and Deployment

Kami mengambil 10 image acak dari testing dan memperhatikan apakah model dapat memprediksi image dengan baik, berikut ini adalah hasilnya:

![image 6](Images/Predict.png)

Deployment kami menggunakan streamlit dan berikut ini contohnya:

![image 7](Images/Tampilan.png)

![image 8](Images/Hasil-prediksi.png)
