# Laporan Proyek Machine Learning - Dina Prastuti

## Project Overview

Dalam era digital saat ini, jumlah informasi yang tersedia secara online, termasuk buku, telah berkembang pesat. Hal ini seringkali menyulitkan pengguna untuk menemukan buku yang benar-benar sesuai dengan minat dan preferensi mereka di antara jutaan pilihan yang ada. Sistem rekomendasi hadir sebagai solusi untuk mengatasi masalah kelebihan informasi ini (information overload) dengan cara menyaring dan menyajikan item (dalam hal ini, buku) yang paling relevan bagi pengguna tertentu. Proyek ini bertujuan untuk membangun sebuah sistem rekomendasi buku yang efektif menggunakan data dari komunitas Book-Crossing.

Pentingnya proyek ini terletak pada kemampuannya untuk meningkatkan pengalaman pengguna dalam menemukan buku baru. Bagi platform penjualan buku atau perpustakaan digital, sistem rekomendasi yang baik dapat secara signifikan meningkatkan keterlibatan pengguna, kepuasan pelanggan, dan pada akhirnya, dapat mendorong penjualan atau peminjaman buku. Seperti yang telah dibuktikan oleh perusahaan besar seperti Amazon dan Netflix, sistem rekomendasi yang efisien merupakan aset krusial yang dapat memberikan keunggulan kompetitif yang signifikan. Dengan menganalisis preferensi pengguna dan karakteristik buku, sistem ini dapat memberikan rekomendasi yang dipersonalisasi, membantu pengguna menemukan 'permata tersembunyi' yang mungkin tidak akan mereka temukan melalui penelusuran biasa.

## Business Understanding

Bagian ini akan mengklarifikasi masalah yang ingin diselesaikan, tujuan yang ingin dicapai, dan pendekatan solusi yang akan digunakan.

### Problem Statements

Berdasarkan latar belakang yang telah diuraikan, masalah utama yang ingin diatasi dalam proyek ini adalah:

- Bagaimana cara membantu pengguna menemukan buku yang relevan dengan minat baca mereka di tengah banyaknya pilihan buku yang tersedia?
- Bagaimana cara membangun model rekomendasi yang dapat memberikan saran buku yang dipersonalisasi berdasarkan riwayat baca dan preferensi pengguna lain (collaborative) serta berdasarkan konten atau atribut buku itu sendiri (content-based)?

### Goals

Tujuan utama dari proyek ini adalah:

- Mengembangkan sistem yang mampu memberikan rekomendasi buku yang akurat dan relevan kepada pengguna.
- Mengimplementasikan dan membandingkan dua pendekatan utama dalam sistem rekomendasi: Content-Based Filtering dan Collaborative Filtering, untuk memberikan rekomendasi buku.
- Menghasilkan daftar rekomendasi Top-N buku untuk pengguna berdasarkan kedua pendekatan tersebut.

### Solution statements

- **Content-Based Filtering:** Pendekatan ini akan merekomendasikan buku berdasarkan kemiripan konten atau atribut buku (seperti genre, penulis, atau deskripsi jika tersedia) dengan buku-buku yang pernah disukai atau dibaca oleh pengguna di masa lalu. Kemiripan antar buku akan dihitung menggunakan teknik seperti TF-IDF pada fitur tekstual dan cosine similarity.
- **Collaborative Filtering:** Pendekatan ini akan merekomendasikan buku berdasarkan pola preferensi dari pengguna lain yang memiliki selera serupa. Jika pengguna A dan pengguna B cenderung menyukai buku yang sama, maka buku yang disukai pengguna B tetapi belum dibaca oleh pengguna A akan direkomendasikan kepada pengguna A, dan sebaliknya. Teknik yang umum digunakan adalah User-Based atau Item-Based Collaborative Filtering, atau menggunakan teknik faktorisasi matriks seperti Singular Value Decomposition (SVD).

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah Kumpulan Data Rekomendasi Buku yang tersedia di Kaggle dengan judul Book Recommendation Dataset dan dapat diunduh melalui tautan berikut: [Kumpulan Data Rekomendasi Buku](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).

