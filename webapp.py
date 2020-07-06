import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn import datasets
from xgboost import XGBClassifier
import importlib



from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_usm_fault(predict_input):
    
    prediction=classifier.predict(predict_input)
    print(prediction)
    return prediction

def main():
    
    st.title("😀 Welcome to Prediction Dashboard 😀")
    html_temp = """
    <div style="background-color:SteelBlue;padding:10px">
    <h2 style="color:Wheat;text-align:center;">Ultrasonic Flowmeter Diagnostics </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: Orchid;'>Value Ranges - </h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Flat Ratio - 0.6 - 1.1 </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Symmetry - 0.7 - 1.3 </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Crossflow - 0.8 - 1.1 </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Average Speed - 1483 - 1487 </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Average Flowvelocity - 1.9 - 9.5 </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Average Gain - 34 - 35 </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Salmon;'>Prediction - 0 : Healthy & 1 : Installation Effects </h5>", unsafe_allow_html=True)
    flat_ratio = st.text_input("Flat Ratio","Type Here")
    symmetry = st.text_input("Symmetry","Type Here")
    crossflow = st.text_input("Crossflow","Type Here")
    av_speed = st.text_input("Average Speed","Type Here")
    avg_flowvelocity = st.text_input("Average Flowvelocity","Type Here")
    avg_gain = st.text_input("Average Gain","Type Here")
    single_input=[]
    single_input.insert(0,flat_ratio)
    single_input.insert(1,symmetry)
    single_input.insert(2,crossflow)
    single_input.insert(3,av_speed)
    single_input.insert(4,avg_flowvelocity)
    single_input.insert(5,avg_gain)
    print(single_input)
    predict_input = np.reshape(single_input,(-1, 6))
    print(predict_input)
    result=""
    if st.button("Predict"):
        result=predict_usm_fault(predict_input)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Powered by Streamlit")
        st.text("Built with Love")


if __name__=='__main__':
    main()
    
    


