# Machine Learning Project: Fraud Detection in Bank Transactions

This project focuses on detecting fraudulent bank transactions using machine learning techniques. The project uses the **Bank Transaction Dataset for Fraud Detection** sourced from Kaggle and consists of two main tasks: **clustering** and **classification**.

## Project Overview

The project was developed using **Python** and implemented in two Jupyter Notebooks:

1. **Clustering** — uses an unlabeled `.csv` dataset to identify patterns and group transactions based on their characteristics.
2. **Classification** — uses a labeled dataset generated from the clustering results to build models for detecting fraudulent transactions.

## Key Steps & Techniques

* Performed **feature selection** to identify the most relevant attributes for the clustering process.
* Applied **K-Means Clustering** to discover hidden patterns and group similar transactions.
* Generated labeled data based on the clustering results for the classification task.
* Applied multiple **classification algorithms** to identify fraudulent transactions.
* Evaluated model performance using **Accuracy** and **F1-Score**.
* Achieved **≥92% Accuracy and F1-Score** on both training and testing sets.

## Project Structure

```text
fraud-detection-bank-transactions/
├── clustering/
│   └── fraud_detection_clustering.ipynb
├── classification/
│   └── fraud_detection_classification.ipynb
├── data/
│   ├── bank_transactions_unlabeled.csv
│   └── bank_transactions_labeled.csv
└── README.md
```

## Technologies

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn

## Learning Outcomes

This project strengthened my understanding of **end-to-end machine learning workflows**, including feature selection, unsupervised learning, supervised classification, and model evaluation. It also provided practical experience in applying machine learning techniques to **fraud detection in the financial domain**.

