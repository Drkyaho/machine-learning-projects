# Sentiment Analysis Project: Play Store Reviews – Block Blast Game

This project focuses on performing **sentiment analysis** on user reviews of the **Block Blast** game from the Google Play Store. The dataset was collected through **web scraping**, followed by data preprocessing, feature extraction, and sentiment labeling.

Machine learning algorithms were then applied to train and evaluate sentiment classification models.

## Project Overview

The project follows a sentiment analysis workflow consisting of:

1. **Data Collection** — Scraped user reviews of the Block Blast game from the Google Play Store.
2. **Data Preprocessing** — Prepared and cleaned the collected review data for analysis.
3. **Feature Extraction** — Transformed review text into numerical features suitable for machine learning.
4. **Data Labeling** — Assigned sentiment labels to the review data.
5. **Model Training** — Trained multiple machine learning classification algorithms.
6. **Model Evaluation** — Compared model performance using accuracy on the training and testing datasets.

## 🤖 Machine Learning Models

Two models achieved the highest performance:

* **Random Forest**
* **Logistic Regression**

Both models achieved an accuracy of **93.58%** on the training and testing sets, exceeding the target accuracy of **92%**.

Based on the evaluation results, **either Random Forest or Logistic Regression can be selected as the main predictor** for classifying the sentiment of new Block Blast review texts.

## Results

| Model               | Training Accuracy | Testing Accuracy |
| ------------------- | ----------------: | ---------------: |
| Random Forest       |            93.58% |           93.58% |
| Logistic Regression |            93.58% |           93.58% |

The results indicate that both models performed consistently across the training and testing datasets.

## 🛠️ Technologies & Techniques

* Python
* Jupyter Notebook
* Web Scraping
* Natural Language Processing (NLP)
* Feature Extraction
* Sentiment Analysis
* Random Forest
* Logistic Regression
* Scikit-learn

## Learning Outcomes

This project strengthened my understanding of **text-based machine learning workflows**, from collecting real-world data through web scraping and preprocessing text to feature extraction, sentiment labeling, model training, and evaluation.

It also provided practical experience in applying **Natural Language Processing and machine learning classification techniques** to analyze user feedback and sentiment.

