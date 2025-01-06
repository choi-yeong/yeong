#1번
name = input("1.이름을 입력하세요.")
age = input("1.나이를 입력하세요.")
print(f"1.안녕하세요! {name}님 ({age})")

#2번
name2 = input("2.이름을 입력하세요.")
born2 = input("2.태어난 년도를 입력하세요.")
year2 = input("올해 년도를 입력하세요.")
print(f"올해는{year2}년, {name2}님의 나이는 {int(year2)-int(born2)}세 입니다.")

"""
2번 문제 나이 계산할 때
input은 자료형 str형으로 받기 때문에
int()로 자료형을 int로 강제변환하여 계산했습니다.
"""