# Laporan Proyek Machine Learning - Rizky Prayogi Reksomulyo

## Project Overview

Maraknya konten digital telah menyebabkan banyaknya pilihan bagi konsumen, sehingga menjadi tantangan tersendiri bagi setiap orang untuk menemukan konten yang sesuai dengan preferensi mereka. Sistem rekomendasi, yang menyarankan konten yang relevan berdasarkan data pengguna, menjawab tantangan ini dengan memberikan pengalaman yang dipersonalisasi dan meningkatkan kepuasan pengguna. Sistem ini diadopsi secara luas di berbagai domain, seperti e-commerce, hiburan, dan perpustakaan digital, yang bertujuan untuk meningkatkan keterlibatan pelanggan dan mengurangi upaya pencarian dengan menyajikan rekomendasi yang disesuaikan[1].

Dalam konteks buku, sistem rekomendasi memainkan peran penting dalam membantu pengguna menavigasi koleksi yang besar, menemukan buku baru, dan menemukan kembali buku-buku favorit. Sistem rekomendasi buku biasanya menggunakan collaborative filtering, content-based filtering, atau pendekatan hibrida untuk menganalisis preferensi dan interaksi pengguna. Penyaringan kolaboratif, khususnya, mengidentifikasi pola dalam data perilaku pengguna, menggunakan kemiripan di antara pengguna atau item untuk memprediksi rekomendasi. Teknik ini telah terbukti sangat efektif, terutama ketika umpan balik eksplisit, seperti peringkat, atau umpan balik implisit, seperti riwayat pembelian, tersedia[2].

Proyek ini bertujuan untuk merancang sistem rekomendasi yang secara efektif membantu pengguna dalam menemukan buku-buku yang sesuai dengan minat mereka, menggunakan pendekatan collaborative filtering dengan content-based filtering untuk dikomparasi, dan mengevaluasi kinerja kedua model tersebut untuk memastikan rekomendasi yang relevan dan menarik.
 
## Business Understanding
### Problem Statements
- Bagaimana cara mengembangkan sistem rekomendasi yang cepat dan akurat untuk menemukan buku yang sesuai dengan preferensi user?

### Goals
- Mengembangkan sistem rekomendasi buku yang dapat memberikan saran yang relevan berdasarkan riwayat atau preferensi pengguna.

### Solution statements
- Menggunakan collaborative filtering yang memanfaatkan data dari pengguna lain untuk memberikan rekomendasi.

- Menggunakan content-based filtering yang memanfaatkan data karakteristik/konten dari buku(judul, penulis, penerbit) untuk memberikan rekomendasi.

- Sebagai metrik pembanding, menggunakan beberapa metrik evaluasi antara lain RMSE dan MSE untuk melakukan evaluasi kualitatif terhadap rekomendasi yang dihasilkan untuk memastikan relevansi.

## Data Understanding
data yang digunakan adalah Book 'Book Recommendation Dataset' yang bersumber di kaggle. Dataset ini terdiri dari 3 file yang berisi users, ratings dan books. file users memiliki terdiri dari 278858 baris dan 3 kolom, ratings terdiri dari 1149780 baris dan 3 kolom dan file books terdiri dari 271360 baris dan 8 kolom. dataset ini dapat diperoleh dari link ini [dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data).

### Variabel-variabel pada dataset adalah sebagai berikut:
Dataset Book-Crossing terdiri dari 3 berkas.

1. Pengguna
   
   a. User-ID : ID pengguna.
   
   b. Location: lokasi pengguna.
   
   c. Age : umur pengguna.

2. Buku
   
   a. Book-Title : judul buku.
   
   b. Book-Author: penulis buku.
   
   c. Year-Of-Publication : tahun buku di cetak.
   
   d. Publisher : pencetak buku.
   
   e. Image-URL-S :  gambar sampul berukuran kecil.
   
   f. Image-URL-M : gambar sampul berukuran sedang.
   
   g. Image-URL-L : gambar sampul berukuran besar.
   
   h. ISBN(International Standard Book Number) : nomor unik untuk identifikasi buku.

3. Rating:
     
   a. User-ID : ID pengguna.
   
   b. ISBN(International Standard Book Number) : nomor unik untuk identifikasi buku.
   
   c. Book-Rating : rating sebuah buku.

