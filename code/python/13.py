#전역변수
quantity=10

def get_price(price): #price는 매개변수 '5000'을 부르고있다.
    return price*quantity

print(f"{quantity}개의 가격은 {get_price(5000)}입니다.")

#지역변수
def oneUp():
    x=0
    x+=1
    return x

print(oneUp())
# print(x)


#함수호출 키워드
def introduce(name,age,city):
     print(f"이름은{name}이고, 나이는 {age}이고, 사는 곳은 {city}입니다.")
introduce("allie",23,"서울")
introduce("allie",city="서울", age=23)

#가변키워드매개변수
def print_info(**kwargs):
    print(kwargs) #dictraionary
print_info(name="홍길동",ciry="서울", gender="남자")
print_info(name="성춘향",ciry="부산", age=30)