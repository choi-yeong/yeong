import folium
from geojson import Feature,Polygon,FeatureCollection
#실습
polygon=Feature(geometry=Polygon([
          [
            [127.01929637959489,37.694459385751756],
            [126.78460718680918,37.58299565980957],
            [126.59417680689467,37.60344405478962],
            [126.61190270631568,37.359756407986055],
            [
              126.8246071722599,
              37.27570233575409
            ],
            [
              127.1661055346741,
              37.4934609215631
            ],
            [
              127.09251015017867,
              37.69479321988537
            ],
            [
              127.01929637959489,
              37.694459385751756
            ]
          ]
        ]), properties={"name":"수도권"})
geojson_data= FeatureCollection([polygon])
my_map=folium.Map(location=[37.562775, 126.849182],zoom_start=7)

#지도그리기
folium.GeoJson(
    geojson_data,
    name="수도권",
    tooltip=folium.GeoJsonTooltip(fields=['name'],aliases=["영역이름:"]),
    style_function=lambda x:{
        "fillcolor":"yellow",
        "color":"black",
        "weight":2,
        "fillOpacity":0.5
    }
).add_to(my_map)
my_map.save("실습_0124_2해답.html")