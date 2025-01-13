# 정적(static) 메서드 : cls나 self를 사용하지 않음.
# @staticmethod 데코레이터 사용
# 클래스와 독립적인 작업(예: 유틸리티 함수)을 정의할 때 유용
# 클래스나 인스턴스와 관계없는 기능이 필요할 때

class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
print(MathUtils.add(10,20))
print(MathUtils.multiply(10,20))

#but, 일반함수의 경우

def add(a,b):
    return a+b
    
def multiply(a,b):
    return a*b

print(add(10,20))
print(multiply(10,20))

# "일반 함수로도 충분한데 뭐하러 정적메소드가 필요하지?"
# >> 클래스 외부에서 함수가 독립적으로 존재.
# = 함수들이 어떤 맥락에서 사용되는지 직관적으로 알기 어려울 수 있음.
# 따라서, 협업 시 개발자들끼리 유지보수하기 편하기 위해 관리용으로 스태틱함수 사용.
# self,cls와 같은 첫번째 매개변수가 필요하지 않음 = 클래스변수나 인스턴스변수에 접근 불가능.
# 유틸리티 함수처럼 사용.