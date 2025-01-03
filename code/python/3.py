#입력함수 사용 테스트
song = input("당신의 최애 노래는?")
print(song)
print(type(song)) #input으로 받는 값의 자료형은 항상 문자열이다.

a=input("1+1= ?")
print(a)
print(a*2) #a를 2번 반복해버린다... (곱하기2를 하려는 의도였다면 a의 자료형을 int나 float으로 바꿔줘야한다.)

#자료형을 바꾸는 방법 (type casting, type conversion)
# int("문자열") # 문자열을 int 정수형으로 바꿔준다.
# float("문자열") #문자열을 float 실수형으로 바꿔준다.
print(float(a)*2) #float형이라서 소수점이 나오지만 int형으로 하면 소수점이 안나온다.
print(int(a)*3)

b=2 #정수형
print(b*10)
print(str(b)*10)

# print(b + "입니다.") : int형 b와 str형 "입니다."는 서로 더하기(+)할수 없다.
print(str(b)+"입니다.", " : str형 \"b\"와 str형 \"입니다.\"는 더하기로 서로 붙여줄수있다.") # str형 "b"와 str형 "입니다."는 더하기로 서로 붙여줄수있다.
print(str(b)*10, " : str형 \"b\"와 int형 10을 곱해주면 str형 \"b\"를 10번 반복하겠다는 뜻이다.") #str형 "b"와 int형 10을 곱해주면 str형 "b"를 10번 반복하겠다는 뜻이다.