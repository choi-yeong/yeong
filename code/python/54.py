import pandas as pd

# #리스트 형식으로 생성 #########
# data = [10,20,30,40]
# series= pd.Series(data)#기본인덱스
# series= pd.Series(data, index=('a','b','c','d')) #커스텀인덱스
# print(series)

# #딕셔너리 형식으로 생성 #########
# data = {
#     'a':10,
#     'b':True,
#     'c':3.14,
#     'd':'Python'
# }
# series=pd.Series(data, name="딕셔너리")
# print(series)
# print(series.index)
# print(series.values)
# print(series.shape)

# data = ('민지','여',False)
# member=pd.Series(data, index=['이름','성별','결혼여부'])
# print(member)
# print()
# print(member["이름"])
# print()
# print(member[["성별","결혼여부"]])

# data=[10,20,30,40,50]
# series = pd.Series(data, index=['a','b','c','d','e'])
# print(series[0]) # 기존의 인덱스로 불러오려고하면 커스텀으로 부여한 인덱스로 부르라고 경고창이 뜸. 하지만 값을 출력해줌. "츤데렌가"
# print(series['a'])
# print(series[series>20])
# series["c"]=100
# print(series)
# print('a' in series) #해당 인덱스가 있는지 검사
# print(series.sum()) #모든 밸류값을 더한다.
# print(series.mean()) # 모든 밸류값의 평균
# print(series.max()) # 모든 밸류값의 최대값
# print(series.astype(float)) #타입을 변경

#시리즈 만들기
# data = {
#     "밀가루":"4 cups",
#     "우유":"1 cup",
#     "계란":"2 large",
#     "참치캔":"1 can"
# }
# series=pd.Series(data, name="Dinner")
# print(series)

# 데이터 프레임(Data Frame)
# Series들을 결합해놓은 형태
# index=['2020','2021','2022','2023','2024','2025']
# yeonghee=pd.Series([140,150,160,170,180,190],index=index)
# cheolsu=pd.Series([200,210,220,230,240,250],index=index)
# result = pd.DataFrame({
#     "영희":yeonghee,
#     "철수":cheolsu
# })
# print(result)
# print(result.head()) #head() : 위에서부터 기본으로 0~5까지 보여줌
# print(result.tail()) #head() : 밑에서부터 기본으로 0~5까지 보여줌
# print(result.shape) # 행x열
# print(result.info()) #요약정보 #non-null : non값이 (null)없다. 즉 테이블에 데이터가 꽉찼다.



data={
    'name':['홍길동','임꺽정','성춘향'],
    'age' : [25, 30, 35],
    'city':['Seoul','Busan','Incheon']
}
df=pd.DataFrame(data,index=['a','b','c'])
#데이터값 추출하는 방법 ######################
# print(df)
# print(df.loc["b"])
print(df.loc["b","age"]) #b의 age부분 값 반환/
# print(df.loc[~(df["age"]>=30)])
# print(df.loc[:, "name"])
# print(df.loc["a",:]) #[index,column] 따라서 전체인덱스불러올땐 [:,"name"], 전체 칼럼을 불러올땐 ["a",:]
# print(df.iloc[1]) # ="b"인덱스를 숫자인덱스로 호출
# print(df.iloc[1,1]) # ="b"인덱스의 1번 column 호출

# print(df.iloc[0:2,0:1]) # 끝값을 포함하지 않음
# print(df.loc["a":"c", "name":"age"]) #포함

# print(df.iloc[[0,2],[1,2]])

#데이터를 넣고 추가/수정 하는 방법 ############
#행추가(커스텀 인덱스를 초기화하는 방법)
# new_data={'name':'이몽룡', "age":31, "city":"Pohang"}
# result = pd.concat([df,pd.DataFrame([new_data])], ignore_index=True) #concat :배열합치기
# print(result)
# #행추가(커스텀 인덱스를 부여하여 concat으로 합치는 방법)
# new_data=pd.DataFrame({'name':'이몽룡', "age":31, "city":"Pohang"}, index=["d"])
# result = pd.concat([df,new_data]) #concat :배열합치기
# print(result)
# # !append를 쓰는 방법은 신버전에서 막힘. 대신 loc로 추가 가능.
# result.loc["e"]=["전우치",28,"Daejeon"]
# print(result)

