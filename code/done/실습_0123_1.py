import pandas as pd
import matplotlib.pyplot as plt
#한글설정
from matplotlib import font_manager
path="Pretendard.ttf"
font=font_manager.FontProperties(fname=path)
#[ csv파일 불러오기 ]######################
file_name="202412_202412_연령별인구현황_월간.csv"
data=pd.read_csv(file_name, encoding="EUC-KR")
#############[ 결측값 확인 ]######################
# print(data.head())
# print(data.info())# 13 번 column에 int 값이 있어서 오류가 발생

# #나이 컬럼 리스트만 추출
age_columns=[col for col in data.columns if '세' in col and '_남_' in col]
print(age_columns)
# #숫자로 변환
for col in age_columns:
    data[col]=data[col].astype(str).str.replace(",","").astype(int) #csv파일은 모두 str형으로 불러오므로 반점을 지우고 int형으로 변환
# #필터링
# #contains() : 문자열 데이터 필터링해주는 메서드, 특정 패턴을 찾을때 사용. (!!!!!!!!!!!)
# #옵션값###
# # na: 결측값을 포함할지 결정, 기본값은 True
# # case : 영문의 대소문자를 구분할지 결정, 기본값은 True
region_name=input("검색하고 싶은 지역명을 입력하세요. : ")
region_data=data[data["행정구역"].str.contains(region_name,na=False,case=False)]
if region_data.empty: #만약 오타를 쳤을 때
    print(f"{region_name}의 지역은 존재하지 않습니다.")

# #데이터추출
male_groups=[col.split("_남_")[1] for col in age_columns if "_남_" in col]
# fem_groups=[col.split("_여_")[1] for col in age_columns if "_여_" in col] #x축값은 1개만 있어도 됨.
print(male_groups)
# print(fem_groups)
# "2024년12월_계_0~9세" -> ["2024년12월","0~9세"] -> "0~9세"
# #결과값
result=region_data[age_columns].iloc[0].values

print(result)

# #그래프 그리기
plt.figure(figsize=(10,8))
plt.plot(male_groups,result, marker="o", label="Male", color='blue')
plt.plot(fem_groups,result, marker="x", label="Female", color='red')
plt.title(f"{region_name}의 연령별 인구수,Population",fontsize=16,pad=10, fontproperties=font)
plt.xlabel("연령대,ages",fontproperties=font)
plt.ylabel("인구수,population",fontproperties=font)
plt.grid(True, linestyle="--",alpha=0.5)
plt.xticks(rotation=45,fontproperties=font)
plt.legend()
plt.show()