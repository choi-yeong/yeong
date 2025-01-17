money =0
way="결제수단"
age = int(input("나이를 숫자로 입력해주세요. : "))
if age<0:
    print("나이는 음수값이 될 수 없습니다.")
elif age<8:
    print("8세 미만 어린이 요금은 무료입니다.")
elif age<14:
    print(f"{age}세 어린이 요금은 450원입니다.")
elif age>=75:
    print("75세 이상 경로 요금은 무료입니다.")
elif 14<=age<75:
    way=input("결제방법을 입력해주세요. (현금 또는 카드) : ")
    if age>20:
        if way=="카드":
            print(f"{age}세의 카드 요굼운 720원입니다.")
        elif way=="현금":
            print(f"{age}세의 현금 요금은 1000원입니다.")
        else :
            print("결제수단을 \"카드\" 또는 \"현금\"으로만 입력해주세요.")
    else :
        if way=="카드":
            print(f"{age}세의 카드 요굼운 1200원입니다.")
        elif way=="현금":
            print(f"{age}세의 현금 요금은 1300원입니다.")
        else :
            print("결제수단을 \"카드\" 또는 \"현금\"으로만 입력해주세요.")
else :
    print("나이를 숫자로만 입력해주세요.") #숫자 외 입력시 이미 int(input())에서 오류로 걸러짐.
