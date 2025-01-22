#xticks(x값,눈금값,lotation=각도) 기울이기
import matplotlib.pyplot as plt
#실습1. 그래프그리기
# months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# sales_2019=[100,120,140,110,130,150,160,170,180,200,190,210]
# sales_2020=[90,110,130,120,140,160,170,160,150,180,200,190]
# plt.title("Monthly Sales Comparison (2019-2020)", pad=5) #pad:표와 제목간 거리
# plt.plot(months,sales_2019,color="blue",linewidth=2,label="2019")
# plt.plot(months,sales_2020,color="orange",linewidth=2,label="2020")
# plt.legend(loc='upper left')  #범례표시
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()

#실습2. 그래프그리기
# categories=["Category 1","Category 2","Category 3","Category 4","Category 5",]
# data=[20,35,15,27,45]
# plt.figure(figsize=(7,10))
# plt.title("Bar Chart",pad=2)
# plt.bar(categories,data,color="darkcyan")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.grid(True,color="gray",alpha=0.5)
# plt.xticks(rotation=45) #글자 기울기
# plt.show()

#실습3. 그래프 그리기
sizes=[34,32,16,18]
label=['Apple','Banana','Melon','Grape']
explode=[0,0.1,0,0.1] # 이격점 (강조효과)
colors=['red','yellow','green','darkviolet']
plt.pie(sizes,labels=label,explode=explode,
        autopct="%1.1f%%", #파이그래프 안에 %를 텍스트로 표시해준다.
        startangle=0, #시작하는 앵글을 준다. x선을 기준으로한다.
        colors=colors, # 색깔을 부여한다.
        textprops={"fontsize":10,"color":"black"}, #텍스트 속성이다.
        wedgeprops={"edgecolor":"black","width":0.7} #가운데 빈 구멍을 내준다.
        )
plt.show()