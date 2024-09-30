import streamlit as st
import joblib  # For loading your trained model

# Load your trained model (replace 'model.pkl' with your model file)
model = joblib.load('Random_forest_ctc_model.pkl')

# Title of the app
st.title("CTC Prediction App")

# Input fields for the user to enter their data
college = st.number_input("College")
role = st.number_input("Role")
city = st.number_input("City")
previous_ctc = st.number_input("Previous CTC", min_value=0.0)
previous_job_changes = st.number_input("Previous Job Changes", min_value=0)
graduation_marks = st.number_input("Graduation Marks", min_value=0.0, max_value=100.0)
experience_months = st.number_input("Experience (Months)", min_value=0)

# Button to trigger prediction
if st.button("Predict CTC"):
    # Prepare the input data as a DataFrame (or however your model expects it)
    input_data = [
        [college, role, city, previous_ctc, previous_job_changes, graduation_marks, experience_months]]

    # Make the prediction (replace `model.predict` with the appropriate method if needed)
    predicted_ctc = model.predict(input_data)

    # Display the prediction
    st.write(f"The predicted CTC is: ₹{predicted_ctc[0]:,.2f}")



