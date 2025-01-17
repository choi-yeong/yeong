#람다식
def add (x,y): #일반함수 선언
    return x+y
print(add(3,4))

add2=lambda x,y:x+y #람다식
print(add2(4,5))

#매개변수 1개 람다식
trisquare= lambda x:x**3
print(trisquare(5))

#매개변수 2개 람다식
trisquare= lambda x,y:x*y
print(trisquare(5,2))

#람다식을 매개변수로 전달
print("콜백함수")
def call(func):
    for _ in range(10):
        func()
def hello():
    print("안녕")
#람다식으로 정의된 함수 hello2
hello2=lambda:print("하이")

call(hello)
call(hello2)


#map과 람다식
numbers=[2,4,6,8,10]
print(list(map(lambda x:x**3,numbers)))

#filter와 람다식
numbers2=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,numbers2)))

#map과 filter와 람다식
print(list(map(lambda x:x**2,filter(lambda x:x%2==0, numbers2))))