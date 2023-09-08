import numpy as np
import pandas as pd
import streamlit as st
import pickle




model = pickle.load(open('model.pkl','rb'))

df = pickle.load(open('df.pkl','rb'))



st.title('car price prediction')

