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
- Sistem rekomendasi akan menggunakan data seperti rating, genre, dan preferensi pengguna untuk menghasilkan rekomendasi yang dipersonalisasi.

- Menggunakan collaborative filtering dan content-based filtering. untuk mencari metode terbaik dalam pengembangan sistem rekomendasi.

- Sebagai metrik pembanding, menggunakan beberapa metrik evaluasi antara lain RMSE dan MSE untuk melakukan evaluasi kualitatif terhadap rekomendasi yang dihasilkan untuk memastikan relevansi.

## Data Understanding
data yang digunakan adalah Book 'Book Recommendation Dataset' yang bersumber di kaggle. Dataset ini terdiri dari 3 file yang berisi users, ratings dan books. file users memiliki terdiri dari 278858 baris dan 3 kolom, ratings terdiri dari 1149780 baris dan 3 kolom dan file books terdiri dari 271360 baris dan 8 kolom. dataset ini dapat diperoleh dari link ini [dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data).

### Variabel-variabel pada dataset adalah sebagai berikut:
Dataset Book-Crossing terdiri dari 3 berkas.
1. Pengguna
a. User-ID : ID pengguna
b. Location: lokasi pengguna
c. Age : umur pengguna

2. Buku
a. Book-Title : judul buku
b. Book-Author: penulis buku
c. Year-Of-Publication : tahun buku di cetak
d. Publisher : pencetak buku
e. Image-URL-S :  gambar sampul berukuran kecil
f. Image-URL-M : gambar sampul berukuran sedang
g. Image-URL-L : gambar sampul berukuran besar
h. ISBN(International Standard Book Number) : nomor unik untuk identifikasi buku

3. Rating:
a. User-ID : ID pengguna
b. ISBN(International Standard Book Number) : nomor unik untuk identifikasi buku
c. Book-Rating : rating sebuah buku
Berisi informasi tentang rating buku. Rating ( Book-Rating) bisa eksplisit, dinyatakan dalam skala 1-10 (nilai yang lebih tinggi menunjukkan apresiasi yang lebih tinggi), atau implisit, dinyatakan dalam skala 0.

### Exploratory Data Analysis
pada proyek ini terdapat beberapa visualisasi seperti pada dibawah yaitu Distribusi rating buku.

## Data Preparation
Dalam data preparation, dilakukan beberapa hal proses sebelum memasukkan data ke model latih yaitu:

- Handling outliers
Handling outlier berfungsi untuk meningkatkan akurasi, mencegah overfitting, dan membuat model lebih stabil serta mudah diinterpretasikan. Dengan menangani data ekstrem, model fokus pada pola yang lebih representatif, sehingga hasil prediksi lebih konsisten. handling outliers yang saya gunakan dengan cara menghapus data yang tidak kurang dari batas bawah dan tidak lebih dari batas atas.

- Handling missing value
Handling missing value dengan menggunakan imputer untuk mengisi nilai null.


## Modeling
Model yang saya gunakan pada proyek ini yaitu:
- Collaborative Filtering 
Metode ini memanfaatkan data dari pengguna lain untuk memberikan rekomendasi. Dalam hal ini, model SVD (Singular Value Decomposition) digunakan untuk memprediksi rating buku berdasarkan pola rating dari pengguna lain. Berikut ini adalah hasil rekomendasi yang diperoleh:


foto rekom

- Content-Based Filtering
Metode ini memanfaatkan data karakteristik/konten dari buku(judul, penulis, penerbit) untuk memberikan rekomendasi. Dalam hal ini, Menggunakan cosine similarity digunakan untuk untuk menghitung kemiripan antar buku. Berikut ini adalah hasil rekomendasi yang diperoleh:



## Evaluation
Metrik evaluasi yang digunakan adalah Confusion Matrix yang merupakan sebuah teknik yang digunakan dalam data mining dan machine learning untuk menghitung seberapa baik sebuah model dapat memprediksi label dari sebuah data seperti contoh pada gambar dibawah.


## Daftar Pustaka
[1] Priyanka, Bendale. (2023). General Purpose Recommendation System. International Journal of Advanced Research in Science, Communication and Technology, 278-280. doi: 10.48175/ijarsct-9040

[2] Argyro P., Agori, Athanasios, Kiourtis., Argyro, Mavrogiorgou., Dimosthenis, Kyriazis. (2022). A Comparative Study of Collaborative Filtering in Product Recommendation. Emerging science journal, 7(1):1-15. doi: 10.28991/esj-2023-07-01-01

