#오버라이딩 : 상속된 메서드의 내용이 자식 클래스에 맞지 않을 경우, 자식클래스에서 동일한 메서드를 재정의 하는 것.
#오버라이딩한 메서드는 부모 메서드의 매개변수 개수와 동일하게 사용하는 것을 권장.
class Parent:
    def greet(self):
        print("안녕하세요, 저는 부모 클래스입니다.")
class Child(Parent):
    def greet(self): #오버라이딩
        Parent().greet() #부모클래스의 greet 호출. 이걸 지우면 자식클래스만 나옴.
        print("안녕하세요. 저는 자식 클래스입니다.")

parent=Parent() #부모클래스의 인스턴스
child=Child() #자식클래스의 인스턴스
parent.greet()
print()
child.greet()