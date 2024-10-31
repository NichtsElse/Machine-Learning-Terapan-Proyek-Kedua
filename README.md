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
data yang digunakan adalah Book 'Book Recommendation Dataset' yang bersumber di kaggle. Dataset ini terdiri dari 3 file yang berisi users, ratings dan books. file users memiliki 3 variabel, ratings memiliki 3 variabel dan file books memiliki 8 variabel. dataset ini dapat diperoleh dari link ini [dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data).

### Variabel-variabel pada dataset adalah sebagai berikut:
Dataset Book-Crossing terdiri dari 3 berkas.
1. Pengguna:
Berisi pengguna. Perhatikan bahwa ID pengguna ( User-ID) telah dianonimkan dan dipetakan ke bilangan bulat. Data demografi disediakan ( Location, Age) jika tersedia. Jika tidak, kolom ini berisi nilai NULL.
2. Buku:
Buku diidentifikasi berdasarkan ISBN masing-masing. ISBN yang tidak valid telah dihapus dari kumpulan data. Selain itu, beberapa informasi berbasis konten diberikan ( Book-Title, Book-Author, Year-Of-Publication, Publisher), yang diperoleh dari Amazon Web Services. Perhatikan bahwa jika ada beberapa penulis, hanya penulis pertama yang diberikan. URL yang menghubungkan ke gambar sampul juga diberikan, muncul dalam tiga bentuk berbeda ( Image-URL-S, Image-URL-M, Image-URL-L), yaitu kecil, sedang, besar. URL ini mengarah ke situs web Amazon.
3. Rating:
Berisi informasi tentang rating buku. Rating ( Book-Rating) bisa eksplisit, dinyatakan dalam skala 1-10 (nilai yang lebih tinggi menunjukkan apresiasi yang lebih tinggi), atau implisit, dinyatakan dalam skala 0.

### Exploratory Data Analysis
pada proyek ini terdapat beberapa visualisasi seperti pada dibawah yaitu Distribusi rating buku.


berdasarkan gambar diatas bahwa nilai benign lebih banyak dari malignant.

visualisasi Frekuensi pembacaan pada tiap genre.


berdasarkan gambar diatas bahwa Fitur radius, perimeter dan area memiliki korelasi sangat kuat satu sama lain, yang menunjukkan bahwa ketika satu nilai meningkat, yang lain juga cenderung meningkat.

visualisasi Hubungan antara genre dan rating.


berdasarkan gambar diatas bahwa beberapa korelasi positif terlihat kuat antara fitur seperti radius_mean, perimeter_mean, dan area_mean, terutama membedakan dua kelas diagnosis.

visualisasi pairplot pada field standard error.


berdasarkan gambar diatas bahwa sebagian besar fitur tidak memiliki korelasi yang kuat satu sama lain, kecuali beberapa fitur seperti radius_se, perimeter_se, dan area_se, yang menunjukkan korelasi lumayan kuat. Fitur-fitur ini masih cukup baik dalam memisahkan dua kelas diagnosis.

visualisasi pairplot pada field worst.


berdasarkan gambar diatas bahwa ada beberapa korelasi yang sangat kuat antara fitur seperti radius_worst, perimeter_worst, dan area_worst.

visualisasi outliers dengan boxplot pada bagian variabel mean.


berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada variabel mean.

visualisasi outliers dengan boxplot pada bagian variabel standard error.


berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada variabel standard error.

visualisasi outliers dengan boxplot pada bagian variabel worst.


berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada variabel worst.

## Data Preparation
Dalam data preparation, dilakukan beberapa hal  sebelum memasukkan data ke model latih yaitu:

- Label Encoder
teknik ini digunakan untuk mengubah data kategorikal (label) menjadi data numerik.

- Handling Outlier
Handling outlier berfungsi untuk meningkatkan akurasi, mencegah overfitting, dan membuat model lebih stabil serta mudah diinterpretasikan. Dengan menangani data ekstrem, model fokus pada pola yang lebih representatif, sehingga hasil prediksi lebih konsisten. handling outliers yang saya gunakan dengan cara menghapus data yang tidak kurang dari batas bawah dan tidak lebih dari batas atas.

