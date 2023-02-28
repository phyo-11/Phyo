import streamlit as st
import pandas as pd
from io import StringIO
from datetime import date

st.header("Identification Card")


uploaded_file = st.file_uploader("Choose Your Passport Photo") 
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()


id = st.text_input('Your Id No')


cn =st.text_input('Your Card No')


d = st.date_input("Issued Date", date.today())


name = st.text_input('Your Name')


fname = st.text_input('Your Father Name')


bd = st.date_input("Choose Your Birthday")


na = st.text_input('Your Nationality')


re = st.text_input('Your Religion')


h = st.text_input('Your Height In Centimeter')


b = st.text_input('Your Blood Type')


j = st.text_input('Your Occupation')


a = st.text_area('Your Address')


if st.button('Submit'):
    st.write('The current id no is', id)
    st.write('The current card no is',cn)
    st.write('The current person name is', name)
    st.write('The current person father name is', fname)
    st.write('Your birthday is:', bd)
    st.write('Your nationality is:', na)
    st.write('Your religion is:', re)
    st.write('Your height in cm is:', h)
    st.write('Your blood type is:', b)
    st.write('Your occupation', j)
    st.write('Your address', a)
    

