import pandas as pd
index=["이름","수학","영어","과학"]
n1=pd.Series(["홍길동",85,88,95],index=index)
n2=pd.Series(['임꺽정',90,76,89],index=index)
n3=pd.Series(["성춘향",78,92,84],index=index)
#n4=pd.Series([95,89,84],index=index)

df=pd.DataFrame([
    n1,
    n2,
    n3
])
print(df)

df.loc[3]=["이몽룡",88,85,90]
print(df)

df['Total']=[268,255,254,263]
print(df)

df.rename(columns={"수학":"Math"}, inplace=True) #inplace=True : 원본데이터 수정 허락.
print(df)

print()
print()
# 해답 ###############################################
data={
    "이름":["홍길동","임꺽정","성춘향"],
    "수학":[85,88,95],
    "영어":[88,76,92],
    "과학":[95,89,84]
}
df=pd.DataFrame(data)
new_df=df.rename(columns={"수학":"Math"})

new_data={"이름":"이몽룡", "Math":88, "영어":85,"과학":98}
new_df=pd.concat([new_df,pd.DataFrame([new_data])], ignore_index=True)
print(new_df)
new_df.loc[new_df["영어"]==76,"영어"]=88
print(new_df)

new_df["Total"] = new_df["Math"]+new_df["영어"]+new_df["과학"] # 알아서 순서대로 더해짐.
print(new_df)

