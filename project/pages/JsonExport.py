import streamlit as st
import leafmap.foliumap as lf
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium


m = folium.Map(location=[31.27856589843028, -316.99511], zoom_start=6)
drawing = Draw(export=True,filename="drawn_shape.geojson")
drawing.add_to(m)
c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=900, height=500)

with c2:
    st.write(output)