# Laporan Proyek Machine Learning - Dina Prastuti

## Domain Proyek

Pemberian pinjaman merupakan proses penting dalam industri keuangan. Kesalahan dalam menilai risiko pemohon dapat menyebabkan kerugian finansial akibat gagal bayar. Menurut Basel Committee on Banking Supervision (2019), 23% kerugian bank global disebabkan oleh kesalahan penilaian risiko kredit.

Permasalahan ini perlu diselesaikan karena:

- **Kerugian Finansial:** Bank kehilangan rata-rata jutaan dolar per tahun akibat kesalahan manual dalam penilaian pinjaman.
- **Ketidakakuratan Subjektif:** Analisis manual oleh manusia memiliki tingkat kesalahan 15-20% (Brown & Mues, 2012).
- **Skalabilitas:** Volume aplikasi pinjaman meningkat pesat, sehingga dibutuhkan solusi otomatis dan efisien.

Solusi yang diusulkan adalah membangun model machine learning untuk memprediksi status persetujuan pinjaman (LoanApproved) berdasarkan profil demografis dan finansial pemohon.

Referensi:

- Basel Committee on Banking Supervision. (2019). Credit risk modelling: Current practices and applications. Bank for International Settlements. https://www.bis.org/bcbs/publ/d457.htm
- Brown, I., & Mues, C. (2012). An experimental comparison of classification algorithms for imbalanced credit scoring data sets. Expert Systems with Applications, 39(3), 3446–3453. https://doi.org/10.1016/j.eswa.2011.09.033
- Zoppelletto, L. (2023). Financial Risk for Loan Approval. Kaggle. https://www.kaggle.com/datasets/lorenzozoppelletto/financial-risk-for-loan-approval

---

## Business Understanding

### Problem Statements

1. Evaluasi risiko pemohon pinjaman secara manual rentan terhadap kesalahan subjektif, sehingga dapat menyebabkan keputusan yang tidak akurat.
2. Tingginya biaya operasional akibat proses seleksi yang tidak efisien, karena volume aplikasi pinjaman yang terus meningkat.
3. Belum adanya sistem otomatis yang dapat membantu bank dalam mengambil keputusan persetujuan pinjaman secara objektif dan cepat.

### Goals

1. Membangun model klasifikasi dengan akurasi ≥85% untuk memprediksi persetujuan pinjaman sehingga dapat mengurangi kesalahan subjektif dalam evaluasi risiko.
2. Mengidentifikasi faktor dominan yang memengaruhi keputusan persetujuan pinjaman untuk membantu bank memahami aspek penting dalam proses seleksi.
3. Mengimplementasikan sistem otomatis berbasis machine learning yang dapat meningkatkan efisiensi proses seleksi pinjaman.

### Solution Statements

- Menggunakan dua algoritma: Logistic Regression dan Random Forest untuk membandingkan performa prediksi.
- Melakukan penyeimbangan kelas dengan SMOTE agar model tidak bias terhadap kelas mayoritas.
- Mengukur performa model dengan metrik: accuracy, precision, recall, F1-score, ROC-AUC.
- Memilih model terbaik berdasarkan hasil evaluasi dan interpretasi feature importance.

---

## Data Understanding

### Pengantar

Dataset yang digunakan adalah **Financial Risk for Loan Approval** (Zoppelletto, 2023) dari Kaggle. Dataset ini berisi data pemohon pinjaman dengan berbagai fitur demografi, keuangan, dan histori kredit.

### Sumber Data

- URL: https://www.kaggle.com/datasets/lorenzozoppelletto/financial-risk-for-loan-approval

### Jumlah Data

- **Jumlah baris:** 20.000
- **Jumlah kolom:** 36

### Kondisi Data

- **Missing Value:** Tidak terdapat missing value pada seluruh fitur, sehingga tidak diperlukan proses imputasi pada data yang digunakan untuk modeling.
- **Duplikat:** Tidak ditemukan data duplikat pada dataset (sudah dicek dengan `df.duplicated().sum()`).
- **Outlier:** Outlier terdeteksi pada beberapa fitur numerik seperti `AnnualIncome` dan `CreditScore` (dilihat dari boxplot), namun tidak dilakukan penghapusan agar tetap merepresentasikan variasi data nyata.
- **Distribusi Target:** Data cukup imbalance, dengan proporsi kelas 0 (tidak disetujui) sekitar 76.1% dan kelas 1 (disetujui) sekitar 23.9%.

