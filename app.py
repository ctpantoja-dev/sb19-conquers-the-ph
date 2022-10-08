# Import libraries
import csv
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import os

import streamlit as st

st.set_page_config(
    page_title="SB19 Conquers the Philippines",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

list_of_pages = [
    "Making SB19 the best-selling artist in the Philippines",
    "Who is SB19?",
    "SB19 should be a successful mainstream artist, right?",
    "SB19 daily streams from 2019 to 2022",
    "How do we make SB19 a mainstay on Spotify Top 200 Daily Charts?",
    "What is a Mainstay?",
    "MAPA vs 2021 Top 5 Mainstays",
    "Genres that dominated the Top 200 Daily Charts",
    "SB19 songs genres",
    "SB19 vs 2021 Mainstay EDM Artists",
    "SB19 vs 2021 Mainstay Pop Artists",
    "Recommendations",
    "Suggested song genre",
    "Suggested collaborations",
    "Remake a mainstay",
    "When best to release and album/single",
    "Increase and sustain SB19's visibility in social media",
    "Some of Sara Geronimo's tracks and Tala",
    "Thank You!",
    "The Team"
]

selection = st.sidebar.radio("", list_of_pages)
page_fn_dict = {}

def slide_page(page_no):
    st.image("slides/{}.png".format(page_no))

for i in range(len(list_of_pages)):
    page_name = list_of_pages[i]
    page_fn_dict[page_name] = slide_page
    
page_fn_dict[selection](list_of_pages.index(selection) + 1)