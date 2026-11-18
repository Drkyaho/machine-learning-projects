# Sentiment Analysis: Block Blast Game Reviews

## Project Overview

This project analyzes user reviews of the Block Blast game collected from the Google Play Store to identify positive and negative user sentiments.

The dataset was collected through web scraping and processed using Natural Language Processing (NLP) techniques. Sentiment labels were generated using an Indonesian sentiment lexicon, followed by TF-IDF feature extraction and machine learning classification.

The objective was to explore user feedback and compare different machine learning models for sentiment classification.

## Project Workflow

1. **Data Collection** — Used previously scraped Google Play Store reviews of the Block Blast game.
2. **Data Cleaning** — Removed missing values and duplicate records from the collected dataset.
3. **Text Preprocessing** — Applied text cleaning, case folding, slang normalization, tokenization, and stopword removal.
4. **Sentiment Labeling** — Assigned positive and negative sentiment labels using an Indonesian sentiment lexicon.
5. **Feature Extraction** — Converted processed review text into numerical representations using TF-IDF and N-gram techniques.
6. **Model Training** — Trained and compared Bernoulli Naive Bayes, Random Forest, and Logistic Regression classifiers.
7. **Model Evaluation** — Evaluated model performance using training and testing accuracy.

## Dataset

- **Source:** Google Play Store reviews of Block Blast
- **Initial records:** 31,638 reviews
- **Records after removing missing values:** 20,640 reviews
- **Sentiment classes:** Positive and Negative

The sentiment distribution after lexicon-based labeling:
- Positive: 14,194 reviews
- Negative: 6,446 reviews

## Machine Learning Models

Three classification models were evaluated using different text feature extraction approaches:

- **Bernoulli Naive Bayes** — TF-IDF features
- **Random Forest** — N-gram features (unigram and bigram)
- **Logistic Regression** — TF-IDF features

## Model Performance

| Model | Training Accuracy | Testing Accuracy |
|---|---:|---:|
| Bernoulli Naive Bayes | 89.32% | 90.41% |
| Random Forest | 100.00% | 93.75% |
| Logistic Regression | 93.50% | 93.58% |

Random Forest achieved the highest testing accuracy of **93.75%**, followed by Logistic Regression at **93.58%**.

## Technologies & Techniques

- Python
- Jupyter Notebook / Google Colab
- Pandas and NumPy
- Matplotlib and Seaborn
- Natural Language Processing (NLP)
- NLTK
- Sastrawi
- Text Preprocessing
- Sentiment Lexicon
- TF-IDF
- N-gram Feature Extraction
- Scikit-learn
- Bernoulli Naive Bayes
- Random Forest
- Logistic Regression

## Learning Outcomes

This project provided practical experience in building a text classification workflow, including collecting user reviews, preprocessing Indonesian text, generating sentiment labels using a lexicon-based approach, extracting text features, and training machine learning classifiers.

It also strengthened my understanding of NLP techniques and model comparison for analyzing user feedback.
