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
# print(data.info())

region_name=input("검색하고 싶은 지역명을 입력하세요. : ")
# 지역 검색
region_data = data [ data ["행정구역"].str.contains(region_name, na=False)]
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")
    exit()

#
male_columns=[col for col in region_data.columns if "세" in col and '_남_' in col]
fem_columns=[col for col in region_data.columns if "세" in col and '_여_' in col]
# print(male_columns)

# for col in male_columns:
#     region_data[col]=region_data[col].astype(str).str.replace(",","").astype(int) # 구식 방법(개발효율낭비)
male_result=region_data[male_columns].iloc[0].astype(str).str.replace(',','').astype(int) #나은방법(개발효율굿)
#iloc : Serise에 벡터화 연산을 적용하여 효율적이고 간결한 코드 작성이 가능.
fem_result=region_data[fem_columns].iloc[0].apply(lambda x: int(str(x).replace(",","")))
#apply() : 사용자함수 정의


#데이터추출
age_groups=[col.split("_남_")[1] for col in male_columns]

#그래프 그리기
plt.figure(figsize=(5,4))
plt.plot(age_groups, male_result,marker='o', label='남성Male',color="blue")
plt.plot(age_groups, fem_result,marker='x', label='여성Female',color="red")

plt.title(f"{region_name}의 연령별 인구수", fontsize=16,pad=10,fontproperties=font)
plt.xlabel("연령대,ages",fontproperties=font)
plt.ylabel("인구수,population",fontproperties=font)
plt.grid(True, linestyle="--",alpha=0.5)
plt.xticks(rotation=45,fontproperties=font)
plt.legend()
plt.show()