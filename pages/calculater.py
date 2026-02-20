import streamlit as st
st.sidebar.title("Bmi Calculator App")
st.sidebar.subheader("Navigation")

st.title("bmi calculator")
h=st.number_input("enter your height in cm")
w=st.number_input("enter your weight in kg")
if st.button("calculate bmi"):
    bmi=w/(h/100)**2
    st.write(f"your bmi is {bmi:.2f}")