import streamlit as st
import pyqrcode as qr
import cv2
import time
from PIL import Image

st.title("QRコード生成器")
text = st.text_input("テキストを入力して下さい")

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

if text:
    qrcode = qr.create(text)
    qrcode.png(file="./temp.png",scale=6)
    image = Image.open('./temp.png')
    st.image(image,caption=f'{text}',use_column_width=False)