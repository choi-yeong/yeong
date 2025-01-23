#실습. 공공데이터 활용
#서울시 공원 내 운동기구 설치 현황

import pandas as pd

file_name="code/python/서울시 공원 내 운동기구 설치 현황_201231.csv"
df=pd.read_csv(file_name, encoding='cp949')

print(df.head())
print(df.info())
df.columns=df.columns.str.strip()
print(df.columns)
df['구분']=df['구분'].str.strip()    # 왜 또 스트립 해줘야하냐;;
df['운동기구 기종명']=df['운동기구 기종명'].str.strip() # 왜 또 스트립 해줘야하냐;;
#공원별 운동기구 설치 수
# part_counts=df.groupby("구분")["운동기구 수량"].sum()
# print(part_counts)
# with open("park_count.txt", "w",encoding='utf-8') as file:
#     file.write("공원별 총 운동기구 설치 수\n")
#     file.write(part_counts.to_string())

#운동기구 별 수량
# equipment_counts=df["운동기구 기종명"].value_counts()
# print(equipment_counts)
# with open("equpment_count.txt", "w",encoding='utf-8') as file:
#     file.write("운동기구 종류별 설치 개수\n")
#     file.write(equipment_counts.to_string())

#관리기관별 총 운동기구 설치 수
# manage_counts=df.groupby("관리기관")["운동기구 수량"].sum()
# print(manage_counts)
# with open("manager_count.txt", "w",encoding='utf-8') as file:
#     file.write("관리기관별 총 운동기구 수량\n")
#     file.write(manage_counts.to_string())

#특정 공원 데이터 필터링
# def filtering(park):
#     print(park,"필터링")
#     filter_park = df[df['구분']==park]
#     print(filter_park)

# filtering("남산공원(회현)")

#특정 운동기구 종류 필터링
# filter_equipment=df[df['운동기구 기종명']=="스텝사이클"]
# print(filter_equipment)
# with open("eqipmen_filt.txt", "w",encoding='utf-8') as file:
#     file.write("스텝사이클\n")
#     file.write(filter_equipment.to_string())

#정렬
# sort_df=df.sort_values(by="운동기구 수량",ascending=False)
# with open("sort_df.txt", "w",encoding='utf-8') as file:
#     file.write("운동기구 수량별 내림차순\n")
#     file.write(sort_df.to_string())