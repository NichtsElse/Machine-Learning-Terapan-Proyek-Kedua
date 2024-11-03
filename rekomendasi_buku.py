# -*- coding: utf-8 -*-
"""rekomendasi-buku.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nQv1HU0P5kUdr63mVJ8ImXJC94ZFUcPJ

import libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

import warnings
warnings.filterwarnings('ignore')
import kagglehub

"""### Data Preparation

download dataset di kaggle
"""

# download data dari kaggle
path = kagglehub.dataset_download("arashnic/book-recommendation-dataset")

print("Path to dataset files:", path)

"""load data csv"""

book_df = pd.read_csv('/root/.cache/kagglehub/datasets/arashnic/book-recommendation-dataset/versions/3/Books.csv')
ratings_df = pd.read_csv('/root/.cache/kagglehub/datasets/arashnic/book-recommendation-dataset/versions/3/Ratings.csv').sample(30000)
user_df = pd.read_csv('/root/.cache/kagglehub/datasets/arashnic/book-recommendation-dataset/versions/3/Users.csv')

"""Merge dataset"""

# Menggabungkan semua dataset berdasarkan User-ID dan ISBN
merged_df = pd.merge(ratings_df, book_df, on='ISBN', how='inner')
merged_df = pd.merge(merged_df, user_df, on='User-ID', how='inner')

# Menampilkan 5 data teratas dari dataframe yang telah digabungkan
merged_df.head()

merged_df.info()

"""### Data Cleaning

cek duplikat
"""

merged_df.duplicated().sum()

"""cek missing value"""

#cek null pada dataframe
merged_df.isnull().sum()

"""cek ukuran dataframe"""

merged_df.shape

"""cek jumlah data keseluruhan"""

merged_df.size

"""berdasarkan hasil cek data  memiliki banyak missing value

### EDA

cek unique value
"""

# melihat nilai unik setiap variabel
merged_df.nunique()

"""drop id karna tidak memiliki korelasi apapun"""

# menghilangkan data image url S dan M dari merged_df
df=merged_df.drop(['Image-URL-M','Image-URL-S'],axis=1)

"""### Univariate Analysis

visualisasi Distribusi Rating
"""

# Distribusi Rating
plt.figure(figsize=(10, 6))
sns.histplot(df['Book-Rating'], bins=10, kde=True)
plt.title('Distribusi Rating Buku')
plt.xlabel('Rating')
plt.ylabel('Jumlah')
plt.show()

"""berdasarkan gambar diatas bahwa distribusi ratingnya right skewed dengan paling banyak rating 1.

visualisasi Distribusi tahun publikasi
"""

# Mengubah kolom 'Year-Of-Publication' menjadi integer
df['Year-Of-Publication'] = df['Year-Of-Publication'].astype(int)

# Filter data untuk tahun antara 1750 dan 2010
df_filtered = df[(df['Year-Of-Publication'] >= 1960) & (df['Year-Of-Publication'] <= 2008)]

# Distribusi Tahun Publikasi
plt.figure(figsize=(10, 6))
sns.histplot(df_filtered['Year-Of-Publication'], bins=10, kde=True)
plt.title('Distribusi Tahun Publikasi (1750 - 2010)')
plt.xlabel('Tahun')
plt.ylabel('Jumlah')
plt.show()

"""berdasarkan gambar diatas bahwa distribusinya left skewed dengan kebanyakan tahun publikasi pada tahun 1990 sampai tahun 2000.

visualisasi outliers age dan rating
"""

# Membuat visualisasi boxplot untuk Age dan Rating
plt.figure(figsize=(12, 6))

# Boxplot untuk Age
plt.subplot(1, 2, 1)
sns.boxplot(y='Age', data=df)
plt.title('Boxplot Age')

# Boxplot untuk Rating
plt.subplot(1, 2, 2)
sns.boxplot(y='Book-Rating', data=df)
plt.title('Boxplot Rating')

plt.tight_layout()
plt.show()

"""berdasarkan gambar diatas bahwa terdapat banyak nilai outliers pada age.

