import streamlit as st
import geopandas as gpd
import leafmap.foliumap as leafmap
point_file = st.file_uploader("Upload Geogson point file", type="geojson")
poly_file = st.file_uploader("Upload Geogson polygon file ", type="geojson")
if point_file and poly_file:
    point_gdf = gpd.read_file(point_file).to_crs('EPSG:3857')
    poly_gdf = gpd.read_file(poly_file).to_crs('EPSG:3857')
    joined=gpd.sjoin(point_gdf,poly_gdf,predicate='intersects')
    # st.write(joined.index_right)
    # print(joined)
    # joined.head()
    st.write("use the layers sympol to deactive your points data layer")
    m = leafmap.Map()
    m.add_gdf(point_gdf, layer_name='Total Points layer')
    m.add_gdf(poly_gdf, layer_name='polygon layer ')
    m.add_gdf(joined, layer_name='Point in polygon ')
    m.to_streamlit(height=500)



