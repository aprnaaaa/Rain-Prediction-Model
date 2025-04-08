import streamlit as st
import joblib
import sklearn

st.title("Rain Fall Prediction")
st.number_input("Enter Pressure:")
st.number_input("Enter Pressure:")
st.number_input("Enter Pressure:")
st.number_input("Enter Pressure:")
st.number_input("Enter winddirection:")
st.number_input("Enter windspeed:")


if st.button("Predict"):
    op= mymodel.predict([[a1,a2,a3,a4,a5,a6,a7]])
    if op==1:
        st.write('Barish Hogi!!!')
else:
    st.write('Barish Nahi Hogi!!!')
        