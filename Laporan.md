# Laporan Proyek Machine Learning - Rizky Prayogi Reksomulyo

## Domain Proyek Kesehatan

Kanker payudara merupakan salah satu masalah kesehatan global yang paling mendesak. WHO mencatat pada tahun 2022 ada 2,3 juta wanita di seluruh dunia yang didiagnosis menderita kanker payudara, dengan angka kematian mencapai 670.000 kasus[1]. Berdasarkan data dari Globocan 2022 Kanker payudara menempati urutan pertama terkait jumlah kanker terbanyak di Indonesia jumlah kasus baru kanker payudara mencapai 66.271 kasus (16,2%) dari total 408.661 kasus baru kanker di Indonesia. Sementara itu, untuk jumlah kematiannya mencapai lebih dari 22 ribu jiwa[2]. Kanker ini dapat menyerang wanita di berbagai usia setelah pubertas, namun prevalensinya meningkat seiring bertambahnya usia. Fakta ini menunjukkan bahwa kanker payudara adalah ancaman serius yang membutuhkan perhatian khusus, terutama dalam hal deteksi dini dan penanganan yang efektif.

berdasarkan data diatas saya memiliki tujuan untuk mengembangkan model prediktif yang dapat membantu mendeteksi apakah kanker bersifat jinak (benign) atau ganas (malignant). Deteksi dini sangat penting dalam penanganan kanker payudara, karena semakin cepat kanker terdeteksi, semakin tinggi kemungkinan kesembuhan dan penurunan risiko kematian. Dengan menggunakan dataset diagnostik Kanker Payudara Wisconsin dan algoritma machine learning, proyek ini diharapkan dapat memberikan solusi yang lebih cepat, akurat, dan efisien dalam membantu diagnosis kanker payudara. 

Hasil proyek ini dapat berkontribusi pada peningkatan akses dan kualitas diagnosis di berbagai negara, terutama di wilayah dengan sumber daya terbatas, sehingga membantu mengurangi angka kematian pada penderita kanker payudara yang selaras dengan tujuan WHO Global Breast Cancer Initiative (GBCI) yaitu mengurangi angka kematian akibat kanker payudara global sebesar 2,5% per tahun, sehingga mencegah 2,5 juta kematian akibat kanker payudara di seluruh dunia antara tahun 2020 dan 2040.
 
## Business Understanding
### Problem Statements
- Bagaimana cara memprediksi apakah seseorang memiliki kanker payudara jinak (benign) atau ganas(malignant)?

### Goals
- Memprediksi apakah seseorang memiliki kanker payudara jinak(benign) atau ganas(malignant) berdasarkan statistik kesehatannya.

### Solution statements
- Menggunakan metode Random Forest, di mana metode ini merupakan algoritma ensemble yang powerful dan mampu menangani data yang kompleks serta fitur yang saling berinteraksi. Random Forest juga memberikan hasil yang stabil dan dapat diandalkan, sehingga digunakan sebagai pembanding dari Logistic Regression.

- Menggunakan Decision Tree yang efektif untuk klasifikasi dan mudah dipahami, memprediksi kanker payudara berdasarkan fitur yang paling informatif. Lalu, AdaBoost digunakan untuk meningkatkan performa dengan menggabungkan beberapa weak learners, memperbaiki kesalahan prediksi, dan meningkatkan akurasi, menjadikannya model yang cocok sebagai pembanding.

- Sebagai metrik pembanding, menggunakan beberapa metrik evaluasi antara lain Akurasi, Precision, Recall, dan F1-Score untuk mendapatkan gambaran yang lebih komprehensif mengenai performa model dalam mendeteksi kanker jinak(benign) dan ganas(malignant).

## Data Understanding
data yang digunakan adalah Breast Cancer Wisconsin (Diagnostic) yang bersumber di kaggle. Dataset ini terdiri dari 569 baris data, memiliki 32 kolom data dan dapat diperoleh dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic). Kondisi data setelah di cek tidak terdapat missing value atau duplikat hanya memilik outliers saja.

### Variabel-variabel pada dataset adalah sebagai berikut:
1.  ID number
2.  Diagnosis (M = Malignant(ganas), B = Benign(jinak))
   
10 fitur utama untuk setiap inti sel:
1.  radius (rata-rata jarak dari pusat ke titik-titik di keliling). 
2. texture (standar deviasi nilai gray-scale).
3. perimeter(keliling).
4. area(nilai area).
5. smoothness (variasi lokal dalam panjang radius).
6. compactness (perimeter^2 / area - 1.0).
7. concavity (tingkat keparahan bagian cekung pada kontur).
8. concave points (jumlah bagian cekung dari kontur).
9. symmetry(nilai simetris).
10. fractal dimension ("perkiraan tepi" - 1).
 