- Train-Test-Split
proses ini berguna untuk membagi dataset menjadi data training dan testing pembagian data pada proyek ini ada 80:30.

- Standarisasi
Proses  ini dilakukan untuk Meningkatkan performa algoritma machine learning. Standarisasi menggunakan standartscaler dan diterapkan pada kolom-kolom yang memiliki fitur numerik.

## Modeling
Model yang saya gunakan pada proyek ini yaitu:
- Collaborative Filtering 
Menggunakan Decision Tree yang merupakan algoritma yang membangun model klasifikasi dengan memecah data berdasarkan fitur yang paling relevan untuk membuat keputusan. Pada proyek ini, model Decision Tree digunakan dengan kedalaman maksimum(max_depth) sebesar 3, yang berarti pohon keputusan dibatasi hingga tiga tingkat untuk mencegah overfitting. Lalu menggunakan AdaBoost yang merupakan metode boosting yang meningkatkan performa model dengan menggabungkan beberapa weak learners (seperti Decision Tree) menjadi model yang lebih kuat. Pada proyek ini, AdaBoost digunakan dengan estimator berupa model Decision Tree yang memiliki kedalaman maksimum 3 dan jumlah estimators sebanyak 1000. Hal ini membantu model belajar dari kesalahan prediksi sebelumnya, meningkatkan akurasi secara keseluruhan.

- Content-Based Filtering
Random Forest adalah algoritma ensemble yang mengombinasikan hasil dari beberapa pohon keputusan (Decision Tree) untuk menghasilkan satu prediksi akhir. Algoritma ini menggunakan proses bagging atau bootstrap aggregating, di mana setiap pohon dilatih menggunakan subset data yang berbeda. Pada proyek ini, model Random Forest menggunakan 100 n_estimators dan dibatasi dengan kedalaman maksimum 
3 untuk menjaga keseimbangan antara bias dan variansi.

Saya mengambil data weighted average dikarenakan data imbalance yang mana data kanker jinak(benign) lebih banyak daripada kanker ganas(malignant). Berdasarkan hasil train AdaBoost lebih unggul dalam hal menangani kesalahan prediksi dan akurasi pada dataset daripada Random Forest dengan metrik presisi 1%, akurasi, recall dan F1 score lebih tinggi 2%.

## Evaluation
Metrik evaluasi yang digunakan adalah Confusion Matrix yang merupakan sebuah teknik yang digunakan dalam data mining dan machine learning untuk menghitung seberapa baik sebuah model dapat memprediksi label dari sebuah data seperti contoh pada gambar dibawah.

![presisi!](https://miro.medium.com/v2/resize:fit:750/format:webp/1*f5ZeXvhsNFZ4q91M4Lotgg.jpeg)

Selanjutnya saya akan membahas secara rinci mengenai metrik akurasi, precision, recall, dan F1-score sebagai berikut:
1. Accuracy
Akurasi adalah persentase prediksi yang benar dari keseluruhan prediksi yang dilakukan oleh model. Cara menghitung accuracy seperti pada rumus di bawah ini.

![akurasi](https://github.com/user-attachments/assets/0d95c09f-ac45-410b-b442-6bea9783aea0)

Berdasarkan hasil evaluasi menggunakan teknik yang dijelasakan sebelumnya kedua model mendapatkan hasil metrik sebagai berikut:
1. Random Forest
Accuracy    : 96%
Precision   : 97% 
Recall      : 96%
F1 Score    : 96%

2. Adaptive Boasting(Decision Tree + Adaboost)
Accuracy    : 97%
Precision   : 97% 
Recall      : 97%
F1 Score    : 97%

berdasarkan hasil evaluasi diatas model Adaptive Boosting adalah model terbaik untuk mengklasifikasi kanker payudara

## Daftar Pustaka
[1] Priyanka, Bendale. (2023). General Purpose Recommendation System. International Journal of Advanced Research in Science, Communication and Technology, 278-280. doi: 10.48175/ijarsct-9040

[2] Argyro P., Agori, Athanasios, Kiourtis., Argyro, Mavrogiorgou., Dimosthenis, Kyriazis. (2022). A Comparative Study of Collaborative Filtering in Product Recommendation. Emerging science journal, 7(1):1-15. doi: 10.28991/esj-2023-07-01-01

