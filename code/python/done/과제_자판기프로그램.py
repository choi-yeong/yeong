#과제 자판기 프로그램
"""
vanding_machine=['게토레이','게토레이','레쓰비','레쓰비','생수','생수','이프로']
while 1 :
    user=input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
    if user=="1":
        drink=input("마시고 싶은 음료는?")
        if drink in vanding_machine :
            vanding_machine.remove(drink)
            print(f"{drink}를 드리겠습니다.")
            print(f"남은 음료수:{vanding_machine}")
        else:
            print("그딴 음료수는 없습니다. 장난치지마세요.")
    elif user=="2":
        doing=input("할 일 선택:\n1.추가\n2.삭제\n")
        if doing=="1":
            drink=input("추가할 음료수?")
            if drink in vanding_machine:
                st=vanding_machine.index(drink)
                vanding_machine.insert(st,drink)
                print("추가완료.")
                print(f"남은 음료수:{vanding_machine}")
            else :
                vanding_machine.insert(0,drink)
                print("추가완료.")
                print(f"남은 음료수:{vanding_machine}")


        elif doing=="2":
            drink=input("삭제할 음료수?")
            if drink in vanding_machine:
                vanding_machine.remove(drink)
                print("삭제완료")
                print(f"남은 음료수 : {vanding_machine}")
            else :
                print("그딴 음료수는 없습니다. 장난치지마세요.")
        else :
            print("이상한 행동이 감지되어 자판기가 폭발합니다.")
            break
    else:
        print("이상한 동작이 감지되어 자판기가 폭발합니다.")
        break
print("자판기 종료.")
"""

#과제 자판기 프로그램 함수화
vanding_machine=['게토레이','게토레이','레쓰비','레쓰비','생수','생수','이프로']
#1.남은 음료수를 확인할 수 있는 함수
def check_machine():
    print(f"남은 음료수 :{vanding_machine}")
    return
#2. 음료수가 있는지 확인하는 함수
def is_drink(drink):
    if drink in vanding_machine:
        return drink
    else :
        return
#3. 음료수를 추가하는 함수
def add_drink(drink):
    if is_drink(drink):
        ind=vanding_machine.index(drink)
        vanding_machine.insert(ind,drink)
        return
    else :
        vanding_machine.append(drink)
        return
    print(f"음료수 \"{drink}\"를 추가했습니다.")
    return 
#4. 음료수를 제거하는 함수
def remove_drink(drink):
    if is_drink(drink):
        return vanding_machine.remove(drink)
    else :
        print("그런 음료수는 없습니다.")
    return


while 1 :
    user=int(input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n그외. 종료\n"))
    if user==1:
        drink=input("마시고 싶은 음료는?")
        remove_drink(is_drink(drink))
        check_machine()
    elif user==2:
        doing=int(input("할 일 선택:\n1.추가\n2.삭제\n"))
        if doing==1:
            drink=input("추가 할 음료는?")
            add_drink(drink)
        elif doing==2:
            drink=input("제거 할 음료는?")
            remove_drink(drink)
        else :
            print("알 수 없는 행동입니다.")
        check_machine()
    else :
        print("자판기를 종료합니다.")
        break