mean, standard error dan "worst" dari fitur-fitur ini dihitung untuk 10 fitur utama yang menghasilkan 30 fitur.
nilai  mean pada 10 fitur utama:
1. radius_mean(rata-rata dari nilai radius). 
2. texture_mean(rata-rata dari nilai texture).
3. perimeter_mean(rata-rata dari nilai perimeter).
4. area_mean(rata-rata dari nilai area).
5. smoothness_mean (rata-rata dari nilai smoothness).
6. compactness_mean rata-rata dari nilai compactness).
7. concavity_mean (rata-rata dari nilai concavity).
8. concave points_mean(rata-rata dari nilai concave points).
9. symmetry_mean(rata-rata dari nilai symmetry).
10. fractal dimension_mean (rata-rata dari nilai fractal dimension).
    
nilai standard error pada 10 fitur utama:
1. radius_se(standard error dari nilai radius). 
2. texture_se(standard error dari nilai texture).
3. perimeter_se(standard error dari nilai perimeter).
4. area_se(standard error dari nilai area).
5. smoothness_se(standard error dari nilai smoothness).
6. compactness_se(standard error darii nilai compactness).
7. concavity_se(standard error dari nilai concavity).
8. concave points_se(standard error dari nilai concave points).
9. symmetry_se(standard error dari nilai symmetry).
10. fractal dimension_se(standard error dari nilai fractal dimension). 

nilai worst pada 10 fitur utama:
1. radius_worst(nilai worst dari radius). 
2. texture_worst(nilai worst dari texture).
3. perimeter_worst(nilai worst dari perimeter).
4. area_worst(nilai worst dari area).
5. smoothness_worst(nilai worst dari smoothness).
6. compactness_worst(nilai worst dari compactness).
7. concavity_worst(nilai worst dari concavity).
8. concave points_worst(nilai worst dari concave points).
9. symmetry_worst(nilai worst dari simetris).
10. fractal dimension_worst(nilai worst dari fractal dimension).

### Exploratory Data Analysis
pada proyek ini terdapat beberapa visualisasi seperti pada dibawah yaitu bar chart data diagnosis.

<img width="481" alt="bar1" src="https://github.com/user-attachments/assets/ea8def24-8b50-4946-a3fd-6e1b60185f54">

berdasarkan gambar diatas bahwa nilai benign lebih banyak dari malignant.

visualisasi korelasi antar variabel pada heatmap.

