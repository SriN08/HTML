import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("REAL-TIME MOVIE RECOMMONDATION USING AI")
st.image('bg.jpeg')
st.header("the best movie recommandation in the world")
st.subheader("it's ai recommended")
st.text("let's start")
uploadfile = st.file_uploader('upload .csv files only',type=['csv'])
if uploadfile is not None:
    dataFrame = pd.read_csv(uploadfile)
    st.success('uploaded csv file successfully...')
    st.subheader("data uploaded successfully")
    st.dataframe(dataFrame)
    st.write('file name is::', uploadfile.name)
    st.write('file shape::', dataFrame.shape)
    st.write('columns data::', dataFrame.columns.tolist())
    st.subheader("let's start preprossing")
    dataFrame.dropna(inplace = True)
    dataFrame['user_id']=dataFrame['user_id'].astype(int)
    dataFrame['movie_id']=dataFrame['movie_id'].astype(int)
    dataFrame['rating']=dataFrame['rating'].astype(float)
    st.write('data cleaning')
    st.dataframe(dataFrame)
    st.write('first five rows')
    st.dataframe(dataFrame.head())
    st.write('last five rows')
    st.dataframe(dataFrame.tail())
    st.write('Data :',dataFrame.describe())
    st.write('Data Visualization')
    fig1, ax1=plt.subplots()
    sns.histplot(dataFrame['rating'],bins = 10,kde = True, ax = ax1,color = 'skyblue')
    ax1.set_xlabel("Rating")
    ax1.set_ylabel("Count")
    ax1.set_title("Rating count of movies")
    st.pyplot(fig1)
    st.checkbox("select checkbox for accepting the dataset")
    st.checkbox("select checkbox for accepting the rating data")
    st.checkbox("select checkbox for accepting the movie data")
    Sg = st.radio("select the datasets column : ",['user_id','movie_id','movie_title','rating'])
    if Sg is not None:
        st.success(Sg)
    data=st.selectbox("seelct the datase columns:",
           ['user_id','movie_id','movie_title','rating'])
    if data is not None:
        st.success(data)

    da = st.multiselect("select the multi columns :",
           ['user_id','movie_id','movie_title','rating'])
    if da is not None:
        st.success(len(da))    
    stbutton=st.button("Register")
    if st.button("Login"):
        st.success('Login successfully ')
    #input type
    Stname = st.text_input("enter the name")
    if st.button("Submit"):
        name = Stname.title()
        st.success('data submitted successfully')
        st.write("your name is :: ",name)

   
        
    
else:
    st.warning("upload csv file")   
    st.error("file not uploaded")
    exc = FileNotFoundError
    st.exception(exc)