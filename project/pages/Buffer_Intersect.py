import streamlit as st
import geopandas as gpd
import leafmap.foliumap as leafmap

inputFile1 = st.file_uploader("upload file point",type="geojson")
inputFile2 = st.file_uploader("upload file polygon1",type="geojson")
inputFile3 = st.file_uploader("upload polygon2",type="geojson")

if  inputFile1 and inputFile2 and inputFile3:
    point_Read = gpd.read_file(inputFile1).to_crs("EPSG:3857")
    buffer_point = point_Read['geometry'].buffer(500)      
    buffer_gdf= gpd.GeoDataFrame(geometry=buffer_point)

    polygon1_Read = gpd.read_file(inputFile2).to_crs("EPSG:3857")
    polygon2_Read = gpd.read_file(inputFile3).to_crs("EPSG:3857")
    intersection = gpd.overlay(polygon1_Read, polygon2_Read, how='intersection')
    st.write("use the layers sympol to deactive your data layer")
    m = leafmap.Map()
    m.add_gdf(buffer_gdf,layer_name='buffer layer')
    m.add_gdf(polygon1_Read,layer_name='polygon1 layer')
    m.add_gdf(polygon2_Read,layer_name='polygon2')  
    m.add_gdf(point_Read,layer_name='Total Points layer') 
    m.add_gdf(intersection,layer_name='intersection')
    m.to_streamlit(height=500)
