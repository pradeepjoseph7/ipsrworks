import streamlit as st
import pandas as pd


st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

spectra = st.file_uploader("upload file", type={"csv", "txt"})
# if spectra is not None:
#     spectra_df = pd.read_csv(spectra)
spectra_df = pd.read_csv(spectra)
st.write(spectra_df)
