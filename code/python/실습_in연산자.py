fruits={"apple":95,"banana":105,"cherry":50}
fruit=input("과일을 영문으로 입력하세요. : ")
if fruit in fruits :
    print(f"{fruit}의 칼로리는 {fruits[fruit]}Kcal입니다.")
else :
    print("그런 과일은 사전에 포함되어있지 않습니다.")