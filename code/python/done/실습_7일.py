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
sum_korean=0
sum_english=0
sum_math=0
for student in students:
    sum_korean=sum_korean+students[student][0]
    sum_english=sum_english+students[student][1]
    sum_math=sum_math+students[student][2]
print(f"국어 평균점수 : {sum_korean/3}")
print(f"영어 평균점수 : {sum_english/3}")
print(f"수학 평균점수 : {sum_math/3}")


# 문제 풀이 (학생 국영수 평균값)
students = {
    "학생1" : {"국어":83, "영어":92, "수학":88},
    "학생2" : {"국어":90, "영어":79, "수학":94},
    "학생3" : {"국어":88, "영어":86, "수학":94},
}
for student, scores in students.items():
    total_score=sum(scores.values()) #국어 영어 수학 점수의 합계
    average_score=total_score/len(scores) #평균계산
    print(f"{student}의 평균 점수 : {average_score:.2f}")
# :.2f ; 소수 두번째 자리까지 표시하라.
# round(average_score,2) ; 소수점 두번째 자리까지 표시하라.