### Data Preprocessing

handling missing value
"""

# Mengubah nilai null pada kolom 'Age' menggunakan teknik inputasi
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
df[['Age']] = imputer.fit_transform(df[['Age']])

"""handling outliers"""

# menghilangkan data outliers
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df[~((df['Age'] < lower_bound) | (df['Age'] > upper_bound))]

df_clean.info()

"""### Modeling

#### model Collaborative Filtering
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install surprise

"""Metode ini memanfaatkan data dari pengguna lain untuk memberikan rekomendasi. Dalam hal ini, model SVD (Singular Value Decomposition) digunakan untuk memprediksi rating buku berdasarkan pola rating dari pengguna lain.

Inisialisasi data dan skala rating untuk Collaborative Filtering
"""

from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy

reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(df_clean[['User-ID', 'ISBN', 'Book-Rating']], reader)

"""Membagi data menjadi train dan test set dengan perbandingan 80:20"""

trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

"""membuat model SVD"""

svd_model = SVD()
svd_model.fit(trainset)

""" Melakukan prediksi pada test set"""

predictions = svd_model.test(testset)

"""Evaluasi Collaborative Filtering menggunakan RMSE dan MSE"""

rmse = accuracy.rmse(predictions)
mae = accuracy.mae(predictions)

"""membuat fungsi rekomendasi"""

def recommend_books(user_id, n=10):
    # List all unique book titles
    all_books = df_clean['Book-Title'].unique()

    # Remove books already rated by the user
    rated_books = df_clean[df_clean['User-ID'] == user_id]['Book-Title'].values
    books_to_predict = [book for book in all_books if book not in rated_books]

    # Predict ratings for remaining books
    predictions = []
    for book in books_to_predict:
        pred = svd_model.predict(user_id, book)
        predictions.append((book, pred.est))

    # Sort predictions by estimated rating
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Get top N recommendations
    top_n = predictions[:n]
    print(f"Top 10 rekomendasi buku untuk user {user_id}:")
    # Iterate through 'top_n' instead of 'recommended_books'
    for i, (title, _) in enumerate(top_n, start=1):
        print(f"{i}. {title}")
    return top_n

"""inference"""

user_id = 271705
recommended_books = recommend_books(user_id)

"""#### model content-based filtering

Metode ini memanfaatkan data karakteristik/konten dari buku(judul, penulis, penerbit) untuk memberikan rekomendasi. Dalam hal ini, Menggunakan cosine similarity digunakan untuk untuk menghitung kemiripan antar buku.

Combine kolom yang relevan untuk content-based filtering
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

df_clean['combined_features'] = df_clean['Book-Title'] + ' ' + df_clean['Book-Author'] + ' ' + df_clean['Publisher']

"""membuat matrix TF-IDF"""

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_clean['combined_features'])
tfidf_matrix.todense()

"""menghitung matriks cosine similarity"""

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix)

"""membuat fungsi rekomendasi"""

def get_recommendations(title, cosine_sim=cosine_sim):
    # Memeriksa apakah judul buku ada dalam DataFrame
    if title not in df_clean['Book-Title'].values:
        print(f"Buku dengan judul '{title}' tidak ditemukan.")
        return

    # Mendapatkan indeks dari buku yang sesuai dengan judul
    idx = df_clean[df_clean['Book-Title'] == title].index[0]

    # Mendapatkan skor kesamaan dari semua buku dengan buku yang diberikan
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Mengurutkan buku berdasarkan skor kesamaan
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Mendapatkan indeks buku dari 10 buku yang paling mirip
    book_indices = [i[0] for i in sim_scores[1:11]]

    # Mengembalikan dan mencetak judul buku yang paling mirip
    recommended_books = df_clean['Book-Title'].iloc[book_indices].tolist()
    print(f"Rekomendasi buku untuk judul buku '{title}':")
    for i, book in enumerate(recommended_books, 1):
        print(f"{i}. {book}")

"""inference"""

get_recommendations('Moment of Truth')