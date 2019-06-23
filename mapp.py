import folium
import webbrowser

def map(Lat,Longi,str):
    # 위도 경도 지정
    map_osm = folium.Map (location = [Lat, Longi],zoom_start=19)
    # 마커 지정
    folium.Marker([Lat, Longi], popup=str).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')

    webbrowser.open('osm.html')