# #열추가
# result['job']=['Enginner','Doctor','Diginer','Programer','DataAnalogist']
# print(result)

# #요소값 수정
# result.at["a", 'city']="Choenan" # 위치에 맞는 행과 열을 찾아서 변경
# result.loc[result["name"]=="임꺽정","age"]=31   # 칼럼의 데이터값을 찾아서 변경
# print(result)

# #컬럼값 변경
# result.rename(columns={"name":"이름", "age":"나이","city":"도시"}, inplace=True) #inplace=True : 원본데이터 수정 허락.
# print(result)

# #데이터 정렬
# result.sort_values(by="나이",inplace=True, ascending=False) #ascending=False : 내림차순
# print(result)

# #칼럼 삭제
# result.drop(columns=["도시"],inplace=True)
# print(result)


# 결측값 ################################################
data = {
    "Name":['홍길동','임꺽정','성춘향'],
    "Age":[25,None,35],
    "City":["서울","부산",None]
}
df=pd.DataFrame(data)
# print(df)
# print(df.isnull()) # 결측값 여부
# print(df.isnull().sum()) # 각 컬럼마다 결측값 갯수 반환
# print(df.info())

# df_drop=df.dropna() # 결측값 있는 행을 아예 삭제해버림
# df_drop_column=df.dropna(axis=1) # 결측값 있는 열을 아예 삭제해버림
# print(df_drop_column)

# df_filled=df.fillna(method="ffill") #이전에 있는 값으로 채운다.
# print(df_filled)
# df_filled=df.fillna(method="bfill") #이후에 있는 값으로 채운다.
# print(df_filled)

#주요메서드 ############################################################
#isin()
s=pd.Series(["홍길동","임꺽정","성춘향","이몽룡"])
result=s.isin(["홍길동","이몽룡"])
# print(result)

data = {
    'Name':["홍길동","임꺽정","성춘향:,"],
    "Age":[25,30,20]
}

df=pd.DataFrame(data)
result=df.isin(["성춘향","홍길동",20])
print(result)

restult=df[df['Name'].isin(["성춘향",'홍길동',20])]
# print(result)

s=pd.Series([1,2,None])
result=s.isin([None,2])
# print(restult)

#Value_counts()
s=pd.Series(["사과","바나나","사과","오렌지","바나나","사과"])
# print(s.value_counts())

df=pd.DataFrame(
    {
    "과일":["사과","바나나","사과","오렌지","바나나",None,"사과"],
    "수량":[1,2,3,4,5,6,7]
    }
)
# print(df["과일"].value_counts(normalize=True))
# print(df["과일"].value_counts(ascending=True))
# print(df["과일"].value_counts(dropna=False))

# agg() ###################################################################################
# s=pd.Series([1,2,3,4,5])
# result=s.agg(['sum','mean','max'])
# print(result)

# df=pd.DataFrame({
#     "A":[1,2,3],
#     "B":[14,15,16]
# })

# print(df.agg(["sum","mean","max"])) # 각 컬럼마다 계산해줌.
# print(df.agg({"A":"sum","B":"mean"})) # 각 컬럼마다 계산해줌.

s1=pd.Series([10,20,30])
s2=pd.Series([5,15,25])
# print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)
# #통계연산#############
# print(s1.sum())
# print(s1.mean())
# print(s1.max())
# print(s1.min())
# print(s1.std())#표준편차
# print(s1.var())#분산
# print(s1.median())#중앙값

#통계지표 #################
# print(s1.describe())

#그룹화 ###################
# data={
#     'group':['A','A',"B","B","C"],
#     'value':[10,20,30,40,50]
# }
# df=pd.DataFrame(data)
# result=df.groupby("group")["value"].sum()
# print(result)
# result=df.groupby("group")["value"].max()
# print(result)
# result=df.groupby("group")["value"].agg(['sum','mean','var'])
# #         그룹을지을건데(그룹지을모집)[사용할값].메서드
# print(result)

data={
    'group':['A','A',"B","B","C"],
    'value1':[10,20,30,40,50],
    'value2':[5,15,25,35,45]
}
df=pd.DataFrame(data)
print(df.columns)
result=df.groupby('group').agg({
    'value1':'sum',
    'value2':["mean","max"]
})
print(result)

result=df.groupby('group').filter(lambda x:x["value1"].sum()>30)
print(result)
