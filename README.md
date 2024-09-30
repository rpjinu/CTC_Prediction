# CTC_Prediction
"A Streamlit-based web application for predicting Cost to Company (CTC) for new hires using machine learning."
<img src="https://github.com/rpjinu/CTC_Prediction/blob/main/streamlit.png" width=900>
CTC Prediction App
Overview
The CTC Prediction App is a machine learning-based web application developed using Streamlit that predicts the Cost to Company (CTC) for new hires based on various features such as college, role, city, previous CTC, job changes, graduation marks, and experience in months. The application leverages a trained machine learning model to provide quick and accurate salary predictions.

Features
User Input: Users can input their details through an intuitive interface, including college, role, city, previous CTC, previous job changes, graduation marks, and experience in months.
Prediction: The app uses a pre-trained machine learning model to predict the CTC based on user inputs.
Label Encoding: Categorical features are processed using label encoding to ensure the model receives the correct input format.
Streamlit Integration: The app is built using Streamlit, making it easy to deploy and share.
Technologies Used
Python
Streamlit
Scikit-learn
Joblib (for model saving/loading)
Pandas
Model Training
The model was trained using a dataset containing features relevant to predicting CTC. After training, the model and the necessary label encoders were saved to disk for easy loading and inference.

How to Run the App

<img src="https://github.com/rpjinu/CTC_Prediction/blob/main/ctc_by%20rp.jpg" width=900>

