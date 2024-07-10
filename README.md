# Career-Recommendation-System

This project implements a career recommendation system using machine learning techniques. It predicts potential career choices based on user inputs related to academic performance and extracurricular activities.


## Features
##### Predicts top career choices based on user input scores and activities
##### Provides probabilities for each predicted career option.
##### Deployed using Streamlit for interactive web-based interface.

## Installation
```bash
#1. Clone the repositories:

git clone https://github.com/shruti-shreya01/Career-Recommendation-System.git
cd Career-Recommendation-System
```
```bash
#2. Install dependencies:

pip install -r requirements.txt
```
```bash
#3. Run the streamlit app:

streamlit run app.py

```

## Usage


#### Fill in the form fields with relevant data (gender, scores, etc.).
#### Click the "Submit" button to see the top career recommendations.
#### Explore the probabilities provided for each career option.

## Technologies used

#### Python
#### Streamlit
#### Scikit-learn
#### NumPy
#### Pandas

## Model details
#### Model:
 RandomForestClassifier
#### Data Preprocessing: 
Scaling using StandardScaler, handling categorical variables with label encoding.

#### Training Data: 
Balanced using SMOTE for class imbalance.

## File Structure
```bash
├── app.py           # Streamlit application code
├── model.pkl        # Pickled trained model file
├── scaler.pkl       # Pickled scaler for data scaling
├── requirements.txt # Dependencies
├── README.md        # This file
└── data             # Folder for dataset (if applicable)
    └── student-scores.csv
```

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Acknowledgement
##### Inspired by the need to provide career guidance based on academic performance.
##### Special thanks to contributors and open-source libraries used.
