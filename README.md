# Machine Learning Project: Bank Transaction Clustering & Classification

## Project Overview

This project explores bank transaction patterns using unsupervised and supervised machine learning techniques. It uses the **Bank Transaction Dataset for Fraud Detection** sourced from Kaggle, containing 2,512 transaction records without predefined fraud labels.

The project consists of two main stages implemented in separate Jupyter Notebooks:

1. **Clustering** — applies K-Means to group transactions based on selected financial and customer attributes, followed by feature selection to improve cluster separation.
2. **Classification** — trains Decision Tree and Random Forest models to predict cluster assignments generated during the clustering process.

Since the original dataset does not contain ground-truth fraud labels, this project focuses on transaction pattern analysis and cluster classification rather than validating actual fraudulent transactions.

## Dataset Description

- **Dataset:** Bank Transaction Dataset for Fraud Detection
- **Source:** Kaggle
- **Original Records:** 2,512
- **Original Features:** 16
- **Target Labels:** None (unlabeled dataset)
- **Records After Outlier Removal:** 2,282

The dataset includes transaction, account, and customer attributes, such as:

**Numerical Features**
- `TransactionAmount`
- `AccountBalance`
- `TransactionDuration`
- `CustomerAge`
- `LoginAttempts`

**Categorical Features**
- `TransactionType`
- `Location`
- `Channel`
- `CustomerOccupation`

## Key Steps & Techniques

### 1. Exploratory Data Analysis (EDA)
- Examined dataset structure, data types, and missing values.
- Analyzed numerical distributions, outliers, and correlations.
- Visualized categorical feature distributions.

### 2. Data Preprocessing
- Checked and removed duplicate records.
- Handled outliers using the Interquartile Range (IQR) method.
- Standardized numerical features using StandardScaler.
- Encoded categorical variables using LabelEncoder.

### 3. K-Means Clustering
- Applied K-Means with 5 clusters to group similar transactions.
- Used the Elbow Method and Silhouette Score to evaluate clustering quality.
- Performed feature selection using VarianceThreshold.
- Compared clustering results before and after feature selection.

**Clustering Results:**

| Experiment | Silhouette Score |
|---|---:|
| Before Feature Selection | 0.32 |
| After Feature Selection | 0.51 |

Feature selection retained `TransactionType`, `Channel`, and `CustomerOccupation`, resulting in a higher Silhouette Score.

### 4. Cluster Classification
- Used the generated cluster assignments as pseudo-labels for supervised classification.
- Trained Decision Tree and Random Forest models.
- Applied GridSearchCV for hyperparameter tuning.
- Evaluated model performance using Accuracy, Weighted F1-Score, Precision, Recall, and Confusion Matrix.

**Classification Results:**

| Model | Accuracy | Weighted F1-Score |
|---|---:|---:|
| Decision Tree | 93.87% | 93.86% |
| Random Forest | 96.94% | 96.94% |
| Tuned Decision Tree | 96.06% | 96.04% |
| Tuned Random Forest | 96.28% | 96.30% |

Random Forest achieved the highest initial classification performance, while hyperparameter tuning resulted in slightly different performance across both models.

*Note: Classification metrics measure the models' ability to predict generated cluster labels, not their ability to detect actual fraudulent transactions.*

## Project Structure

```text
fraud-detection-in-bank-transactions/
├── fraud_detection_clustering.ipynb
├── fraud_detection_classification.ipynb
├── bank_transactions_data.csv
├── hasil_clustering.csv
└── README.md
```

### File Description

| File | Description |
|---|---|
| `fraud_detection_clustering.ipynb` | Notebook covering EDA, preprocessing, K-Means clustering, feature selection, and cluster analysis. |
| `fraud_detection_classification.ipynb` | Notebook covering Decision Tree and Random Forest classification, hyperparameter tuning, and model evaluation. |
| `bank_transactions_data.csv` | Original unlabeled bank transaction dataset. |
| `hasil_clustering.csv` | Dataset containing generated cluster assignments used in the classification stage. |
| `README.md` | Project documentation. |

## Technologies

- Python
- Jupyter Notebook / Google Colab
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Learning Outcomes

This project provided practical experience in applying unsupervised and supervised machine learning workflows to financial transaction data. Key learning areas included exploratory data analysis, data preprocessing, K-Means clustering, feature selection, pseudo-label generation, classification, hyperparameter tuning, and model evaluation.

The project also demonstrated the importance of understanding the limitations of unlabeled datasets when applying machine learning to fraud-related use cases.
