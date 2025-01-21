import pandas as pd
import numpy as np

file_name="code/python/서울시 공원 내 운동기구 설치 현황_201231.csv"
df=pd.read_csv(file_name,encoding="cp949")
print(df.head()) # 불러오기 확인
print(df.info()) # 결측값 감지
df.columns=df.columns.str.strip() #공백제거
print(df.columns)

#공원별 총 운동기구 설치 수
park=df.groupby("구분")["운동기구 수량"].sum()
#         그룹을지을건데(그룹지을모집)[사용할값].메서드
print(park)

#운동기구 종류별 설치 개수
vari=df.groupby("운동기구 기종명")["운동기구 수량"].sum()
#         그룹을지을건데(그룹지을모집)[사용할값].메서드
print(vari)

#관리기관별 총 운동기구 설치 수
union=df.groupby("관리기관")["운동기구 수량"].sum()
#         그룹을지을건데(그룹지을모집)[사용할값].메서드
print(union)
print()

#특정 공원 데이터 필터링
filt="남산공원(회현)"
print(filt,"데이터 필터링")
filted_park=df.groupby("관리기관").filter(filt)
print(filted_park)