import streamlit as st 
import pandas as pd
import pickle 
import time

st.markdown("<h1 style='text-align: center; color: white;'>Iris Classification</h1>", unsafe_allow_html=True)
with st.sidebar:

    radio = st.radio(
        "Documentation IRIS",
        ["About", "Iris Classify"],
    )
    
if radio == "About":
    st.markdown("""The Iris flower dataset is a classic machine learning dataset consisting of 150 observations of iris flowers, with measurements of sepal and petal length and width, and the flower's species by using Logistic Regression.
                """)

else:
    sepal_length = st.number_input(
    "Sepal Length", value=1, placeholder="Type a number...")
    
    sepal_width = st.number_input(
    "Sepal Width", value=1, placeholder="Type a number...")
    
    petal_length = st.number_input(
    "Petal Length", value=1, placeholder="Type a number...")
    
    petal_width = st.number_input(
    "Petal Width", value=1, placeholder="Type a number...")
    
    data = pd.DataFrame({'sepal length (cm)':[sepal_length], 'sepal width (cm)':[sepal_width], 'petal length (cm)':[petal_length],'petal width (cm)':[petal_width]})
    
    
    if data is not None:
        st.write(data)
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(data)
        with st.spinner("Wait for it..."):
            time.sleep(1)
            if prediction == 0:
                st.write(f"Iris species is setosa")
            elif prediction == 1:
                st.write(f"Iris species is versicolor")
            else:
                st.write(f"Iris species is virginica")
