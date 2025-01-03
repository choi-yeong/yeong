#입력함수 사용 테스트
song = input("당신의 최애 노래는?")
print(song)
print(type(song)) #input으로 받는 값의 자료형은 항상 문자열이다.

a=input("1+1= ?")
print(a)
print(a*2) #a를 2번 반복해버린다... (곱하기2를 하려는 의도였다면 a의 자료형을 int나 float으로 바꿔줘야한다.)

#자료형을 바꾸는 방법
int("문자열") # 문자열을 int 정수형으로 바꿔준다.
float("문자열") #문자열을 float 실수형으로 바꿔준다.
print(float(a)*2)