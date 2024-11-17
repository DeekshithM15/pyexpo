import streamlit as st
st.title(f"Vote regestration")
st.write("# hi") 
name=st.text_input("enter your name")
st.write(f"hi{name}")
name2=st.text_input("enter the place")
st.write(f"{name2}")
age=st.number_input("enter the number",min_value=0,max_value=100)
st.subheader(f"age")
st.slider('value',0,100,18)
if st.button("click here is valid"):
    def votel(age):
        if age >=18:
            return "your are valid to vote"
        else:
            return "you are invalid to vote.You must be at least 18 years old."
    result=votel(age)
    st.write(result)
    