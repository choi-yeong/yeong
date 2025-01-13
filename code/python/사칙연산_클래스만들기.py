class Cal:
    def __init__(self,a,b): #생성자
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b==0:
            return "0으로 나눌 수 없습니다."
        else:
            return self.a/self.b
    """
        else:
             return을 지우고

    return self.a/self.b
    이렇게 else없이 바로 리턴으로 종료시킬수있다.
    이걸 "얼리리턴(ealy return)이라 하고 조건문이 만족되면 미리 리턴할 수 있어서 속도면에서 도움된다고 한다.
    """
    
cal=Cal(5,2)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())



class Dog:
    kind = "진돗개" #클래스 변수
    
    def __init__(self,name):
        self.name=name #인스턴스 변수

dog1=Dog("백구")
dog2=Dog("흑구")

print(dog1.name) #독립적인 이름 :인스턴스변수
print(dog2.name) #독립적인 이름 :인스턴스변수
print(dog1.kind) #모든 인스턴스와 공유하는 변수 : 클래스 변수 
print(dog2.kind) #모든 인스턴스와 공유하는 변수 : 클래스 변수
print(Dog.kind) #모든 인스턴스와 공유하는 변수라서 전역변수처럼 클래스만 불러도 나옴.
#보통 클래스변수는 클래스에서 불러와야 오해가 없으므로 실무에선 클래스변수는 클래스로 호출하자.


### 
"""
class Example :
    sheared="공유 변수" #클래스변수
    def __init__ (self,name):
        self.name=name #인스턴스 변수

class Employee:
    serial_num=1000
    def __init__(self,name):
        Employee.serial_num+=1
        self.id=Employee.serial_num
        self.name=name
    def __str__(self):
        return f"사번: {self.id}, 이름: {self.name}"
    
em1 =Employee("김사랑")
print(em1)
"""
class Example :
    sheared="공유 변수" #클래스변수
    def __init__ (self,name):
        self.name=name #인스턴스 변수

class Employee:
    serial_num=1000 #만약 클래스 변수가 아니라 인스턴스변수로 쓰면 계속 1000으로 초기화되었다가 +1이 되어 1001이 출력되므로 반드시!!!! 클래스변수로 써야한다!
    def __init__(self,name):
        Employee.serial_num+=1
        self.id=Employee.serial_num
        self.name=name
    def __str__(self):
        return f"사번: {self.id}, 이름: {self.name}"

#정보은닉
class Person:
    def __init__(self):
        #멤버변수 (_name, _age)언더스코어?
        #- protected 접근제어로 간주
        #- 외부에서 직접 접근하지 않고, 해당/서브 클래스에서 사용
        # "직접 접근"대신 ->getter/setter 를 이용해서 값을 읽거나 /수정하도록 함.
        self._name=""
        self._age=0
    def setname(self,name):
        self._name=name
    def getname(self):
        return self._name
    def setage(self,age):
        self._age=age
    def getage(self):
        return self._age
    

p1=Person()
p1.setname("흥부")
p1.setage(35)
print("이름:",p1.setname)
print("나이:",p1.setage)
