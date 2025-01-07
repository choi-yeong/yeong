"""
#구구단 만들기
enter=input("몇단을 출력할까요?: ")
if not enter.isdigit():
    print("정수를 입력하세요.")
else :
    num = int(enter)
    for i in range(1,10):
        print(f"{num}x{i}={num*i}")

#정수 합 계산
enter1=input("어디까지 계산할까요?: ")
if not enter1.isdigit():
    print("정수를 입력하세요.")
else :
    sum=0
    num1 = int(enter1)
    for i in range(1,num1+1,2):
        sum=sum+i
    print(f"1부터{num1}까지의 홀수의 합 : {sum}")
"""
#평균값 구하기
students={
    "철수":[83, 92, 88],
    "영희":[90, 79, 86],
    "맹구":[88, 86, 94]
}
for student in students:
    sum_korean=student[0]
    sum_english=student[1]
    sum_math=student[2]  #여기 에러 왜남?
print(f"국어 평균점수 : {sum_korean/3}")
print(f"영어 평균점수 : {sum_english/3}")
print(f"수학 평균점수 : {sum_math/3}")