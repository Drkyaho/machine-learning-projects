# Simple ETL Pipeline

## 📌 Project Overview

This project is a final project focused on building a simple ETL (Extract, Transform, Load) pipeline using modular code principles.

The project covers the following key aspects:

- Building an ETL Pipeline using modular code principles
- Extracting data through web scraping
- Transforming and cleaning the extracted data
- Loading processed data into a data repository
- Implementing unit testing
- Measuring test coverage

---

## 📂 Project Structure

```text
Membangun-ETL-Pipeline-Sederhana/
│
├── tests/                 # Unit tests for the ETL pipeline
│   ├── README.md
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_load.py
│   └── test_transform.py
│
├── utils/                 # ETL modules
│   ├── README.md
│   ├── __init__.py
│   ├── extract.py         # Data extraction process
│   ├── transform.py       # Data transformation process
│   └── load.py            # Data loading process
│
├── README.md              # Project documentation
├── main.py                # Main script to run the ETL pipeline
├── products.csv           # Output dataset
├── requirements.txt       # Project dependencies
└── submission.txt         # Submission documentation
```

---

## ⚙️ Installation

Clone this repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Membangun-ETL-Pipeline-Sederhana
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔄 ETL Pipeline

The ETL pipeline consists of three main processes:

### 1. Extract

The extraction process collects product data through web scraping from pages 1 to 50.

### 2. Transform

The extracted raw data is processed, cleaned, and transformed into a structured format.

### 3. Load

The processed data is stored as:

```text
products.csv
```

---

## 🚀 How to Run the ETL Pipeline

Run the following command from the project's root directory:

```bash
python main.py
```

The output will display:

- The scraping process from page 1 to page 50
- The total amount of raw data collected
- The total amount of data after transformation
- Confirmation that the processed data has been successfully saved to `products.csv`

---

## 🧪 Running Unit Tests

To run all unit tests inside the `tests` folder, use:

```bash
pytest tests/ --import-mode=append
```

This command will run the following test files:

- `test_extract.py`
- `test_transform.py`
- `test_load.py`

---

## 📊 Test Coverage

To measure unit test coverage for the modules inside the `utils` folder, run:

```bash
pytest tests/ --import-mode=append --cov=utils --cov-report=term-missing
```

This command displays the percentage of code covered by unit tests and identifies lines that have not yet been tested.

The project achieved a total test coverage of **93%**.

---

## 🛠️ Technologies and Tools

- Python
- Web Scraping
- Pandas
- Pytest
- Pytest-Cov

---

## 🎯 Learning Objectives

Through this project, I learned how to:

- Build a simple ETL pipeline
- Apply modular programming principles
- Extract data through web scraping
- Transform and clean raw data
- Store processed data in a data repository
- Implement unit testing
- Measure test coverage

---

## 👤 Author

**Dina Prastuti**

Information Systems Graduate  
Interested in Data Science, Data Analytics, and Machine Learning
