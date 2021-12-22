import streamlit as st
import pandas as pd
import pickle
from pycaret.classification import load_model, predict_model

st.write("Heart Failure Prediction Web App")

#df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
#st.write(df)
testdata_df = pd.DataFrame()
testdata = st.file_uploader("Please Upload the Unseen Test Data", type={"csv", "txt"})
if testdata is not None:
  testdata_df = pd.read_csv(testdata)
st.write("Number of records in the prediction data are : ")
st.write(testdata_df.count())
st.write(count_row = testdata_df.shape[0])  # Gives number of rows
st.write(count_col = testdata_df.shape[1])
#modelload = load_model('Final_model')
#unseen_predictions_new = predict_model(final, data=testdata_df)
#st.altair_chart(testdata_df, use_container_width=False)
#filename = 'Final_model.pkl'
loaded_model = load_model('Final_model')
#loaded_model = pickle.load(open(filename, 'rb'))
predictions_df = predict_model(estimator=loaded_model, data=testdata_df)
predictions = predictions_df['Label'][0]
st.write("Heart Failure Prediction Results are: ")
st.write(predictions)
