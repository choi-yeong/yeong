# 리스트
number=["Hello","Python",1,3,5,7,9]
print(number)
#Indexing(인덱싱) : 인덱스 번호로 요소를 추출하는 행위
print(number[1]) #Python #리스트 인덱스값은 0부터 시작.
print(number[0]) #Hello
"""
print(number[7]) #인덱스 범위를 벗어나면 에러가 뜬다.
"""
text="Hello, Python"
print(list(text)) #['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n']
"""
- 문자열을 list할 시 공백과 쉼표조차 요소로 만들어서 리스트화한다.
- list() 함수는 반복 가능한(iterable) 객체를 리스트로 변환할 때 사용한다.
반복 가능한 객체? (ex. 문자열, 튜플, 셋(집합), 딕셔너리, 또 다른 리스트)
"""
#그럼 int형은 리스트화 가능한가???
"""
invalid = 1234
print(list(invalid)) #타입에러 : int형 자료형은 list()로 변환 불가능하다.
"""
#문자열의 인덱싱과 슬라이싱
print(text[7])
print(text[7:10])

#리스트 슬라이싱
date = "20250106"
year = date[0:4]
month = date[4:6]
day = date[6:8]
print(year + "년" + month +"월" + day + "일") # 2025년 01월 06일

#문자열에서 사용 가능한 함수
print(len(date)) #문자열의 길이를 구하는 함수
print(len(text))
print(text.count("l")) #문자열의 ()요소를 구하는 함수.
print(text.count("P")) #대소문자 구분함.
print(text.count("j")) #요소가 없으면 0 출력.