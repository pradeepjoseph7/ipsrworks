import streamlit as st
import pandas as pd


st.write("Loan Prediction Web App")

#df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
#st.write(df)
testdata_df = pd.DataFrame()
testdata = st.file_uploader("Please Upload the Unseen Test Data", type={"csv", "txt"})
if testdata is not None:
  testdata_df = pd.read_csv(testdata)
st.write(testdata_df)
#modelload = load_model('Final_model')
#unseen_predictions_new = predict_model(final, data=testdata_df)
st.altair_chart(testdata_df, use_container_width=False)
