import streamlit as st
import pyqrcode as qr
from PIL import Image

st.title("QRコード生成器")
text = st.text_input("テキストを入力して下さい")

if text:
    qrcode = qr.create(text)
    qrcode.png(file="./temp.png",scale=6)
    image = Image.open('./temp.png')
    st.image(image,caption=f'{text}',use_column_width=False)