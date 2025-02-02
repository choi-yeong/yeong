import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import folium
#데이터 프레임으로 서울의 지하철역 5개 정리
# data={
#     'station':['마포역','공덕역','홍대입구역'],
#     'location' : [[37.539702, 126.946078], [37.543727, 126.950801], [37.557035, 126.923978]],
# }

data =[
    {"location":[37.539702, 126.946078],"popup":"마포역"},
    {"location":[37.543727, 126.950801],"popup":"공덕역"},
    {"location":[37.557035, 126.923978],"popup":"홍대역"},
    
]


df=pd.DataFrame(data)
print(df)
my_map= folium.Map(location=[37.542144, 126.951300],zoom_start=12,tiles="CartoDB Positron")
for info in data:
    folium.Circle(
    location=df["location"],
    radius=500,#반지름(미터단위)
    color="red",
    popup=df["popup"],
    fill=True,
    fill_color="yellow").add_to(my_map)

my_map.save("my_map.html")

# 지도에 여러개 마커 딕셔너리 형태로 추가##################
# map_info =[
#     {"location":[37.529886, 126.964512],"popup":"용산역"},
#     {"location":[37.580064, 126.977029],"popup":"경복궁"},
#     {"location":[37.538660, 126.950435],"popup":"강의실"},
# ]
# for info in map_info:
#     folium.Marker(location=info["location"],popup=info["popup"],icon=folium.Icon(color="green", icon="star")).add_to(my_map)