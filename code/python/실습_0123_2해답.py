import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# print(sns.get_dataset_names()) #penguins
#실습 1.###############################
penguins=sns.load_dataset('penguins')
# print(penguins.head())

#종별 평균몸무게를 막대그래프로 시각화!
# sns.barplot(x="species",y="body_mass_g",data=penguins)
# plt.show()

#부리길이와 부리깊이의 관계를 산점도로 시각화, 종별로 색상 다르게!
# sns.scatterplot(data=penguins , x="bill_length_mm",y="bill_depth_mm",hue="species")
# plt.show()

#펭귄의 섬에 따라 몸무게의 분포를 violinplot으로 시각화!
# sns.violinplot(data=penguins, x="island", y="body_mass_g")
# plt.show()

#실습 2.################################
flights=sns.load_dataset('flights')
#연도별 승객수의 평균을 꺽은선 그래프로 나타내기
# print(flights.head())
# sns.relplot(data=flights, x="year", y="passengers",kind="line")
# avg=flights.groupby('year')['passengers'].mean().reset_index()
# print(avg)
# plt.plot(avg["year"],avg["passengers"])
# plt.show()

#연도와 월별 승객수를 히트맵으로 시각화
# sns.heatmap(flights,annot=True,cmap="crest")
# pivot(): 데이터를 재구조화, index, column, value
# pivot=flights.pivot(index="month",columns="year",values="passengers")
# print(pivot)
# sns.heatmap(pivot, annot=True, fmt='d')
# plt.show()

#특정연도의 월별 승객수를 막대그래프로 나타내세요.
# year_1958=flights[ flights['year']==1958]
# sns.barplot(data=year_1958,x='month',y='passengers')
# plt.show()



# 실습 3.#######################################################
# titanic=sns.load_dataset('titanic')
# print(titanic.info())


#탑승 클래스와 생존여부 간의 관계를 catplot으로 시각화
# sns.catplot(data=titanic, x="class", hue="survived", kind="count")
# plt.show()

#나이의 분포를 생존여부에 따라 kdeplot으로 시각화
# sns.kdeplot(data=titanic, x="age",hue="survived",fill=True)
# plt.show()