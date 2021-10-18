import streamlit as st
import io
from main import write_text

st.title("Spotify Playlist Cover Creator")

bg_image = st.file_uploader("Background image", "jpg")

col1, col2, col3 = st.columns([3,2,1])
text = col1.text_input("Cover Title")
text_pos = col2.selectbox("Tile vertical position", ["center", "up", "down"])
text_color = col3.color_picker("Title Color", value="#ffffff")

if bg_image != None:
    cover = write_text(bg_image, text, text_color, text_pos)
    in_mem_file = io.BytesIO()
    cover.save(in_mem_file, format = "JPEG")
    in_mem_file.seek(0)

    st.download_button('Download Cover', in_mem_file, f'{text} cover.jpg')