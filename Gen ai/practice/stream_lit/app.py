import streamlit as st
import pandas as pd

st.title("Application form")
st.header("user details")
st.subheader("please enter your details below")
st.text_input("First name:",type="default",width=400)
st.text_input("Last name:",type="default",width=200)
st.text_input("email :",type="email")
st.text_input("password:",type="password")
st.date_input("select the data")
st.text_input("age:",type="default")
st.text_input("gender:",type="default")

st.text("press the button")
st.button("click me",type="primary")



if st.button("press me"):
    st.text("the button is pressed")
else:
    st.write("not pressed")
    
slider_value=st.slider("how do you rate the experience ",1,100,10)
st.write(f"the slider value is  {slider_value}")
uploded_file=st.file_uploader(" upload the file ",type=["csv","txt"])
if uploded_file is not None:
    df=pd.read_csv(uploded_file)
    st.write(df.head())
    st.write(df.tail())