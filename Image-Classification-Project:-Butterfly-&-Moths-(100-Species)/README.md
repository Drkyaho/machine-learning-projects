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

The classification model combines a custom CNN structure with **MobileNetV2 transfer learning**.

Key components include:

* MobileNetV2 pretrained architecture
* Batch Normalization
* Dropout
* Transfer learning for improved image classification performance

### 🎛️ Data Augmentation

`ImageDataGenerator` was used to improve model generalization through several image transformations:

* Random rotation
* Random zoom
* Horizontal flipping
* Brightness adjustment

### ⚙️ Model Optimization

Several callbacks and optimization techniques were implemented during training:

* **ModelCheckpoint** — saves the best-performing model.
* **EarlyStopping** — stops training when validation performance no longer improves.
* **ReduceLROnPlateau** — automatically reduces the learning rate when validation performance plateaus.
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

## 🌐 Model Deployment

The trained model was converted into several formats for different deployment environments:

* **SavedModel** — TensorFlow model format
* **TensorFlow Lite (`.tflite`)** — suitable for lightweight and mobile deployment
* **TensorFlow.js** — suitable for browser-based applications

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

## 📦 Project Structure

```text
submission/
├── tfjs_model/
│   ├── group1-shard1of1.bin
│   └── model.json
├── tflite/
│   ├── model.tflite
│   └── label.txt
├── saved_model/
│   ├── saved_model.pb
│   └── variables/
├── notebook.ipynb
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Notebook

Open `Submission_Akhir.ipynb` in Jupyter Notebook or Google Colab and run the cells sequentially.

Make sure the dataset is available at the path specified in the notebook before starting the training process.

---

## 📌 Conclusion

This project successfully developed an image classification model capable of distinguishing **100 butterfly and moth species** using transfer learning with MobileNetV2.

The model achieved **96.00% validation accuracy** and **97.00% testing accuracy**, demonstrating strong performance in classifying butterfly and moth species from images.

