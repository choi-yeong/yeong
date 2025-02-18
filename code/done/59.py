import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# print(sns.get_dataset_names()) #: 데이터셋
#:예제데이터
tips=sns.load_dataset('tips')
# print(tips.head())
# print(tips.info())

# sns.scatterplot(x='total_bill',y="tip", data=tips, hue='size',palette='deep',style='time',size="size")
# sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue="size",dodge=True)
# sns.swarmplot(x="day",y="total_bill",data=tips,hue="size",dodge=True) # stripplot과 비교하면 gitter가 없고 나머진 동일
# sns. relplot(x="total_bill",y="tip",data=tips,style="time",hue="sex")
# sns.catplot(x="day",y="total_bill",data=tips,kind="point",hue="sex")
# sns.displot(tips["total_bill"],kind='kde')
# sns.pairplot(data=tips, hue="time")
# sns.regplot(data=tips, x="total_bill",y="tip")
data=np.random.rand(10,10)
print(data)
sns.heatmap(data,annot=True,fmt=".2f", cmap="crest")

plt.show()

