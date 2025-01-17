#파이썬 조건문
"""
age_s=input("나이를 입력하세요.")
age=int(age_s)
print(f"나이는 {age}입니다.")
if age<20:
    print("미성년자입니다.")
    print("술과 담배를 구매할 수 없습니다.")
    print("클럽입장도 안되세요 ^^.")
else :
    print("성인입니다.")
    print("술과 담배를 구매 가능합니다.")
    print("클럽입장도 가능합니다.")

# elif문
"""
"""
if:
if:
경우 if조건문에 true가 중첩되면 두개의 if문이 동시에 실행되며 중복됨.
if:
elif:
경우 위의 if문에 해당되면 elif는 작동되지 않고, 위 if문이 거짓일때만 elif 코드가 작동됨.
"""
"""
if age<20:
    print("10대 이십니다.") #~20
if age<30:
    print("20대 이십니다.") #~30
if age<40:
    print("30대 이십니다.") #~40
if age<50:
    print("40대 이십니다.") #~50

if age<20:
    print("10대 이십니다.") #~20
elif age<30:
    print("20대 이십니다.") #20~30
elif age<40:
    print("30대 이십니다.") #30~40
else :
    print("40대 이상 이십니다.")#40~


#삼항연산자 (파이썬)
# 참일때 값 if 조건 else 거짓일 때 값
print("삼항 성인입니다." if age>19 else "삼항 미성년자입니다.")
print("짝수" if age>19 else "홀수")
#중첩 삼항 연산자
score = int(input("점수를 표시"))
grade = "A" if score >=90 else ("B" if score>=80 else"C")
#           ^^            ^^^^ (    ^^           ^^^^   ) 괄호를 늦게함.
print(grade)

#pass : 코드를 구현하긴 해야하는데 나중에 짜야해서 지금은 넘겨야할 때.


#조건문에서 in 연산자 활용
users =["Sean", "Linda", "Allie", "Martin"]

username=input("이름을 입력하세요>>")

if username in users:
    print(f"환영합니다. {username}님!")
else :
    print(f"{username}은 등록되지 않은 사용자입니다. 회원가입을 진행해주세요.")

"""
#break문
while 1 :
    num = int(input("숫자입력(0입력시 종료)>>"))
    if num==0:
        print("프로그램 종료")
        break
    
    print(f"입력하신 숫자는{num}입니다.")

#continue문
while 1:
    num_1 = int(input("숫자입력( 음수 입력시 종료)>>"))

    if num_1<0:
        print("프로그램 종료")
    if num_1%2!=0:
        continue #홀수건너뛰기
    print(f"입력한 짝수는 {num}입니다.")