### Uraian Seluruh Fitur Dataset

1. ApplicationDate: Tanggal pengajuan pinjaman
2. Age: Usia pemohon
3. AnnualIncome: Pendapatan tahunan
4. CreditScore: Skor kredit
5. EmploymentStatus: Status pekerjaan
6. EducationLevel: Tingkat pendidikan terakhir
7. Experience: Lama pengalaman kerja (tahun)
8. LoanAmount: Jumlah pinjaman yang diajukan
9. LoanDuration: Lama periode pembayaran pinjaman (bulan/tahun)
10. MaritalStatus: Status pernikahan pemohon
11. NumberOfDependents: Jumlah tanggungan
12. HomeOwnershipStatus: Status kepemilikan rumah
13. MonthlyDebtPayments: Cicilan/hutang bulanan
14. CreditCardUtilizationRate: Persentase pemanfaatan limit kartu kredit
15. NumberOfOpenCreditLines: Jumlah jalur kredit aktif
16. NumberOfCreditInquiries: Jumlah pengecekan kredit
17. DebtToIncomeRatio: Rasio hutang bulanan terhadap penghasilan
18. BankruptcyHistory: Riwayat kebangkrutan (0 = tidak pernah, 1 = pernah)
19. LoanPurpose: Tujuan pinjaman
20. PreviousLoanDefaults: Riwayat gagal bayar pinjaman sebelumnya
21. PaymentHistory: Riwayat pembayaran
22. LengthOfCreditHistory: Lama riwayat kredit
23. SavingsAccountBalance: Saldo rekening tabungan
24. CheckingAccountBalance: Saldo rekening giro
25. TotalAssets: Total aset yang dimiliki
26. TotalLiabilities: Total kewajiban/utang
27. MonthlyIncome: Pendapatan bulanan
28. UtilityBillsPaymentHistory: Riwayat pembayaran tagihan utilitas
29. JobTenure: Lama bekerja di pekerjaan saat ini
30. NetWorth: Kekayaan bersih (aset - liabilitas)
31. BaseInterestRate: Suku bunga dasar
32. InterestRate: Suku bunga aktual
33. MonthlyLoanPayment: Pembayaran pinjaman per bulan
34. TotalDebtToIncomeRatio: Rasio total hutang terhadap pendapatan
35. LoanApproved: Target, status persetujuan pinjaman (0 = tidak disetujui, 1 = disetujui)
36. RiskScore: Skor risiko

---

## Data Preparation

1. **Seleksi Fitur:**  
   Memilih fitur yang relevan untuk prediksi persetujuan pinjaman, mengacu pada fitur demografi, keuangan, dan histori kredit. Fitur yang tidak digunakan: `ApplicationDate`, `RiskScore`.

2. **Penanganan Missing Value:**

   - Fitur numerik: Missing value diisi dengan median.
   - Fitur kategorikal: Missing value diisi dengan modus.

3. **Cek dan Penanganan Duplikasi:**  
   Mengecek dan memastikan tidak ada data duplikat pada dataset.

4. **Cek dan Penanganan Outlier:**  
   Melakukan visualisasi boxplot pada fitur numerik utama untuk mendeteksi outlier, namun tidak dilakukan penghapusan agar variasi data tetap terjaga.

5. **Split Data:**  
   Data dibagi menjadi 80% data latih dan 20% data uji, dengan stratifikasi pada target.

6. **Encoding:**  
   Fitur kategorikal diubah menjadi numerik menggunakan OneHotEncoder.

7. **Scaling:**  
   Fitur numerik dinormalisasi menggunakan StandardScaler.

8. **Penyeimbangan Kelas:**  
   Menggunakan SMOTE pada data latih untuk mengatasi imbalance pada target.

---

## Modeling

### Model 1: Logistic Regression

**Cara Kerja:**  
Logistic Regression adalah model klasifikasi linear yang memodelkan probabilitas suatu data termasuk ke kelas tertentu menggunakan fungsi logit (sigmoid). Model ini menghasilkan koefisien untuk setiap fitur yang dapat diinterpretasikan sebagai pengaruh fitur terhadap peluang persetujuan pinjaman.

**Parameter:**

- random_state=42 (untuk reprodusibilitas)
- max_iter=1000 (jumlah iterasi maksimum)
- Parameter lain menggunakan default.

**Kelebihan/Kekurangan:**

- Kelebihan: Sederhana, cepat, interpretatif, cocok untuk baseline.
- Kekurangan: Kurang menangkap relasi non-linear antar fitur.

