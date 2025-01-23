for i in range(2,10):
    print(f"[{i} 단]")
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

#선택실습_별찍기1
for i in range(3):
    print("")
    for j in range(5):
        print("*",end="")

#선택실습_별찍기2
for i in range(5):
    print("")
    for j in range(i+1):
        print("*",end="")

#선택실습_별찍기3
for i in range(5):
    print("")
    for j in range(5,i,-1):
        print("*",end="")

#선택실습_별찍기3 (인풋응용,정수외 입력시 오류 뜨는거 방치함.)
max=int(input("몇 줄 생성할지 정수를 입력하세요 : "))
for i in range(max):
    print("")
    for j in range(max,i,-1):
        print("*",end="")
print()

#선택실습_별찍기4