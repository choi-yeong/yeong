import matplotlib.pyplot as plt
from matplotlib import font_manager

#폰트경로 (!현재 경로 인식을 못함)
# path = "Pretendard.ttf"
# font = font_manager.FontProperties(fname=path).get_name()
# plt.rc('font', family=font)
font={"size":20,"color":"white","backgroundcolor":"black","weight":"bold"} #font 고정방법

#기본 사용법##############################################################################
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.title("Matplotlib", pad=10, fontdict=font) #pad:표와 제목간 거리
# plt.legend(title="legend",fontsize=13,loc='lower center')  #범례표시
# plt.plot(x,y,color="red",linestyle="--",linewidth=3,label="Sample graph")
# plt.plot(x,y, marker="*", markersize=20,markerfacecolor="red",markeredgecolor="blue", label="maker")
# plt.grid(True, axis="both",linestyle="--",color="blue",alpha=0.1)
# plt.xlabel("x axis",fontdict=font, labelpad=10)
# plt.ylabel("y axis",fontdict=font, labelpad=20)

#축범위설정#################################################################################
# plt.xlim([1,10])
# plt.ylim([0,20])
# plt.axis([1,10,0,20])
# plt.axis("equal") #x,y축을 동일하게 설정
# plt.axis('tight') #그래프가 모든 영역을 채워 딱맞춰서 나옴.
# plt.axis("scaled") #x,y축이 데이터 비율에 따라서 나옴.

#하나의 창에 여러개 보기#####################################################################
# x=[1,2,3,4]
# y1=[1,2,3,4]
# y2=[2,4,6,8]
# y3=[3,6,9,12]
# y4=[4,8,12,16]
# plt.plot(x,y1, label="y=x", color="red")
# plt.plot(x,y2, label="y=2x", color="orange")
# plt.plot(x,y3, label="y=3x", color="green")
# plt.plot(x,y4, label="y=4x", color="blue")
# plt.title("graph sample") #pad:표와 제목간 거리
# plt.legend(title="4graph",loc='upper center')  #범례표시
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.show()

#서브플롯 사용 (2x2로 여러개 그래프 띄우기[순서이용형])#############################################
# x=[1,2,3,4]
# y1=[1,2,3,4]
# y2=[2,4,6,8]
# y3=[3,6,9,12]
# y4=[4,8,12,16]
# plt.subplot(2,2,1)
# plt.plot(x,y1)
# plt.title("x=y")
# plt.subplot(2,2,2)
# plt.plot(x,y2)
# plt.title("x=2y")
# plt.subplot(2,2,3)
# plt.plot(x,y3)
# plt.title("x=3y")
# plt.subplot(2,2,4)
# plt.plot(x,y4)
# plt.title("x=4y")
# plt.suptitle("sample graph")
# plt.tight_layout()
# plt.show()

#서브플롯 사용 (2x2로 여러개 그래프 띄우기[좌표이용형])##################################################
# x=[1,2,3,4]
# y1=[1,2,3,4]
# y2=[2,4,6,8]
# y3=[3,6,9,12]
# y4=[4,8,12,16]
# fig, axes = plt.subplots(2,2)
# axes[0,0].plot(x,y1)
# axes[0,0].set_title("x=y")
# axes[0,1].plot(x,y2)
# axes[0,1].set_title("x=2y")
# axes[1,0].plot(x,y3)
# axes[1,0].set_title("x=3y")
# axes[1,1].plot(x,y4)
# axes[1,1].set_title("x=4y")
# plt.suptitle("sample graph")
# plt.tight_layout()
# plt.show()

#수직그래프 (기본)
# categories=['A','B','C']
# values=[10,15,7]
# # plt.bar(categories,values, width=0.5, color=['red','blue','green'],alpha=0.5,edgecolor="y",linewidth=5)
# #바 그래프별 텍스트 넣기
# bars=plt.bar(categories,values,color='orange',label="Bar graph")
# for bar in bars :
#     plt.text(
#         bar.get_x()+bar.get_width()/2,  #x좌표 중심
#         bar.get_height()+0.5,
#         str(bar.get_height()),
#         ha="center",
#         va="top",
#         color="black"
#         )
# plt.title("Bar graph")
# plt.show()


#수평그래프 그리기
# categories=['A','B','C']
# values=[10,15,7]
# bars=plt.barh(categories,values,color={"r","g","b"}) #bar -> barh
# #수평그래프에 텍스트 추가
# for bar in bars:
#     plt.text(bar.get_width()+0.5, #x좌표
#              bar.get_y()+bar.get_height()/2, #y좌표의 중심
#              str(bar.get_width()),
#              ha="right",
#              va="center",
#              color="black"
#     )
# plt.legend(bars,["2023","2024","2025"],title="year",ncol=3)
# # 기준선
# plt.axvline(x=values[0], linestyle="--")
# plt.title("Bar graph")
# plt.xlabel("categoty")
# plt.ylabel("year")
# # plt.show()
# plt.savefig("bar.png",format="png")

