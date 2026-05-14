Student Performance Prediction System 🎓
📌 Project Overview

The Student Performance Prediction System is a Machine Learning-based classification project developed as part of the Week 2 Artificial Intelligence Internship Project at DecodeLabs.

This application predicts student academic performance categories such as:

Excellent
Average
Poor

using demographic and educational attributes.

The project demonstrates the complete workflow of a supervised Machine Learning pipeline, including:

Data preprocessing
Feature encoding
Model training
Model evaluation
Model deployment using Streamlit
🚀 Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Pickle
📂 Project Structure
student-performance-classification/
│
├── data/
│   └── StudentsPerformance.csv
│
├── models/
│   ├── student_model.pkl
│   ├── encoders.pkl
│   └── target_encoder.pkl
│
├── train.py
├── app.py
├── requirements.txt
└── README.md
📊 Features
Student performance prediction
Logistic Regression classification model
Data preprocessing & label encoding
Interactive Streamlit frontend
Model saving using Pickle
Simple and user-friendly interface
🧠 Machine Learning Workflow
1. Data Loading

The dataset is loaded using Pandas.

2. Data Preprocessing

Categorical features are encoded using LabelEncoder.

3. Feature Engineering

An average score is calculated using:

Math score
Reading score
Writing score

Performance labels are created based on average scores.

4. Model Training

A Logistic Regression classification model is trained using Scikit-learn.

5. Model Evaluation

The model is evaluated using accuracy score.

6. Model Deployment

The trained model is deployed using Streamlit.

🎯 Prediction Categories
Average Score	Performance
80+	Excellent
50–79	Average
Below 50	Poor
▶️ How to Run the Project
Step 1: Clone the Repository
git clone <repository-link>
Step 2: Navigate to Project Folder
cd student-performance-classification
Step 3: Create Virtual Environment
python -m venv venv
Step 4: Activate Virtual Environment
Windows
venv\Scripts\activate
Step 5: Install Dependencies
pip install -r requirements.txt
Step 6: Train the Model
python train.py
Step 7: Run Streamlit App
streamlit run app.py
📈 Model Used
Logistic Regression

The Logistic Regression algorithm was selected because it achieved the best accuracy among tested models.

Accuracy Comparison
Model	Accuracy
Logistic Regression	70%
Decision Tree	65%
Random Forest	63.5%
📚 Learning Outcomes

Through this project, I learned:

Supervised Machine Learning
Classification algorithms
Feature encoding
Data preprocessing
Model serialization
Frontend integration using Streamlit
End-to-end ML workflow
🏢 Internship Information

Organization: DecodeLabs
Program: Artificial Intelligence Internship
Project: Week 2 – Data Classification Using AI

👨‍💻 Developed By

Ayyaz Qamar
Artificial Intelligence Intern
DecodeLabs Internship Program