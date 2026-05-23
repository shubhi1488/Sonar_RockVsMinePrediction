# Sonar Rock vs Mine Prediction using Machine Learning

A complete end-to-end Machine Learning project that predicts whether an underwater object is a Rock or a Mine using sonar signal data and Machine Learning algorithms.
---

## Project Overview

This project analyzes sonar signal data and predicts whether the detected underwater object is:
Rock
Mine
The project includes:
Data preprocessing
Exploratory Data Analysis (EDA)
Model training
Model evaluation
Prediction system
Gradio web application deployment
---

## Technologies Used

-Python
-Pandas
-NumPy
-Matplotlib
-Seaborn
-Scikit-learn
-Gradio
-Pickle
---

## Machine Learning Models Used

- Logistic Regression

---

## Dataset

Dataset used:
Dataset used:
Sonar Dataset
The dataset contains:
60 numerical sonar signal attributes
1 output label:
R → Rock
M → Mine

---

## Project Workflow

Data Loading
→ Data Preprocessing
→ Exploratory Data Analysis
→ Train Test Split
→ Model Training
→ Model Evaluation
→ Prediction System
→ Save Model using Pickle
→ Gradio Deployment
---

Data Preprocessing
Performed:
Data cleaning
Feature and label separation
Train-test split
Numerical data handling
---

## Best Model

Final model used:
Logistic Regression
Achieved accuracy:
~75% to 85%

---

## Gradio Web Application

The project includes a Gradio-based web interface where users can:
Enter 60 sonar signal values
Predict whether the object is a Rock or Mine
Get instant prediction results

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Gradio App

```bash
python app/gradio_app.py
```

---

## Project Structure

SonarRockvsMinePrediction/
│
├── app.py
├── sonar_model.pkl
├── prediction_result.csv
├── SonarRockvsMinePrediction.ipynb
├── requirements.txt
└── README.md
---
Sample Input
0.0307,0.0523,0.0653,0.0521,0.0612,0.0999,0.1204,0.1506,0.0985,0.1102,0.1453,0.1765,0.2014,0.2556,0.3102,0.3651,0.4123,0.4502,0.4891,0.5102,0.5345,0.5601,0.5894,0.6012,0.6201,0.6453,0.6702,0.6901,0.7104,0.7321,0.7011,0.6802,0.6451,0.6103,0.5892,0.5601,0.5302,0.5004,0.4703,0.4302,0.3901,0.3502,0.3101,0.2802,0.2501,0.2203,0.1902,0.1601,0.1302,0.1101,0.0902,0.0701,0.0602,0.0501,0.0402,0.0301,0.0202,0.0151,0.0102,0.0051
---

## Future Improvements

- Improve model accuracy
-Add advanced ML algorithms
-Deploy on Hugging Face Spaces
-Add Streamlit deployment
-Add batch CSV prediction support
-Add model explainability
---

## Author

Shubhi Agarwal