Dataset ini merupakan hasil dari proyek Book-Crossing dan terdiri dari tiga berkas utama dalam format CSV, yaitu:

- **Books.csv:** Berisi informasi 271.360 data buku yang diidentifikasi berdasarkan kode ISBN. Data ini mencakup judul buku (Book-Title), nama penulis (Book-Author), tahun terbit (Year-Of-Publication), dan penerbit (Publisher). Selain itu, terdapat juga URL gambar sampul dalam tiga ukuran berbeda (Image-URL-S, Image-URL-M, Image-URL-L) yang mengarah ke situs Amazon.
- **Users.csv:** Berisi 278.858 data pengguna yang telah dianonimkan dengan fitur ID unik (User-ID). Jika tersedia, informasi demografis seperti lokasi (Location) dan usia (Age) juga disertakan. Namun, sebagian data mungkin memiliki nilai kosong (NULL) jika informasi tidak tersedia.
- **Ratings.csv:** Berisi informasi mengenai rating buku dari para pengguna. Terdapat 1.149.780 data rating. Fitur yang ada adalah `User-ID`, `ISBN`, dan `Book-Rating`. Rating diberikan dalam skala 1-10 (eksplisit, nilai lebih tinggi berarti apresiasi lebih tinggi) atau 0 (implisit).

Variabel-variabel pada Kumpulan Data Rekomendasi Buku adalah sebagai berikut:

- **Users.csv:**
  - `User-ID`: Identifier unik untuk setiap pengguna (Integer).
  - `Location`: Lokasi geografis pengguna (String).
  - `Age`: Usia pengguna (Float). Terdapat nilai kosong (NaN).
- **Books.csv:**
  - `ISBN`: International Standard Book Number, identifier unik untuk setiap buku (String).
  - `Book-Title`: Judul buku (String).
  - `Book-Author`: Nama penulis buku (String). Terdapat nilai kosong.
  - `Year-Of-Publication`: Tahun buku diterbitkan (String/Object, perlu diperiksa dan dibersihkan).
  - `Publisher`: Nama penerbit buku (String). Terdapat nilai kosong.
  - `Image-URL-S`: URL ke gambar sampul buku ukuran kecil (String).
  - `Image-URL-M`: URL ke gambar sampul buku ukuran sedang (String).
  - `Image-URL-L`: URL ke gambar sampul buku ukuran besar (String). Terdapat nilai kosong.
- **Ratings.csv:**
  - `User-ID`: Identifier pengguna yang memberikan rating (Integer).
  - `ISBN`: Identifier buku yang diberi rating (String).
  - `Book-Rating`: Nilai rating yang diberikan oleh pengguna (Integer). Skala 0 (implisit) atau 1-10 (eksplisit).

### Analisis Eksplorasi Data (EDA) dan Visualisasi

Setelah memuat data, dilakukan analisis eksplorasi untuk memahami lebih dalam karakteristik dataset:

- **Missing Values:** Ditemukan nilai kosong pada kolom `Book-Author` (2), `Publisher` (2), dan `Image-URL-L` (3) di dataset `Books`. Kolom `Age` pada dataset `Users` memiliki jumlah nilai kosong yang signifikan (110.762). Dataset `Ratings` tidak memiliki nilai kosong.
- **Duplikat:** Tidak ditemukan data duplikat berdasarkan `ISBN` di `Books`, kombinasi `User-ID` dan `ISBN` di `Ratings`, maupun `User-ID` di `Users`.
- **Distribusi Rating:** Sebagian besar rating adalah 0 (implisit), menunjukkan bahwa pengguna menandai buku tanpa memberikan rating eksplisit. Untuk rating eksplisit (1-10), rating 8 adalah yang paling umum, diikuti oleh 10 dan 7. Rating rendah (1-4) jauh lebih jarang.
- **Distribusi Usia:** Kolom `Age` memiliki beberapa nilai yang tidak realistis (misalnya 0 atau > 100). Setelah membersihkan data dan hanya mempertimbangkan usia antara 5 dan 100 tahun, distribusi usia menunjukkan puncak di sekitar usia 20-30 tahun dan 40-50 tahun.
- **Distribusi Tahun Publikasi:** Kolom `Year-Of-Publication` awalnya bertipe object dan mengandung beberapa nilai non-numerik serta tahun yang tidak valid (misalnya 0 atau tahun di masa depan). Setelah dibersihkan dan dikonversi menjadi numerik, distribusi menunjukkan peningkatan jumlah buku yang diterbitkan dari waktu ke waktu, dengan lonjakan signifikan mulai akhir tahun 1980-an hingga awal 2000-an.

