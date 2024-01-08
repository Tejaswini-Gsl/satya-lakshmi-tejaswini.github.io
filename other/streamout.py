import streamlit as st
import pandas as pd
import numpy as np
import pickle
# from sklearn.svm import SVC


#### RUN with streamlit run streamout.py
st.write("""
# Google Service Prediction App
This app predicts the google services!
Data obtained from the [cmsa library](https://github.ford.com/GSATYALA/test/tree/main/hackathon) in python.
""")
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://github.ford.com/GSATYALA/test/blob/main/hackathon/sample.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        webapp = st.sidebar.selectbox('WebApplication',('True','False'))
        mobileapp = st.sidebar.selectbox('MobileApplication',('True','False'))
        containerwork = st.sidebar.selectbox('ContainerWorkloads',('True','False'))
        eventdriven = st.sidebar.selectbox('EventDrivenApplication',('True','False'))
        mainframe = st.sidebar.selectbox('MainframeApplication',('True','False'))
        analytical = st.sidebar.selectbox('AnalyticalApplication',('True','False'))
        iotapp = st.sidebar.selectbox('IOTapplication',('True','False'))
        datatrans = st.sidebar.selectbox('DataTransactionVolume',('More','Less'))
        imagestorage = st.sidebar.selectbox('Imagestorage',('True','False'))
        caching = st.sidebar.selectbox('Caching',('True','False'))
       
        data = {'WebApplication': webapp,
                'MobileApplication': mobileapp,
                'ContainerWorkloads': containerwork,
                'EventDrivenApplication': eventdriven,
                'MainframeApplication': mainframe,
                'AnalyticalApplication': analytical,
                'IOTapplication': iotapp,
                'DataTransactionVolume': datatrans,
                'Imagestorage':imagestorage ,
                'Caching': caching
                 }
        features = pd.DataFrame(data, index=[0])
        return features
    df = user_input_features()

encode = ['WebApplication','MobileApplication','ContainerWorkloads','EventDrivenApplication','MainframeApplication','AnalyticalApplication','IOTapplication','Imagestorage','Caching']
for col in encode:
    df[col] = df[col].map({'True':1 ,'False':0})
df['DataTransactionVolume']= df['DataTransactionVolume'].map({'Less':1 ,'More':0})


st.subheader('User Input features')


if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)


# load_clf = pickle.load(open('model.pkl', 'rb'))

# # Apply model to make predictions
# prediction = load_clf.predict(df)
# # prediction_proba = load_clf.predict_proba(df)

# data = pd.read_csv("service_name.csv")
# output = data.loc[data['GoogleServicecodes'] == prediction[0], 'GoogleService'].iloc[0]

# st.subheader('Prediction')
# st.write(output)

# st.subheader('Prediction Probability')
# st.write(prediction_proba)

