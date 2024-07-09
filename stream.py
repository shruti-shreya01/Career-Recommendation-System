import streamlit as st
import pickle
import numpy as np

# Load the scaler and model
scaler = pickle.load(open("scaler.pkl", 'rb'))
model = pickle.load(open("label_encoder.pkl", 'rb'))  # Ensure this is your trained model

class_names = ['Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Unknown',
               'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
               'Banker', 'Writer', 'Accountant', 'Designer',
               'Construction Engineer', 'Game Developer', 'Stock Investor',
               'Real Estate Developer']

def Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
                    weekly_self_study_hours, math_score, history_score, physics_score,
                    chemistry_score, biology_score, english_score, geography_score,
                    total_score, average_score):
    
    # Encode categorical variables
    gender_encoded = 1 if gender.lower() == 'female' else 0
    part_time_job_encoded = 1 if part_time_job == 'Yes' else 0
    extracurricular_activities_encoded = 1 if extracurricular_activities == 'Yes' else 0
    
    # Create feature array
    feature_array = np.array([[gender_encoded, part_time_job_encoded, absence_days, extracurricular_activities_encoded,
                               weekly_self_study_hours, math_score, history_score, physics_score,
                               chemistry_score, biology_score, english_score, geography_score, total_score, average_score]])
    
    # Scale features
    scaled_features = scaler.transform(feature_array)
    
    # Predict using the model
    probabilities = model.predict_proba(scaled_features)
    
    # Get top five predicted classes along with their probabilities
    top_classes_idx = np.argsort(-probabilities[0])[:5]
    top_classes_names_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]
    
    return top_classes_names_probs

def main():
    st.title('Career Aspiration Predictor')

    with st.form(key='my_form'):
        col1, col2 = st.columns(2)
        with col1:
            gender = st.selectbox('Gender:', ('Male', 'Female'))
            absence_days = st.number_input('Absence Days:', min_value=0)
            weekly_self_study_hours = st.number_input('Weekly self-study hours:', min_value=0)
            history_score = st.number_input('History Score:', min_value=0)
            chemistry_score = st.number_input('Chemistry Score:', min_value=0)
            english_score = st.number_input('English Score:', min_value=0)
            total_score = st.number_input('Total Score:', min_value=0)

        with col2:
            part_time_job = st.selectbox('Part-time Job:', ('Yes', 'No'))
            extracurricular_activities = st.selectbox('Extra Curricular Activities:', ('Yes', 'No'))
            math_score = st.number_input('Maths Score:', min_value=0)
            biology_score = st.number_input('Biology Score:', min_value=0)
            physics_score = st.number_input('Physics Score:', min_value=0)
            geography_score = st.number_input('Geography Score:', min_value=0)
            average_score = st.number_input('Average Score:', min_value=0.0, format="%.2f")

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        recommendations = Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
                                          weekly_self_study_hours, math_score, history_score, physics_score,
                                          chemistry_score, biology_score, english_score, geography_score,
                                          total_score, average_score)
        st.write("Top 5 Career Aspirations with probabilities:")
        for career, prob in recommendations:
            st.write(f"{career}: {prob:.2f}")

if __name__ == '__main__':
    main()
