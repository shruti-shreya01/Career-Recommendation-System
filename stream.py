# import streamlit as st
# import pickle
# import numpy as np

# # Load the scaler and model
# try:
#     scaler = pickle.load(open("scaler.pkl", 'rb'))
#     model = pickle.load(open("model.pkl", 'rb'))
# except Exception as e:
#     st.error(f"Error loading model or scaler: {e}")
#     st.stop()

# class_names = ['Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Unknown',
#                'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
#                'Banker', 'Writer', 'Accountant', 'Designer',
#                'Construction Engineer', 'Game Developer', 'Stock Investor',
#                'Real Estate Developer']

# def Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
#                     weekly_self_study_hours, math_score, history_score, physics_score,
#                     chemistry_score, biology_score, english_score, geography_score):
#     # Calculate total_score and average_score
#     total_score = math_score + history_score + physics_score + chemistry_score + biology_score + english_score + geography_score
#     average_score = total_score / 7
    
#     # Encode categorical variables
#     gender_encoded = 1 if gender.lower() == 'female' else 0
#     part_time_job_encoded = 1 if part_time_job == 'Yes' else 0
#     extracurricular_activities_encoded = 1 if extracurricular_activities == 'Yes' else 0
    
#     # Create feature array
#     feature_array = np.array([[gender_encoded, part_time_job_encoded, absence_days, extracurricular_activities_encoded,
#                                weekly_self_study_hours, math_score, history_score, physics_score,
#                                chemistry_score, biology_score, english_score, geography_score,
#                                total_score, average_score]])
    
#     # Scale features
#     try:
#         scaled_features = scaler.transform(feature_array)
#     except Exception as e:
#         st.error(f"Error scaling features: {e}")
#         st.stop()
    
#     # Predict using the model
#     try:
#         probabilities = model.predict_proba(scaled_features)
#     except Exception as e:
#         st.error(f"Error predicting probabilities: {e}")
#         st.stop()
    
#     # Get top five predicted classes along with their probabilities
#     top_classes_idx = np.argsort(-probabilities[0])[:5]
#     top_classes_names_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]
    
#     return top_classes_names_probs

# def main():
#     st.title('Career Recommendation System')

#     with st.form(key='my_form'):
#         col1, col2 = st.columns(2)
#         with col1:
#             gender = st.selectbox('Gender:', ('Male', 'Female'))
#             absence_days = st.number_input('Absence Days:', min_value=0, max_value=100, value=0, step=1)
#             weekly_self_study_hours = st.number_input('Weekly self-study hours:', min_value=0, max_value=100, value=0, step=1)
#             history_score = st.number_input('History Score:', min_value=0, max_value=100, value=0, step=0.5)
#             chemistry_score = st.number_input('Chemistry Score:', min_value=0, max_value=100, value=0, step=0.5)
#             english_score = st.number_input('English Score:', min_value=0, max_value=100, value=0, step=0.5)
            
        
#         with col2:
#             part_time_job = st.selectbox('Part-time Job:', ('Yes', 'No'))
#             extracurricular_activities = st.selectbox('Extra Curricular Activities:', ('Yes', 'No'))
#             math_score = st.number_input('Maths Score:', min_value=0, max_value=100, value=0, step=0.5)
#             biology_score = st.number_input('Biology Score:', min_value=0, max_value=100, value=0, step=0.5)
#             physics_score = st.number_input('Physics Score:', min_value=0, max_value=100, value=0, step=0.5)
#             geography_score = st.number_input('Geography Score:', min_value=0, max_value=100, value=0, step=0.5)
            

#         submit_button = st.form_submit_button(label='Submit')

#         if submit_button:
#             st.write('Processing Input...')
#             recommendations = Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
#                                               weekly_self_study_hours, math_score, history_score, physics_score,
#                                               chemistry_score, biology_score, english_score, geography_score)
#             st.write("Top Career Recommendations:")
#             for career, probability in recommendations:
#                 st.write(f"{career}: {probability:.2f}")

# if __name__ == '__main__':
#     main()


import streamlit as st
import pickle
import numpy as np

# Load the scaler and model
try:
    scaler = pickle.load(open("scaler.pkl", 'rb'))
    model = pickle.load(open("model.pkl", 'rb'))
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")
    st.stop()

class_names = ['Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Unknown',
               'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
               'Banker', 'Writer', 'Accountant', 'Designer',
               'Construction Engineer', 'Game Developer', 'Stock Investor',
               'Real Estate Developer']

def Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
                    weekly_self_study_hours, math_score, history_score, physics_score,
                    chemistry_score, biology_score, english_score, geography_score):
    # Calculate total_score and average_score
    total_score = math_score + history_score + physics_score + chemistry_score + biology_score + english_score + geography_score
    average_score = total_score / 7
    
    # Encode categorical variables
    gender_encoded = 1 if gender.lower() == 'female' else 0
    part_time_job_encoded = 1 if part_time_job == 'Yes' else 0
    extracurricular_activities_encoded = 1 if extracurricular_activities == 'Yes' else 0
    
    # Create feature array
    feature_array = np.array([[gender_encoded, part_time_job_encoded, absence_days, extracurricular_activities_encoded,
                               weekly_self_study_hours, math_score, history_score, physics_score,
                               chemistry_score, biology_score, english_score, geography_score,
                               total_score, average_score]])
    
    # Scale features
    try:
        scaled_features = scaler.transform(feature_array)
    except Exception as e:
        st.error(f"Error scaling features: {e}")
        st.stop()
    
    # Predict using the model
    try:
        probabilities = model.predict_proba(scaled_features)
    except Exception as e:
        st.error(f"Error predicting probabilities: {e}")
        st.stop()
    
    # Get top five predicted classes along with their probabilities
    top_classes_idx = np.argsort(-probabilities[0])[:5]
    top_classes_names_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]
    
    return top_classes_names_probs

def main():
    st.title('Career Recommendation System')

    with st.form(key='my_form'):
        col1, col2 = st.columns(2)
        with col1:
            gender = st.selectbox('Gender:', ('Male', 'Female'))
            absence_days = st.number_input('Absence Days:', min_value=0, max_value=100, value=0, step=1)
            weekly_self_study_hours = st.number_input('Weekly self-study hours:', min_value=0, max_value=100, value=0, step=1)
            history_score = st.number_input('History Score:', min_value=0, max_value=100, value=0.0, step=0.5)
            chemistry_score = st.number_input('Chemistry Score:', min_value=0, max_value=100, value=0.0, step=0.5)
            english_score = st.number_input('English Score:', min_value=0, max_value=100, value=0.0, step=0.5)
        
        with col2:
            part_time_job = st.selectbox('Part-time Job:', ('Yes', 'No'))
            extracurricular_activities = st.selectbox('Extra Curricular Activities:', ('Yes', 'No'))
            math_score = st.number_input('Maths Score:', min_value=0, max_value=100, value=0.0, step=0.5)
            biology_score = st.number_input('Biology Score:', min_value=0, max_value=100, value=0.0, step=0.5)
            physics_score = st.number_input('Physics Score:', min_value=0, max_value=100, value=0.0, step=0.5)
            geography_score = st.number_input('Geography Score:', min_value=0, max_value=100, value=0.0, step=0.5)

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write('Processing Input...')
            recommendations = Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
                                              weekly_self_study_hours, math_score, history_score, physics_score,
                                              chemistry_score, biology_score, english_score, geography_score)
            st.write("Top Career Recommendations:")
            for career, probability in recommendations:
                st.write(f"{career}: {probability:.2f}")

if __name__ == '__main__':
    main()