## Data Preparation

Tahap persiapan data dilakukan untuk membersihkan dan mentransformasi data agar siap digunakan untuk pemodelan. Berikut adalah langkah-langkah yang dilakukan:

- **Penggabungan Data:** Data `Ratings` digabungkan dengan data `Books` berdasarkan kolom `ISBN` menggunakan _left merge_. Hal ini dilakukan untuk mendapatkan informasi detail buku untuk setiap rating yang diberikan.
- **Penanganan Missing Values:**
  - Nilai kosong pada `Book-Author` dan `Publisher` diisi dengan string 'Unknown'.
  - Nilai kosong pada `Age` diabaikan karena tidak digunakan langsung dalam model awal.
- **Mengatasi Sparsity Data (Filtering):** Untuk mengurangi sparsity dan fokus pada interaksi yang lebih signifikan, dilakukan filtering:
  - **Filter Buku:** Hanya buku yang memiliki minimal 10 rating yang dipertahankan.
  - **Filter Pengguna:** Hanya pengguna yang telah memberikan minimal 5 rating (pada buku-buku yang tersisa setelah filter pertama) yang dipertahankan.
  - Proses filtering ini mengurangi ukuran dataset menjadi ~456 ribu rating, dengan ~13.808 pengguna unik dan ~18.318 buku unik.
- **Reset Index:** Index DataFrame direset setelah filtering.

### Persiapan Fitur untuk Content-Based Filtering

- **Pembuatan Fitur Konten:** Kolom `Book-Author` dan `Publisher` digabungkan menjadi satu fitur teks (`content_features`) untuk setiap buku unik yang tersisa setelah tahap filtering.
- **Sampling Buku:** Karena keterbatasan sumber daya komputasi untuk menghitung matriks kemiripan pada seluruh buku, dilakukan pengambilan sampel acak sebanyak 5.000 buku unik. Proses selanjutnya untuk Content-Based Filtering dilakukan pada sampel ini.
- **Vectorisasi TF-IDF:** Fitur teks (`content_features`) dari buku-buku sampel diubah menjadi representasi vektor numerik menggunakan Term Frequency-Inverse Document Frequency (TF-IDF). TF-IDF memberikan bobot yang lebih tinggi pada kata-kata yang penting untuk suatu dokumen (buku) tetapi tidak terlalu umum di seluruh korpus (kumpulan buku).

### Persiapan Data untuk Collaborative Filtering

- **Penggunaan Rating Eksplisit:** Hanya rating eksplisit (nilai > 0) yang digunakan untuk Collaborative Filtering.
- **Sampling Pengguna dan Buku:** Untuk mengurangi ukuran matriks interaksi pengguna-item, dilakukan sampling:
  - Diambil sampel acak 5.000 pengguna dari pengguna yang tersisa setelah filtering.
  - Dari rating yang diberikan oleh pengguna sampel ini, diambil sampel acak 5.000 buku unik.
  - Dataset rating akhir yang digunakan untuk model Collaborative Filtering berisi interaksi antara 5.000 pengguna sampel dan 5.000 buku sampel (~20.740 rating).
- **Pembuatan Matriks User-Item:** Dibuat matriks pivot di mana baris mewakili pengguna (indeks sampel), kolom mewakili buku (indeks sampel), dan nilai sel adalah rating yang diberikan. Nilai kosong diisi dengan 0.

