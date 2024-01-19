import streamlit as st
import requests

st.image('assets/header-iris.png')
st.title('Iris Flower Classification')

# st.write("""
# The Iris flower data set or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]
# """)

st.divider()

with st.form('iris-form'):
    sepal_length = st.number_input('sepal length', min_value=0.0, max_value=10.0, help='centimeter')
    petal_length = st.number_input('petal length', min_value=0.0, max_value=10.0, help='centimeter')
    sepal_width = st.number_input('sepal width', min_value=0.0, max_value=10.0, help='centimeter')
    petal_width = st.number_input('petal width', min_value=0.0, max_value=10.0, help='centimeter')

    submit = st.form_submit_button('predict')

    if submit:
        st.snow()
        with st.spinner("Predicting....."):
            result = requests.post('http://api_service-1:8000/predict/', json={
                "sepal_length":sepal_length,
                "petal_length":petal_length,
                "sepal_width":sepal_width,
                "petal_width":petal_width,
            }).json()

        st.info(f'Your Iris is {result["result"]}')