# 실습
# 1번
password = input("비밀번호를 입력하세요 : ")
if password == "abc123":
    print("비밀번호가 맞습니다")
else:
    print("비밀번호가 틀렸습니다")
# 2번
num = int(input("숫자를 입력하세요 : "))
if num%2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
# 3번
score = int(input("점수를 입력하세요 : "))
if score < 60:
    grade = "F"
elif score < 70:
    grade = "D"
elif score < 80:
    grade = "C"
elif score < 90:
    grade = "B"
else:
    grade = "A"
print(f"학점 : {grade}")