# Machine Learning Project: Fraud Detection in Bank Transactions

This project focuses on detecting fraudulent bank transactions using machine learning techniques. The project uses the **Bank Transaction Dataset for Fraud Detection** sourced from Kaggle and consists of two main tasks: **clustering** and **classification**.

## Project Overview

The project was developed using **Python** and implemented in two Jupyter Notebooks:

1. **Clustering** — uses the original `bank_transactions_data.csv` dataset to identify patterns and group similar transactions using the K-Means algorithm.
2. **Classification** — uses the labeled `hasil_clustering.csv` dataset generated from the clustering process to build classification models for detecting fraudulent transactions.

## 🛠️ Key Steps & Techniques

* Performed **feature selection** to identify relevant attributes for the clustering process.
* Applied **K-Means Clustering** to uncover hidden patterns and group similar transactions.
* Generated labeled transaction data through the clustering results.
* Applied multiple **classification models** to detect fraudulent transactions.
* Evaluated model performance using **Accuracy** and **F1-Score**.
* Achieved **≥92% Accuracy and F1-Score** on both training and testing sets.

## Project Structure

```text
fraud-detection-bank-transactions/
├── fraud_detection_clustering.ipynb
├── fraud_detection_classification.ipynb
├── bank_transactions_data.csv
├── hasil_clustering.csv
└── README.md
```

### File Description

| File                                   | Description                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------- |
| `fraud_detection_clustering.ipynb`     | Jupyter Notebook containing the feature selection and K-Means clustering process.           |
| `fraud_detection_classification.ipynb` | Jupyter Notebook containing the classification process and model evaluation.                |
| `bank_transactions_data.csv`           | Original bank transaction dataset used for the analysis and clustering process.             |
| `hasil_clustering.csv`                 | Dataset containing the clustering results used as labeled data for the classification task. |
| `README.md`                            | Documentation describing the project.                                                       |

## Technologies

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

## Learning Outcomes

This project strengthened my understanding of **machine learning workflows**, including feature selection, unsupervised learning, supervised classification, and model evaluation. It also provided practical experience in applying machine learning techniques to **fraud detection in the financial domain**.
