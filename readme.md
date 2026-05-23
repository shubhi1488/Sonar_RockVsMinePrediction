Sonar Rock vs Mine Prediction using Machine Learning
A Machine Learning project that predicts whether an underwater object is a Rock or a Mine using sonar signal data.
This project uses a trained ML classification model along with a Gradio web interface for real-time prediction.
🚀 Project Overview
Sonar systems send sound waves underwater and analyze the reflected signals.
Using these sonar readings, this project classifies objects into:
Rock (R)
Mine (M)
The model is trained on the famous Sonar dataset using Machine Learning techniques.
🛠️ Technologies Used
Python
NumPy
Pandas
Scikit-learn
Gradio
Pickle
📂 Project Structure
SonarRockvsMinePrediction/
├── app.py
├── sonar_model.pkl
├── prediction_result.csv
├── requirements.txt
├── SonarRockvsMinePrediction.ipynb
└── README.md
📊 Dataset Information
The dataset contains:
60 numerical sonar frequency values
1 target label:
R → Rock
M → Mine
Each row represents reflected sonar signals from an object underwater.
⚙️ Features
Sonar signal classification
Real-time prediction
Gradio web interface
Model saving using Pickle
Prediction result export to CSV
Easy deployment support
🧠 Model Workflow
Load sonar dataset
Data preprocessing
Train ML classification model
Save trained model as .pkl
Predict Rock or Mine
Deploy using Gradio
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone <your-github-repo-link>
cd SonarRockvsMinePrediction
2️⃣ Install Requirements
pip install -r requirements.txt
3️⃣ Run the Gradio App
python app.py
🌐 Gradio Interface
The Gradio app allows users to:
Enter 60 sonar values
Predict Rock or Mine instantly
Interact with the model through a simple UI
🧪 Sample Input
0.0307,0.0523,0.0653,0.0521,0.0612,0.0999,0.1204,0.1506,0.0985,0.1102,0.1453,0.1765,0.2014,0.2556,0.3102,0.3651,0.4123,0.4502,0.4891,0.5102,0.5345,0.5601,0.5894,0.6012,0.6201,0.6453,0.6702,0.6901,0.7104,0.7321,0.7011,0.6802,0.6451,0.6103,0.5892,0.5601,0.5302,0.5004,0.4703,0.4302,0.3901,0.3502,0.3101,0.2802,0.2501,0.2203,0.1902,0.1601,0.1302,0.1101,0.0902,0.0701,0.0602,0.0501,0.0402,0.0301,0.0202,0.0151,0.0102,0.0051
📈 Future Improvements
Improve model accuracy
Add multiple ML algorithms
Deploy on Hugging Face Spaces
Add graphical analytics dashboard
Add CSV batch prediction support
📸 Project Demo
