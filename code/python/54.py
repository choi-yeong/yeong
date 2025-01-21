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
# print(df.loc["b","age"]) #b의 age부분 값 반환/
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
new_data={'name':'이몽룡', "age":31, "city":"Pohang"}
result = pd.concat([df,pd.DataFrame([new_data])], ignore_index=True) #concat :배열합치기
print(result)
#행추가(커스텀 인덱스를 부여하여 concat으로 합치는 방법)
new_data=pd.DataFrame({'name':'이몽룡', "age":31, "city":"Pohang"}, index=["d"])
result = pd.concat([df,new_data]) #concat :배열합치기
print(result)
# !append를 쓰는 방법은 신버전에서 막힘. 대신 loc로 추가 가능.
result.loc["e"]=["전우치",28,"Daejeon"]
print(result)

#열추가
result['job']=['Enginner','Doctor','Diginer','Programer','DataAnalogist']
print(result)

#요소값 수정
result.at["a", 'city']="Choenan" # 위치에 맞는 행과 열을 찾아서 변경
result.loc[result["name"]=="임꺽정","age"]=31   # 칼럼의 데이터값을 찾아서 변경
print(result)