### Exploratory Data Analysis
pada proyek ini terdapat beberapa visualisasi seperti pada dibawah yaitu Distribusi rating buku.

visualisasi Distribusi Rating

![disr](https://github.com/user-attachments/assets/2323bdc4-a463-4118-a1d8-19cb5992cc59)

berdasarkan gambar diatas bahwa distribusi ratingnya right skewed dengan paling banyak rating 1.

visualisasi Distribusi tahun publikasi

![disp](https://github.com/user-attachments/assets/984da831-4f32-41f4-9638-3d909095f3c2)

berdasarkan gambar diatas bahwa distribusinya left skewed dengan kebanyakan tahun publikasi pada tahun 1990 sampai tahun 2000.

visualisasi outliers age dan rating

![box](https://github.com/user-attachments/assets/43b9e3a0-0d7e-4900-8d25-1226e0612d1e)

berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada age.

## Data Preparation
Dalam data preparation, dilakukan beberapa hal proses sebelum memasukkan data ke model latih yaitu:

- Handling outliers
Handling outlier berfungsi untuk meningkatkan akurasi, mencegah overfitting, dan membuat model lebih stabil serta mudah diinterpretasikan. Dengan menangani data ekstrem, model fokus pada pola yang lebih representatif, sehingga hasil prediksi lebih konsisten. handling outliers yang saya gunakan dengan cara menghapus data yang tidak kurang dari batas bawah dan tidak lebih dari batas atas.

- Handling missing value
Handling missing value dengan menggunakan imputer untuk mengisi nilai null.

-TF-IDF
teknik dalam pemrosesan teks yang digunakan untuk menilai seberapa penting sebuah kata dalam suatu dokumen relatif terhadap kumpulan dokumen lainnya (corpus).

## Modeling
Model yang saya gunakan pada proyek ini yaitu:
- Collaborative Filtering 
Metode ini memanfaatkan data dari pengguna lain untuk memberikan rekomendasi. Dalam hal ini, model SVD (Singular Value Decomposition) digunakan untuk memprediksi rating buku berdasarkan pola rating dari pengguna lain.

- Content-Based Filtering
Metode ini memanfaatkan data karakteristik/konten dari buku(judul, penulis, penerbit) untuk memberikan rekomendasi. Dalam hal ini, Menggunakan cosine similarity digunakan untuk untuk menghitung kemiripan antar buku.

## Evaluation
1. Root Mean Squared Error (RMSE)
RMSE adalah turunan dari MSE. Seperti namanya, RMSE adalah akar kuadrat dari MSE. RMSE menghitung rata-rata dari selisih kuadrat antara nilai prediksi dan nilai aktual kemudian diambil akar kuadratnya. seperti rumus dibawah ini:

![rmse-1](https://github.com/user-attachments/assets/617f16a0-50d0-4306-b09a-19a983992ba5)

Semakin kecil nilai RMSE, semakin baik kualitas model tersebut.
2. Mean Absolute Error (MAE)
MAE adalah salah satu metode evaluasi yang umum digunakan dalam data science. MAE menghitung rata-rata dari selisih absolut antara nilai prediksi dan nilai aktual. seperti rumus dibawah ini: 

![mae-formula](https://github.com/user-attachments/assets/c8505139-840b-476f-b09b-0671a0680f4f)

Dengan kata lain, MAE menghitung berapa rata-rata kesalahan absolut dalam prediksi. Semakin kecil nilai MAE, semakin baik kualitas model tersebut.

Berdasarkan nilai metrik RMSE sebesar 3.6319 dan MAE sebesar 3.1951, dapat disimpulkan bahwa model memiliki akurasi prediksi yang moderat dengan rata-rata kesalahan sekitar 3 satuan dari nilai sebenarnya. 

## Daftar Pustaka
[1] Priyanka, Bendale. (2023). General Purpose Recommendation System. International Journal of Advanced Research in Science, Communication and Technology, 278-280. doi: 10.48175/ijarsct-9040

[2] Argyro P., Agori, Athanasios, Kiourtis., Argyro, Mavrogiorgou., Dimosthenis, Kyriazis. (2022). A Comparative Study of Collaborative Filtering in Product Recommendation. Emerging science journal, 7(1):1-15. doi: 10.28991/esj-2023-07-01-01

