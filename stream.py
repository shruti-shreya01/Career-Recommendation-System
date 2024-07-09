import streamlit as st
st.title('Career Recommender System')
with st.form(key='my_form'):
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('Gender:', ('Male', 'Female'))
        st.number_input('Absence Days:')
        st.number_input('Weekly self-study hours:')
        st.number_input('History Score:')
        st.number_input('Chemistry Score:')
        st.number_input('English Score:')
        st.number_input('Total Score:')

    with col2:
        st.selectbox('Part-time Job:', ('Yes', 'No'))
        st.selectbox('Extra Curricuar Activities:', ('Yes', 'No'))
        st.number_input('Maths Score:')
        st.number_input('Biology Score:')
        st.number_input('Physics Score:')
        st.number_input('Geography Score:')
        st.number_input('Average Score:')

    st.form_submit_button(label='Submit')