from distutils.command.upload import upload
from doctest import Example
from re import A
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import profile_report
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
# webapp title
st.markdown('''
# ''Exploratory Data Analysis web application''
This app is developed by Aryan Nijhara called ''EDA app''
''')

# How to upload a fill from PC

with st.sidebar.header("Upload Your Dataset (.csv)"):
    uploaded_file=st.sidebar.file_uploader("Upload your file",type=['csv'])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example csv file](df)")

# profiling report from pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv("uploaded_file")
        return csv
    df= load_csv()
    pr =profile_Report(df,explorative=True) 
    st.header('**Input DF**')
    st.write(df)
    st.write('---') 
    st.header('**Profile report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for csv file')
    if st.button('Press to use example data'):
        # example data set
        @st.cache
        def load_data():
            a=pd.DataFrame(np.random.rand(100,5),
            columns=['age','banna','codanics','germany','Ear'])
            return a
        df=load_data()
        pr =profile_Report(df,explorative=True) 
        st.header('**Input DF**')
        st.write(df)
        st.write('---') 
        st.header('**Profile report with pandas**')
        st_profile_report(pr)    








