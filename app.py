import streamlit as st
import pandas as pd

st.set_page_config(page_title= "File Uploader")
st.title("Comma to Pipe Convert")

file_type_select = st.selectbox('Select your file extension',('Excel','csv'))


if file_type_select =='Excel':
    st.write('You select :',file_type_select)

    df = st.file_uploader(label= "Upload your Excel File")
    if df:
        df_1 = pd.read_excel(df,engine="openpyxl",dtype={'No':str})

        st.write(df_1)

        st.download_button("Download CSV with Pipe prepared",
                            df_1.to_csv(sep='|',index=False,quoting=1,quotechar='"'),
                            file_name="DER_xxx.csv",
                            mime='text/csv')

else:
    st.write('You select :',file_type_select)

    df = st.file_uploader(label= "Upload your .csv File")
    delimiter_select = st.selectbox('Select your original file seperate',(',','|'))
    if df:
        df_1 = pd.read_csv(df, sep = delimiter_select, dtype={'No':str})

        st.write(df_1)

        st.download_button("Download CSV with Pipe prepared",
                            df_1.to_csv(sep='|',index=False,quoting=1,quotechar='"'),
                            file_name="commatopipe.csv",
                            mime='text/csv')