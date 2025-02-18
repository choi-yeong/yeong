import folium

#--------기본
#지도열기
# my_map= folium.Map(location=[37.542144, 126.951300],zoom_start=12)
# my_map.save("my_map.html")
#지도스타일추가
# my_map= folium.Map(location=[37.542144, 126.951300],zoom_start=12,tiles="CartoDB Positron") #회색지도
#지도에 마커 추가
# my_map= folium.Map(location=[37.542144, 126.951300],zoom_start=12,tiles="CartoDB Positron")
# folium.Marker([37.566463, 127.009208], popup="동대문ddp플라자").add_to(my_map) #기본마커
# folium.Marker([37.537762, 126.977384], popup="전쟁기념관", icon=folium.Icon(color="red",icon="home")).add_to(my_map) #Home마커 표시
#지도에 여러개 마커 딕셔너리 형태로 추가
# my_map= folium.Map(location=[37.542144, 126.951300],zoom_start=12,tiles="CartoDB Positron")
# map_info =[
#     {"location":[37.529886, 126.964512],"popup":"용산역"},
#     {"location":[37.580064, 126.977029],"popup":"경복궁"},
#     {"location":[37.538660, 126.950435],"popup":"강의실"},
    
# ]
# for info in map_info:
#     folium.Marker(location=info["location"],popup=info["popup"],icon=folium.Icon(color="green", icon="star")).add_to(my_map)

#지도에 영역표시
# my_map= folium.Map(location=[37.542144, 126.951300],zoom_start=12,tiles="CartoDB Positron")
#원형영역
# folium.Circle(
#     location=[37.580064, 126.977029],
#     radius=500,#반지름(미터단위)
#     color="red",
#     popup="경복궁 일대",
#     fill=True,
#     fill_color="yellow").add_to(my_map)

# my_map.save("my_map.html")

# GeoJSON -------------------------------------------------------------------------------------#
from geojson import Feature,FeatureCollection,Polygon,Point
import json
# #지도생성
# my_map=folium.Map(location=[36.643780, 128.017202],zoom_start=8)

# #데이터 생성
# feature1=Feature(geometry=Point((126.983829,37.564230)), properties={"name":"서울","population":"970만"})
# feature2=Feature(geometry=Point((129.048102,35.171220)), properties={"name":"부산","population":"340만"})
# feature3=Feature(geometry=Point((127.395377,36.342733)), properties={"name":"대전","population":"150만"})
# feature4=Feature(geometry=Point((128.577762,35.835960)), properties={"name":"대구","population":"240만"})

# #데이터 하나로 묶기
# geojson_data=FeatureCollection([feature1,feature2,feature3,feature4])

# #데이터를 지도에 추가
# folium.GeoJson(
#     geojson_data,
#     name="GeoGJSON Data",
#     tooltip=folium.GeoJsonTooltip(
#         fields=["name","population"], #표시할 속성
#         aliases=["도시이름 : ","인구 : "], #속성의 별칭
#     )
# ).add_to(my_map)

# my_map.save("my_map.html")


#실무실습 ###################################
my_map=folium.Map(location=[37.559677, 127.003740], zoom_start=7,tiles="CartoDB Positron")

#geojson
geojson_data = "HangJeongDong_ver20241001.geojson"

# with open(geojson_data, encoding="utf-8") as f:
#     geojson_data=json.load(f)

folium.GeoJson(
    geojson_data,
    name="대한민국 경계",
    style_function=lambda _:{
        "fillcolor":"blue",
        "color":"black",
        "weight":1,
        "fillOpacity":0.1
    }
).add_to(my_map)

my_map.save("대한민국경계.html")