![cor](https://github.com/user-attachments/assets/f364bbfb-f5ae-4a06-a093-72809733f244)

berdasarkan gambar diatas bahwa Fitur radius, perimeter dan area memiliki korelasi sangat kuat satu sama lain, yang menunjukkan bahwa ketika satu nilai meningkat, yang lain juga cenderung meningkat.

visualisasi pairplot pada field mean.

![mean](https://github.com/user-attachments/assets/096b5581-751d-4f9b-b6e3-83b628555d2c)

berdasarkan gambar diatas bahwa beberapa korelasi positif terlihat kuat antara fitur seperti radius_mean, perimeter_mean, dan area_mean, terutama membedakan dua kelas diagnosis.

visualisasi pairplot pada field standard error.

![se](https://github.com/user-attachments/assets/6b343fca-528c-4e6f-867c-986ecfb2e956)

berdasarkan gambar diatas bahwa sebagian besar fitur tidak memiliki korelasi yang kuat satu sama lain, kecuali beberapa fitur seperti radius_se, perimeter_se, dan area_se, yang menunjukkan korelasi lumayan kuat. Fitur-fitur ini masih cukup baik dalam memisahkan dua kelas diagnosis.

visualisasi pairplot pada field worst.

![worst](https://github.com/user-attachments/assets/f65c1c66-b54c-4367-ab7b-e8253df78813)

berdasarkan gambar diatas bahwa ada beberapa korelasi yang sangat kuat antara fitur seperti radius_worst, perimeter_worst, dan area_worst.

visualisasi outliers dengan boxplot pada bagian variabel mean.

![outliermean](https://github.com/user-attachments/assets/27c6e0e3-baa6-4c18-912d-8ab2a11cdd3c)

berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada variabel mean.

visualisasi outliers dengan boxplot pada bagian variabel standard error.

![outlierse](https://github.com/user-attachments/assets/87fd6cd9-6ca9-40ea-a1b8-0442acce1e56)

berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada variabel standard error.

visualisasi outliers dengan boxplot pada bagian variabel worst.

![outlierworst](https://github.com/user-attachments/assets/f6422838-d773-41b4-8cd7-5ace951cca89)

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
- Adaptive Boosting
Menggunakan Decision Tree yang merupakan algoritma yang membangun model klasifikasi dengan memecah data berdasarkan fitur yang paling relevan untuk membuat keputusan. Pada proyek ini, model Decision Tree digunakan dengan kedalaman maksimum(max_depth) sebesar 3, yang berarti pohon keputusan dibatasi hingga tiga tingkat untuk mencegah overfitting. Lalu menggunakan AdaBoost yang merupakan metode boosting yang meningkatkan performa model dengan menggabungkan beberapa weak learners (seperti Decision Tree) menjadi model yang lebih kuat. Pada proyek ini, AdaBoost digunakan dengan estimator berupa model Decision Tree yang memiliki kedalaman maksimum 3 dan jumlah estimators sebanyak 1000. Hal ini membantu model belajar dari kesalahan prediksi sebelumnya, meningkatkan akurasi secara keseluruhan.

- Random Forest
Random Forest adalah algoritma ensemble yang mengombinasikan hasil dari beberapa pohon keputusan (Decision Tree) untuk menghasilkan satu prediksi akhir. Algoritma ini menggunakan proses bagging atau bootstrap aggregating, di mana setiap pohon dilatih menggunakan subset data yang berbeda. Pada proyek ini, model Random Forest menggunakan 100 n_estimators dan dibatasi dengan kedalaman maksimum 
3 untuk menjaga keseimbangan antara bias dan variansi.

Saya mengambil data weighted average dikarenakan data imbalance yang mana data kanker jinak(benign) lebih banyak daripada kanker ganas(malignant). Berdasarkan hasil train AdaBoost lebih unggul dalam hal menangani kesalahan prediksi dan akurasi pada dataset daripada Random Forest dengan metrik presisi 1%, akurasi, recall dan F1 score lebih tinggi 2%.

## Evaluation
Metrik evaluasi yang digunakan  adalah Confusion Matrix yang merupakan sebuah teknik yang digunakan dalam data mining dan machine learning untuk menghitung seberapa baik sebuah model dapat memprediksi label dari sebuah data seperti contoh pada gambar dibawah.

![presisi!](https://miro.medium.com/v2/resize:fit:750/format:webp/1*f5ZeXvhsNFZ4q91M4Lotgg.jpeg)

Selanjutnya saya akan membahas secara rinci mengenai metrik akurasi, precision, recall, dan F1-score sebagai berikut:
1. Accuracy
Akurasi adalah persentase prediksi yang benar dari keseluruhan prediksi yang dilakukan oleh model. Cara menghitung accuracy seperti pada rumus di bawah ini.

![akurasi](https://github.com/user-attachments/assets/0d95c09f-ac45-410b-b442-6bea9783aea0)

3. Precision (Presisi)
Precision adalah persentase prediksi yang benar dari semua prediksi yang positif. Dengan kata lain, precision mengukur akurasi dari prediksi positif model. Cara menghitung precision seperti pada rumus di bawah ini.

![presisi](https://github.com/user-attachments/assets/a6e2bd90-5108-46e6-8e43-c1b30cfd4a3d)

5. Recall (Sensitivitas)
Recall adalah persentase dari semua kasus positif yang terdeteksi oleh model. Ini mengukur seberapa baik model dapat menangkap semua kasus yang benar-benar positif. Cara menghitung recall seperti pada rumus di bawah ini.

![recall](https://github.com/user-attachments/assets/72ce4717-b24d-42ef-9131-0814b1696dc3)

7. F1-Score
F1-score adalah rata-rata harmonis dari precision dan recall. Metrik ini berguna ketika Anda ingin mencapai keseimbangan antara precision dan recall. Cara menghitung F1-Score seperti pada rumus di bawah ini.

<img width="581" alt="f1" src="https://github.com/user-attachments/assets/07abb886-7c2d-424b-bd25-6d4539b3e515">


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
[1] Ferlay J, Ervik M, Lam F, Laversanne M, Colombet M, Mery L, Piñeros M, Znaor A, Soerjomataram I, Bray F (2024). Global Cancer Observatory: Cancer Today. Lyon, France: International Agency for Research on Cancer. Available from: https://gco.iarc.who.int/today, accessed 22 October 2024.

[2] World Health Organization (2024). Breast Cancer. Online at https://www.who.int/news-room/fact-sheets/detail/breast-cancer, accessed 22 October 2024

