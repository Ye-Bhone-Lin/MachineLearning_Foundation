import streamlit as st 
import pandas as pd
import pickle 

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
    sepel_length = st.number_input(
    "Sepel Length", value=None, placeholder="Type a number...")
    
    sepel_width = st.number_input(
    "Sepel Width", value=None, placeholder="Type a number...")
    
    petal_length = st.number_input(
    "Petal Length", value=None, placeholder="Type a number...")
    
    petal_width = st.number_input(
    "Petal Width", value=None, placeholder="Type a number...")
    
    data = pd.DataFrame({'sepal length (cm)':[sepel_length], 'sepal width (cm)':[sepel_width], 'petal length (cm)':[petal_length],'petal width (cm)':[petal_width]})
    
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
