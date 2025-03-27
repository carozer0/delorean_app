import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Famous Twins", layout="wide")
st.title("👯‍♂️ Famous Twins")


image = Image.open("img/zendaya.png")
st.image(image, width=400, caption="Zendaya")
image = Image.open("img/pierre_niney_2.png")
st.image(image, width=400, caption="Pierre Niney")
image = Image.open("img/poolvoerde.png")
st.image(image, width=400, caption="Benoît Poolvoerde")
