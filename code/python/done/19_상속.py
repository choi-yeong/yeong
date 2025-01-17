"""
일반적인 클래스
class namal:

부모를 둔 자식클래스
class child(namal):

"""

#예시
"""
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")
    def move(self):
        print("동물이 움직입니다.")
#자식클래스
class Dog(Animal):
    def bark(self):
        print("멍멍!")
class Cat(Animal):
    def meow(self):
        print("야옹~")
dog=Dog()
dog.speak()
dog.move()
dog.bark()

cat=Cat()
cat.speak()
cat.meow()
cat.move()
"""
#부모클래스에 생성자가 있는 경우
"""
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name}이(가) 소리 냅니다.")
    def move(self):
        print(f"{self.name}이(가) 움직입니다.")
#자식클래스
class Dog(Animal):
    def __init__(self,name,sound):
        super().__init__(name)
        self.sound=sound
    def bark(self):
        print(f"{self.name}이(가) {self.sound} 짖습니다.")
class Cat(Animal):
    def __init__(self,name,sound="크아악"):
        super().__init__(name) #단일 상속이라서 super()으로 불러올수있음.
        self.sound=sound
    def meow(self):
        print(f"{self.name}이(가) {self.sound} 웁니다.")
dog=Dog("백구","멍멍!")
dog.speak()
dog.move()
dog.bark()

cat=Cat("나비","냐옹~")
cat.speak()
cat.meow()
cat.move()

cat2=Cat("톰")
cat2.speak()
cat2.meow()
cat2.move()
"""
#다중상속 (파이썬만 가능)
class Engine:
    def __init__(self, horspower):
        self.horspower=horspower
class Wheels:
    def __init__(self,wheel_count):
        self.wheel_count=wheel_count
class Car(Engine,Wheels):
    def __init__(self,horspower, wheel_count):
        Engine.__init__(self, horspower) #첫번째 부모 생성자 호출
        Wheels.__init__(self,wheel_count) #두번째 부모 생성자 호출
    def info(self):
        print(f"이 자동차는 {self.horspower} 마력 엔진과 {self.wheel_count}개의 바퀴를 가지고 있습니다.")

car=Car(1500,4)
car.info()
print(Car.mro()) #MRO : Method Resolution Order, 매서드 해석 순서. 다중상속에서 매서드 호출순서를 결정하는 규칙.

