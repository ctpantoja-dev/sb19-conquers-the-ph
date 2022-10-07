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
    "PH Spotify Top 200",
    "Genres that dominated the PH Top 200",
    "Audio features of each genre",
    "SB19 Ranking in Spotify daily Top 200",
    "SB19 songs in Spotify Top 200",
    "Analysing SB19 songs",
    "SB19 Competitors",
    "Make SB19 the most listend artist on Spotify",
    "Suggested collaborations",
    "Suggested song genre",
    "Best time to release album/single"
]

selection = st.sidebar.radio("", list_of_pages)
page_fn_dict = {}

def slide_page(page_no):
    st.image("slides/{}.png".format(page_no))

for i in range(len(list_of_pages)):
    page_name = list_of_pages[i]
    page_fn_dict[page_name] = slide_page
    
page_fn_dict[selection](list_of_pages.index(selection) + 1)