## Modeling

Pada tahap ini, dua pendekatan sistem rekomendasi diimplementasikan: Content-Based Filtering dan Collaborative Filtering.

### Content-Based Filtering

Pendekatan ini merekomendasikan buku berdasarkan kemiripan fitur konten buku itu sendiri. Setelah fitur konten buku diubah menjadi vektor numerik menggunakan TF-IDF pada tahap persiapan data, model menghitung kemiripan antar buku menggunakan _Cosine Similarity_. Untuk mendapatkan rekomendasi bagi suatu buku (berdasarkan ISBN), sistem mencari buku-buku lain dalam sampel yang memiliki skor kemiripan tertinggi dengan buku input tersebut. Daftar Top-N buku dengan skor tertinggi (tidak termasuk buku input itu sendiri) kemudian disajikan sebagai rekomendasi.

**Contoh Hasil Rekomendasi Content-Based (untuk ISBN 0425115801):**

```
|  No |     ISBN     |        Book-Title       |    Book-Author    |       Publisher       | Similarity_Score |
|-----|--------------|-------------------------|-------------------|-----------------------|------------------|
|  1  | 0425136981   | Shadowfires             | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  2  | 0425099334   | Shattered               | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  3  | 0425181111   | Strangers               | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  4  | 042511984X   | The Face of Fear        | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  5  | 0425132951   | The House of Thunder    | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  6  | 0425115801   | Lightning               | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  7  | 0425100650   | Twilight Eyes           | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  8  | 0425140032   | Dragon Tears            | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
|  9  | 0425130711   | Cold Fire               | Dean R. Koontz    | Berkley Publishing... |      1.000000    |
| 10  | 0425192032   | Lightning               | Dean Koontz       | Berkley               |      0.877481    |
```

### Collaborative Filtering (SVD)

Pendekatan ini merekomendasikan buku berdasarkan pola rating dari pengguna lain yang memiliki preferensi serupa. Setelah data disiapkan dalam bentuk matriks user-item pada tahap persiapan data, dilakukan faktorisasi matriks menggunakan Singular Value Decomposition (SVD). Matriks rating lengkap diprediksi dengan mengalikan kembali matriks hasil SVD. Untuk mendapatkan rekomendasi bagi pengguna tertentu, sistem mengambil baris prediksi rating pengguna tersebut dari matriks hasil prediksi, mengabaikan buku yang sudah pernah dirating, dan menyajikan Top-N buku dengan skor prediksi tertinggi.

**Contoh Hasil Rekomendasi Collaborative Filtering (SVD) untuk User-ID 276859 (dari sampel):**

```
|  No |     ISBN      |                Book-Title                                 |      Book-Author         |         Publisher           | Predicted_Rating |
|-----|---------------|-----------------------------------------------------------|--------------------------|-----------------------------|------------------|
|  1  | 1558743669    | A Child Called "It": One Child's Courage to Survive       | Dave Pelzer              | Health Communications       |     0.109432     |
|  2  | 0670894605    | The Secret Life of Bees                                   | Sue Monk Kidd            | Viking Books                |     0.094370     |
|  3  | 0345422783    | How Reading Changed My Life (Library of Contemporary...)  | Anna Quindlen            | Ballantine Books            |     0.092538     |
|  4  | 0877017883    | Griffin & Sabine: An Extraordinary Correspondence         | Nick Bantock             | Chronicle Books             |     0.092065     |
|  5  | 0805061762    | A Gentle Madness : Bibliophiles, Bibliomanes, and the...  | Nicholas A. Basbanes     | Owl Books                   |     0.090666     |
|  6  | 0385508417    | Skipping Christmas                                        | JOHN GRISHAM             | Doubleday                   |     0.089266     |
|  7  | 0451169522    | Misery                                                    | Stephen King             | Penguin USA (Paper)         |     0.089004     |
|  8  | 0451205073    | Last Breath                                               | Michael Prescott         | Signet Book                 |     0.088760     |
|  9  | 031242227X    | Running with Scissors: A Memoir                           | Augusten Burroughs       | Picador USA                 |     0.087961     |
| 10  | 0345423097    | Joy School (Ballantine Reader's Circle)                   | ELIZABETH BERG           | Ballantine Books            |     0.086778     |
```

