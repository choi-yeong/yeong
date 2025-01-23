#클래스 메서드

# 1) 대체 생성자(Alternative Constructor)패턴
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    @classmethod
    def form_birth_year(cls, name, birth_year): #cls = class 즉, Person 클래스를 말한다.
        age=2025-birth_year
        return cls(name,age) #Person(name,age)
    
p1=Person("김철수",20) #기본생성자로 객체생성
p2=Person.form_birth_year("홍길동",1990) #생년도를 이용해 대체생성자로부터 객체 생성
print(p1.name,p1.age)
print(p2.name,p2.age)

#class인 Person(이름,나이)로 인스턴트를 생성하는 방법과
#class의 메소드인 Person.from_birth_yeear(이름,나이)로 인스턴트를 대체생성하는 방법이 있다.


# 2)유틸리티 함수 구현
# 유틸리티 함수? 여러곳에서 재사용할 수 있는 특정한 기능을 하는 독립적인 함수
# ex. 마일 단위를 킬로미터로 단위 변환
class Converter:
    conversion_rate = 1.60934 #클래스 변수
    @classmethod
    def miles_to_km(cls,mile):
        return mile*cls.conversion_rate
    
my_mile=7
print(Converter.miles_to_km(my_mile))
#객체 생성없이 바로 클래스.메서드명()으로 사용 가능. = 클래스메서드의 존재이유. 간편!


# 3) 클래스 변수 수정
# 모든 인스턴스가 공유하는 값을 관리해야 할 때
class Counter:
    count=0
    @classmethod
    def increment(cls):
        cls.count +=1
    @classmethod
    def get_count(cls):
        return cls.count

Counter.increment()
print(Counter.get_count())

# 4) 자식 클래스의 정보 유지
class Animal:
    species ="동물"

    @classmethod
    def get_species(cls):
        return cls.species

class Dog(Animal):
    species="진돗개"

print(Animal.get_species())
print(Dog.get_species())  #Dog 클래스가 부모인 Animal클래스에서 가져온 get_species클래스에서 species를 "진돗개"로 바꿨기 때문에
# Dog.get_species의 리턴값인 cls.species는 진돗개를 리턴하게 되고  프린트하면 진돗개를 출력한다.