# 🦋 Butterfly & Moths Image Classification (100 Species)

A deep learning project for classifying **100 species of butterflies and moths** using a Convolutional Neural Network (CNN) with **transfer learning** and advanced model optimization techniques.

🔗 **Dataset:** [Butterfly & Moths Image Classification (100 Species)](https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species)

---

## 📊 Dataset

The project uses the **Butterfly & Moths Image Classification 100 species** dataset from Kaggle.

| Dataset           |      Number |
| ----------------- | ----------: |
| Classes           | 100 species |
| Training Images   |      12,594 |
| Validation Images |         500 |
| Testing Images    |         500 |

The dataset is organized in a directory structure compatible with Keras `ImageDataGenerator`.

---

## ✨ Key Features

### 🧠 Model Architecture

The classification model uses **MobileNetV2 with transfer learning**, combined with additional layers for improved classification performance.

Key components include:

* MobileNetV2 pretrained architecture
* Batch Normalization
* Dropout
* Transfer learning

### 🎛️ Data Augmentation

`ImageDataGenerator` was used to improve model generalization through:

* Random rotation
* Random zoom
* Horizontal flipping
* Brightness adjustment

### ⚙️ Model Optimization

Several techniques were implemented during training:

* **ModelCheckpoint** — saves the best-performing model.
* **EarlyStopping** — stops training when validation performance no longer improves.
* **ReduceLROnPlateau** — reduces the learning rate when validation performance plateaus.
* **Adam Optimizer** — initial learning rate of `0.001`.

---

## 📈 Model Performance

The model achieved a **96.00% validation accuracy** at epoch 49 and **97.00% testing accuracy**.

### Training Progress

| Epoch | Train Accuracy | Val Accuracy | Val Loss | Learning Rate |
| ----: | -------------: | -----------: | -------: | ------------: |
|     1 |          2.65% |        4.20% |   5.2687 |        0.0010 |
|     5 |         32.68% |       50.60% |   1.7026 |        0.0010 |
|    10 |         54.39% |       68.40% |   1.1019 |        0.0010 |
|    15 |         67.53% |       81.20% |   0.6459 |        0.0010 |
|    20 |         73.41% |       85.40% |   0.4518 |        0.0010 |
|    25 |         78.49% |       90.40% |   0.3663 |        0.0010 |
|    30 |         81.32% |       87.80% |   0.4495 |        0.0010 |
|    35 |         85.47% |       94.60% |   0.2463 |        0.0005 |
|    40 |         88.08% |       93.40% |   0.2575 |        0.0005 |
|    45 |         89.98% |       95.20% |   0.1939 |       0.00025 |
|    49 |         90.25% |   **96.00%** |   0.1940 |       0.00025 |

### Testing Results

```text
Test Accuracy : 97.00%
Test Loss     : 0.1321
```

Training was conducted for up to **50 epochs** using EarlyStopping and ModelCheckpoint to retain the best-performing model.

---

## 📦 Model Files

Due to the size of the trained model files, some files are provided through **Google Drive**.

### 🔗 `URL.txt`

The `URL.txt` file contains the **Google Drive link** to the files that are not directly stored in this repository.

### 📁 `saved_model/`

The `saved_model/` folder contains the TensorFlow SavedModel structure. The **`variables/`** folder is represented through a Google Drive link because the model variable files are too large to store directly in the repository.

```text
saved_model/
├── saved_model.pb
├── fingerprint.pb/
└── URL.txt/
```

The `URL.txt` folder provides access to the Google Drive link containing the required **model variable files**.

### 📁 `tflite/`

The `tflite/` folder contains the TensorFlow Lite version of the model along with its corresponding class labels.

```text
tflite/
├── model.tflite
└── label.txt
```

* **`model.tflite`** — TensorFlow Lite model used for lightweight deployment.
* **`label.txt`** — contains the class labels corresponding to the model's 100 butterfly and moth species.

---

## 🗂️ Project Structure

```text
submission/
├── saved_model/
│   ├── saved_model.pb
│   └── variables/
│       └── README.md
├── tflite/
│   ├── model.tflite
│   └── label.txt
├── URL.txt
├── notebook.ipynb
├── README.md
└── requirements.txt
```

---

## 🧰 Technologies

* **Python 3.11+**
* **TensorFlow 2.12+**
* **Keras**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Google Colab**
* **GPU Acceleration**
* **Google Drive**

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Notebook

Open `Submission_Akhir.ipynb` in Jupyter Notebook or Google Colab and run the cells sequentially.

Make sure the dataset is available at the path specified in the notebook before starting the training process.

### 3. Access the Model Files

For the complete TensorFlow SavedModel, use the Google Drive link provided in `URL.txt` or the `README.md` inside the `saved_model/variables/` folder.

For TensorFlow Lite deployment, use the files available directly in the `tflite/` folder.

---

## 📌 Conclusion

This project successfully developed an image classification model capable of distinguishing **100 butterfly and moth species** using transfer learning with MobileNetV2.

The model achieved **96.00% validation accuracy** and **97.00% testing accuracy**, demonstrating strong performance in classifying butterfly and moth species from images.