## Evaluation

Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.
Evaluasi dilakukan untuk mengukur kinerja model rekomendasi yang telah dibangun.

### Metrik Evaluasi

- **Collaborative Filtering (SVD):** Metrik yang digunakan adalah **Root Mean Squared Error (RMSE)**. RMSE mengukur rata-rata akar kuadrat dari selisih antara rating aktual yang diberikan pengguna dan rating yang diprediksi oleh model. Nilai RMSE yang lebih rendah menunjukkan performa model yang lebih baik dalam memprediksi rating.
  - **Rumus:** `RMSE = sqrt(mean((actual_rating - predicted_rating)^2))`
- **Content-Based Filtering:** Pada implementasi ini, belum dilakukan evaluasi kuantitatif formal menggunakan metrik standar seperti _Precision@k_ atau _Recall@k_ karena keterbatasan data ground truth untuk relevansi rekomendasi. Kualitas rekomendasi dinilai secara kualitatif berdasarkan relevansi hasil rekomendasi yang dihasilkan oleh model.

### Hasil Evaluasi

- **Collaborative Filtering (SVD):** RMSE yang diperoleh pada **data training (sampel CF)** adalah **6.5812**.
  - **Penting untuk dicatat:** Nilai RMSE ini dihitung pada data yang sama yang digunakan untuk melatih model SVD (karena tidak ada pemisahan data test eksplisit dalam implementasi ini) dan pada data hasil sampling. Oleh karena itu, nilai ini mungkin tidak sepenuhnya mencerminkan kinerja model pada data baru atau pada keseluruhan dataset. Nilai RMSE yang relatif tinggi juga bisa disebabkan oleh sparsity data atau sifat rating itu sendiri.
- **Content-Based Filtering:** Rekomendasi didasarkan pada kemiripan konten (penulis dan penerbit). Contoh hasil menunjukkan buku-buku dengan penulis dan penerbit yang sama mendapatkan skor kemiripan tertinggi, yang secara intuitif masuk akal untuk pendekatan berbasis konten ini.

### Analisis Hasil

- **Collaborative Filtering (SVD):** Meskipun RMSE memberikan gambaran tentang akurasi prediksi rating, metrik ini kurang ideal untuk mengevaluasi kualitas rekomendasi Top-N. Metrik seperti _Precision@k_ dan _Recall@k_ akan lebih cocok untuk mengukur seberapa relevan item yang direkomendasikan dalam daftar Top-N, namun memerlukan implementasi yang lebih kompleks dengan pemisahan data test.
- **Content-Based Filtering:** Pendekatan ini efektif dalam menemukan buku yang secara konten mirip dengan preferensi pengguna (berdasarkan penulis/penerbit). Kelemahannya adalah kurangnya _serendipity_ (kemampuan menemukan item baru yang berbeda tetapi mungkin disukai pengguna) dan ketergantungan pada kualitas fitur konten yang tersedia.
- **Perbandingan:** Kedua model memberikan jenis rekomendasi yang berbeda. CF memanfaatkan kebijaksanaan kolektif pengguna, sementara CB fokus pada atribut item. Penggunaan sampling karena keterbatasan resource mempengaruhi cakupan dan mungkin akurasi kedua model dibandingkan jika dijalankan pada data penuh.

Secara keseluruhan, proyek ini berhasil mengimplementasikan kedua pendekatan rekomendasi dengan penyesuaian untuk mengatasi keterbatasan sumber daya. Evaluasi memberikan indikasi awal kinerja, meskipun evaluasi lebih lanjut dengan metrik yang sesuai dan data test terpisah akan memberikan pemahaman yang lebih mendalam.
