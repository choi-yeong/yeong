import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# print(sns.get_dataset_names()) #penguins
penguins=sns.load_dataset('penguins')
# print(penguins.head())
#실습 1.
#종별 평균몸무게를 막대그래프로
# sns.catplot(x="species",y="body_mass_g",data=penguins,kind="bar")

#부리길이와 부리깊이의 관계를 산점도로 시각화, 종별로 색상 다르게
# sns.relplot(data=penguins , x="bill_length_mm",y="bill_depth_mm",hue="species")

#펭귄의 섬에 따라 몸무게의 분포를 violinplot으로 시각화
# sns.catplot(data=penguins, x="island", y="body_mass_g", kind="violin")
# plt.show()




#실습2. flights 데이터셋을 이용하여 그래프생성
#연도별 승객수의 평균을 꺽은선 그래프로 나타내기
flights=sns.load_dataset('flights')


print(flights.head())

# sns.relplot(data=flights, x="year", y="passengers",kind="line")
#연도와 월별 승객수를 히트맵으로 시각화
# sns.heatmap(flights,annot=True,cmap="crest")
# plt.show()


#실습3. 특정연도의 월별 승객수를 막대그래프로 나타내세요.
select_year=int(input("검색할 연도 :"))

region_data=flights[flights["year"].contains(select_year,na=False,case=False)]
if region_data.empty: #만약 오타를 쳤을 때
    print(f"{select_year}의 지역은 존재하지 않습니다.")

result=region_data.values
print(result)