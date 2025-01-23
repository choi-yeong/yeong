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

#리스트 인덱싱과 슬라이싱
shop = ["반팔","청바지", "이어폰", ["무선키보드", "기계식키보드"]]
#인덱싱
print(shop[:2]) #['반팔', '청바지']
print(shop[3]) #['무선키보드', '기계식키보드']
print(shop[-2]) #이어폰 #뒤에서부터 카운팅
print(shop[:]) #['반팔', '청바지', '이어폰', ['무선키보드', '기계식키보드']] #리스트 요소 전부 출력함.
#리스트 수정
shop[0]="긴팔"
print(shop) #['긴팔', '청바지', '이어폰', ['무선키보드', '기계식키보드']]
"""
shop[100]="신발" #인덱스에러 : 존재하는 인덱스까지만 출력가능하다.
print(shop) 
"""
#리스트 삭제
print(shop[1]) #청바지 #1번 인덱스이다.
del shop[1] #단일삭제
print(shop) #['긴팔', '이어폰', ['무선키보드', '기계식키보드']] #1번요소던 "청바지"가 삭제되었다.
print(shop[1]) #이어폰 #삭제된 중간 요소의 빈자리를 뒷자리 요소들이 당겨서 채운다.
del shop[2:] #복수삭제 #여러개의 요소를 삭제시킨다.
print(shop) #['긴팔', '이어폰']

#리스트 연산
a=[1,2,3]
b=["안녕","반가워"]
print(a+b) #[1, 2, 3, '안녕', '반가워'] #두 리스트가 순서대로 합쳐진다.
print(b*3) #['안녕', '반가워', '안녕', '반가워', '안녕', '반가워'] #해당 리스트를 해당횟수만큼 반복한다.
"""
즉 리스트 연산은 문자열 연산과 비슷하다.
"""

#리스트 함수
#sorted(리스트 정렬함수) : 오름차순 정렬 함수. 원본은 변경하지 않고 새로운 리스트를 반환. 내림차순으로 하고싶으면 reverse=True 옵션항 추가로 설정가능

# 리스트 매서드
# sort() : 오름차순 정렬 매서드. 원본을 정렬하여 변경하고, 새로운 리스트를 반환하지 않음.
# reverse() : 리스트의 인덱스 순서를 반대로 정렬하는 매서드
# index() : 위치찾기 매서드
# append() : 맨 마지막에 요소 추가
# pop(): 맨마지막에 요소 삭제
# POP(idx) : idx번째 인덱스 요소 삭제
# remove('a') : 리스트에서 특정요소 삭제
# insert(idx,'a') : idx번째 위치에 요소 삽임
# clear() : 모든 요소 삭제
num=[3,1,5,2]
num_asc=sorted(num)
print(num) #sorted(num)은 원본 num을 유지한다.
print(num_asc) #sorted(num)은 새로운 리스트를 반환한다. (새로운 변수에 저장 가능.)

num_desc = sorted(num, reverse=True) 
print(num_desc) #reverse=True 옵션으로 내림차순으로 가능.

num.sort()
print(num) #num.sort()는 새로운 리스트를 반환하지 않지만, 원본을 변경한다. (원래 변수가 바뀌어버림.)

"""
함수vs메서드
함수 : 어떤 입력값이든 사용 가능한 도구(전역적)
 -iterable 객체에서 사용 가능
메서드 : 특정 객체의 동작(종속적)
 -list 객체 전용.
"""

korean=["강","이","박","최"]
korean.sort(reverse=1)
print(korean)
alphabet=["b","c","a","g"]
print(alphabet)
alphabet.reverse() #내림차순이 아니라 인덱스 순서를 역순으로 바꿈.
print(alphabet)
print(alphabet.index("c")) #reverse로 인덱스 순서가 바뀌었기에 1이 아닌 2가 출력됨.

a=["a", "b", "C", "안녕", "Hi"]
print(a) #['a', 'b', 'C', '안녕', 'Hi']
a.append("Good") #인덱스 마지막에 요소 추가.
print(a) #['a', 'b', 'C', '안녕', 'Hi', 'Good']
a.pop() #인덱스 마지막 요소 삭제
print(a) #['a', 'b', 'C', '안녕', 'Hi']
a.pop(2) #2번째 인덱스 요소 삭제 후 뒷 인덱스가 자리 당겨옴.
print(a) #['a', 'b', '안녕', 'Hi']
a.remove("안녕") #해당 요소를 삭제
print(a) #['a', 'b', 'Hi']
a.insert(2, "잘가") #2번째 인덱스에 요소 추가삽입
print(a) #['a', 'b', '잘가', 'Hi']
a.clear() #인덱스 요소 전부 삭제
print(a) #[]

x=["Q", "W", "E", "R", "W"] 
print(x.count("W"))#해당 요소 갯수 출력

#이차원 리스트
"""
리스트 안에 리스트를 넣을 수 있다.
행과 열로 이루어진 데이터 표현
리스트변수=[[요소1,요소3...],[요소2,요소4...]]
행 : 각 리스트가 한 행
열 : 각 리스트의 요소가 해당 열
"""