---

### Model 2: Random Forest Classifier

**Cara Kerja:**  
Random Forest adalah model ensemble berbasis pohon keputusan yang membangun banyak pohon secara acak dan menggabungkan hasil voting mayoritas. Dapat menangkap relasi non-linear dan interaksi antar fitur.

**Parameter:**

- random_state=42 (untuk reprodusibilitas)
- Parameter lain menggunakan default.

**Kelebihan/Kekurangan:**

- Kelebihan: Kuat untuk data tabular, mampu menangkap relasi non-linear, dapat mengukur feature importance.
- Kekurangan: Lebih kompleks, rawan overfitting jika tidak diatur, interpretasi lebih sulit dibanding Logistic Regression.

---

## Evaluation

### Metrik Evaluasi

- Accuracy: Proporsi prediksi benar dari seluruh data.
- Precision: Ketepatan model saat memprediksi “disetujui”.
- Recall: Kemampuan model mendeteksi semua pinjaman yang seharusnya disetujui.
- F1 Score: Harmonis antara precision dan recall.
- ROC-AUC: Area di bawah kurva ROC, mengukur kemampuan model membedakan kelas.

### Hasil Evaluasi

Perbandingan Model Klasifikasi: Logistic Regression vs Random Forest

| Model               | Accuracy | Precision | Recall | F1-Score | ROC AUC |
| ------------------- | -------- | --------- | ------ | -------- | ------- |
| Logistic Regression | 0.9630   | 0.8907    | 0.9634 | 0.9256   | 0.9948  |
| Random Forest       | 0.9268   | 0.8338    | 0.8661 | 0.8497   | 0.9778  |

**Classification Report**

| Model               | Metric    | Class 0 | Class 1 | Macro Avg |
| ------------------- | --------- | ------- | ------- | --------- |
| Logistic Regression | Precision | 0.99    | 0.89    | 0.94      |
|                     | Recall    | 0.96    | 0.96    | 0.96      |
|                     | F1-Score  | 0.98    | 0.93    | 0.95      |
|                     | Support   | 3044    | 956     | -         |
| Random Forest       | Precision | 0.96    | 0.83    | 0.90      |
|                     | Recall    | 0.95    | 0.87    | 0.91      |
|                     | F1-Score  | 0.95    | 0.85    | 0.90      |
|                     | Support   | 3044    | 956     | -         |

**Visualisasi ROC Curve**

- Logistic Regression AUC: 0.9948
- Random Forest AUC: 0.9778

### Penentuan Model Terbaik

Berdasarkan hasil evaluasi, **Logistic Regression** merupakan model terbaik karena memiliki nilai F1-Score dan ROC-AUC yang lebih tinggi dibandingkan Random Forest.

---

## Hubungan dengan Business Understanding

- **Problem Statement 1:** Model machine learning yang dibangun berhasil mengurangi kesalahan subjektif dalam evaluasi risiko, terbukti dari akurasi dan F1-Score yang tinggi.
- **Problem Statement 2:** Proses seleksi pinjaman menjadi lebih efisien dan otomatis, mengurangi biaya operasional dan waktu proses.
- **Problem Statement 3:** Sistem otomatis berbasis machine learning telah diimplementasikan dan terbukti efektif dalam memprediksi persetujuan pinjaman.

**Goals tercapai:**

- Model klasifikasi mencapai akurasi di atas 85% (Logistic Regression: 96.3%).
- Faktor dominan yang memengaruhi keputusan pinjaman dapat diidentifikasi melalui analisis koefisien Logistic Regression (misal: TotalDebtToIncomeRatio, InterestRate, MonthlyIncome).
- Sistem otomatis berbasis machine learning telah berhasil dibangun dan dievaluasi.

**Solusi yang direncanakan berdampak positif** terhadap proses bisnis, meningkatkan akurasi, efisiensi, dan objektivitas dalam proses persetujuan pinjaman.

---

## Kesimpulan

- Model Logistic Regression memberikan performa terbaik untuk prediksi persetujuan pinjaman pada dataset ini.
- Fitur-fitur seperti `TotalDebtToIncomeRatio`, `InterestRate`, dan `MonthlyIncome` memiliki pengaruh besar terhadap keputusan persetujuan pinjaman.
- Model dapat digunakan sebagai alat bantu dalam proses seleksi awal persetujuan pinjaman, namun tetap perlu evaluasi lebih lanjut sebelum diterapkan pada data nyata.
