#for문 
"""
for i in range():
^^^ for문을 사용할거다.
    ^ 변수는 i다.
      ^^언제까지냐면
         ^^^^^^range()의 시퀀스까지다!
range(시작,종료,스탭)
시작 : 몇부터 시작해서
종료 : 몇까지 세알릴건데
스탭 : 몇칸씩 건너 세알려라.
"""
for i in range(11,20,2):
    print(i,end=" ")
print() #다음 코드와 헷갈리지 않게 줄바꿈용.

#list와 for문
fruits =["사과", "바나나", "포도", "체리"]
for fruit in fruits :
    print(fruit,end="|")
print() #다음 코드와 헷갈리지 않게 줄바꿈용.

numbers=[1,2,3,4,5,6,7,8,9,10]
total=0
for num in numbers:
    total+=num
print(f"합계는 {total}입니다.")
print() #다음 코드와 헷갈리지 않게 줄바꿈용.

my_dic = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"],
}