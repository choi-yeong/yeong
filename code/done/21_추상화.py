#추상화
#세부사항을 감추고, 필요한 부분만 노출 : 코드를 더 간단하고 명확하게 작성.
# 복잡한 구현 세부 사항을 몰라도 제공된 기능을 사용.
#abc(Abstract Base Class) 모듈을 사용해 추상화 지원.
#"모듈을 최초로 배우게 될 듯..."
#모듈(module):여러 기능들이 뭉쳐진 하나의 <~~.py> 파일
# - 표준 모듈 : python에 기본적으로 내장되어 있음
# - 외부 모듈 : 파이썬 개인 개발자들이 필요에 의해 직접 만든 모듈

#추상클래스 : 하나 이상의 추상메서드를 포함한 클래스
# - 직접 인스턴트화 할수 없으며 상속받아 사용해야함.
# - 생성자, 일반 메서드와 추상 메서드를 모두 포함 가능
# -> 공통된 동작은 추상 클래스에서 정의하고, 구체적인 동작은 자식클래스에서 구현.

#추상매서드 : 선언만 되어있는 메서드
# - 자식 클래스에서 반드시 구현해야하는 메서드로 강제성을 지님.
# -> 만약 자식 클래스에서 추상메서드를 구현하지 못했으면, 추상메서드가 여전히 남아있으므로 인스턴스 생성 불가.

from abc import ABC, abstractmethod #abc모듈 불러오기. abc모듈로부터 ABC클래스와 abstractmethod 불러오기

class PaymentSystem(ABC): #PaymentSystem클래스는 ABC를 상속받는 추상 클래스
    #추상매서드 2개 :P.S클래스에서 구현하지 않고, 상속받을 자식클래스에서 구현할 예정.
    @abstractmethod
    def authenticate(self): #인증처리하는 기능 메소드 예정
        pass
    @abstractmethod
    def process_payment(self,amount): #결제처리 기능 메소드 예정
        pass

    #일반매서드
    def payment_info(self, amount): #결제완료 후 정보출력 메소드
        print(f"{amount}원 결제완료!")

class KakaoPay(PaymentSystem):
    def authenticate(self):
        print("[인증완료]카카오페이")
    def process_payment(self, amount):
        print(f"[결제진행]카카오페이 {amount}원")

class NaverPay(PaymentSystem):
    def authenticate(self):
        print("[인증완료]네이버페이")
    def process_payment(self,amount):
        print(f"[결제진행]네이버페이 {amount}원")
    #네이버페이 클래스에서만 사용하는 일반 메서드
    def discount(self, amount):
        discount_amount=amount*0.05
        print(f"[이벤트]네이버페이 5%이벤트 적용으로 {discount_amount}원 할인")
        return amount-discount_amount #정가 - 할인액=구매액


pay= 3600
kakao=KakaoPay()
kakao.authenticate()
kakao.process_payment(pay)
kakao.payment_info(pay)

# test=PaymentSystem() # 추상메서드가 있어서 인스턴스 생성 불가
# test.authenticate() #따라서 타입에러가 뜸.

naver=NaverPay()
naver.authenticate()
pay_after_discount=naver.discount(pay)
print("할인후 결제액 :",pay_after_discount)