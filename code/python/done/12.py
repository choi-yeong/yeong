#함수 (매개변수o,리턴x)
def print_greeting(name):
    print(f"Hello, {name}")
print_greeting("Allie")
print_greeting("Martin")
#출력되는 Heloo,Allie는 리턴값이 아니라 함수내부 수행이다.

#매개변수 2개인 함수(리턴x)
def gugudan(dan,end):
    print(f"{dan}단 시작!")
    for i in range(1,end+1):
        print(f"{dan}x{i}={dan*i}")
gugudan(7,15)

#매개변수x, 리턴o
def mul_number():
    print("곱셈을 시작합니다.")
    return 10*5
result=mul_number()
print(result)
# print(mul_number()) 도 가능

#매개변수o, 리턴값 o
def add_numbers(x,y):
    print("덧셈을 시작합니다.")
    return x+y
result2=add_numbers(40,50)
print(result2)


#다양한 타입을 return하는 함수
#1. list 타입을 반환하는 함수
#ex. 제한값(limit)까지의 짝수를 출력하는 함수
def print_even_number(limit):
    return[i for i in range(0,limit) if i%2==0]
print(print_even_number(10))

#Dictionary 타입을 변환하는 함수
def print_user_info(name,grade):
    return {"name":name, "grade":grade}

print(print_user_info("Aliile",2))
print(print_user_info("Bob",4))

# print(set("달팽이고기이빨"))
# 3. set타입을 반환하는 함수
def print_unique_char(word):
    return set(word)
print(print_unique_char("Hi, My mame is Sean"))

# 4. Tuple 타입으로 반환하는 함수
# 두 숫자의 합과 곱을 동시에 반환
def calculate_sum_and_product(a,b):
    return(a+b,a*b)
print(calculate_sum_and_product(3,5))
print(calculate_sum_and_product(7,8))
"""
#Collection(컬렉션)
def split_nums(numbers):
    even_nums=[n for n in numbers if n%==0]
    odd_nums=[n for n in numbers if n%==0]

return {"odd":odd_nums,"even":even_nums}
"""


