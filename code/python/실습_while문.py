while 1 :
    enter=input("양수를 입력하세요(\'종료\'입력 시 프로그램 종료) : ")
    sum=0
    cont=0
    num=0
    if enter=="종료":
        print("프로그램을 종료합니다.")
        break
    elif enter.isdigit():  #음수는 '-'(하이픈)을 포함하는 문자열이라 숫자만으로 이루어진 데이터라고 판단하지 않아서 false를 출력해버린다;;
        num = int(enter)
        cont=num
        if num>=0:
            while num>0:
                sum=sum+num
                num-=1
            print(f"0부터 {cont}까지 합은 {sum}입니다.")
        else :
            print("양수를 입력하세요.")
    else :
        print("먼가 잘못됨.")