import matplotlib.pyplot as plt
# 히스토그램 ===================================================================================================
# data=[1,1,2,3,4,5,5,5,6,7,8,9,0,5,3,2,3,5,6,7,2,3,6,7,8,3,4,5,3,3,3,5,4,2,2]
# plt.hist(data,color="green",histtype="bar")

# # 여러개 data
# data1=[1,2,3,4,5,3,3,3,4]
# data2=[2,2,3,3,3,4,4,4,4]
# plt.hist([data1,data2],bins=5,color=["green","purple"])
# plt.title("hist")
# plt.xlabel('value')
# plt.ylabel('bins')
# plt.legend()

# plt.show()

#산점도 그리기 ===============================================================================================
# x=[1,2,3,4,5]
# y=[2,3,5,7,11]
# sizes=[20,50,80,100,200]
# colors=[10,20,30,40,50]
# plt.scatter(x,y,s=sizes,c=colors,cmap="plasma")
# plt.colorbar(label="color bar")
# plt.show()
#산점도 예시
import numpy as np
# n=50
# x=np.random.rand(n) #0과 1의 난수
# y=np.random.rand(n)
# area=(30*np.random.rand(n))**2 #0과 30사이 난수 생성 후 제곱
# colors=np.random.rand(n)

# plt.scatter(x,y,s=area,c=colors,cmap="Spectral",alpha=0.5)
# plt.show()

#파이차트 =============================================================
# sizes=[15,30,34,10]
# label=['apple','banana','grape','chrry']
# explode=[0,0.1,0,0] # 이격점 (강조효과)
# colors=['gold','lightblue','lightgreen','pink']
# plt.pie(sizes,labels=label,explode=explode,autopct="%1.1f%%",startangle=140,colors=colors,textprops={"fontsize":20,"color":"darkblue"},wedgeprops={"edgecolor":"black","width":0.7})
# plt.show()

#도넛===============================================
# sizes=[40,30,20,10]
# labels=['x','y','z','w']
# plt.pie(sizes,labels=labels,wedgeprops={"width":0.4}) #wedgeprops의 width사이즈가 작아질수록 가운데 구멍이 커진다.
# plt.show()
