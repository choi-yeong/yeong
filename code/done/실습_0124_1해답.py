# 서울의 지하철역 5개를 선정하여 마커로 표시하세요
# 1. 데이터 프레임으로 만들기
# 2. subway.csv 파일로 만들기
import pandas as pd
import folium
# 서울 지하철역 5개
data= {
    "station":["서울역","공덕역","응암역","홍대입구역","디지털미디어시티역"],
    "Latitude":[37.555044, 37.5422723,37.598571,37.557412,37.576269],
    "Logitude":[126.970741,126.951833,126.915663,126.924493,126.901534]
}
subway=pd.DataFrame(data)
#csv파일 저장
subway.to_csv("subway.csv",encoding="EUC-KR",index=False)
#folium 지도제작
my_map=folium.Map(location=[37.580307,126.928719],zoom_start=12)

#방법1 : 복합한 함수가 쓰이지만, 속도측면에서 유리함.
# subway.apply(
#     lambda x:folium.Marker(
#         location=[x["Latitude"],x["Logitude"]],
#         popup=x["station"],
#         icon=folium.Icon(color="blue",icon="home")
#     ).add_to(my_map),
#     axis=1 #열단위로 작업. axis=0 :행단위로 작업
# )
# my_map.save("subway.html")

#방법2 : 간단한 함수가 쓰이지만, 자체계산 기능이 있어서 데이터가 많아질수록 속도가 떨어짐.
#iterrow() :데이터프레임에서 행단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수
# for index, x in subway.iterrows():
#     folium.Marker(
#         location=[x["Latitude"],x["Logitude"]],
#         popup=x["station"],
#         icon=folium.Icon(color="blue",icon="star")
#     ).add_to(my_map)

# my_map.save("subway.html")

