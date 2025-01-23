class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
#재고 업데이트 매서드
    def update_quantity(self,amount):
        self.quantity+=amount
        print(f"{self.name} 재고가 {amount}만큼 {"증가"if amount>0 else "감소"}했습니다. 현재 재고 : ",self.quantity)
        
        #상품 정보 출력 메서드
    def display_info(self):
        print("상품명:",self.name)
        print("가격:",self.price)
        print("재고:",self.quantity,"개")
    
class Electronic(Product):
    def __init__(self,name,price,quantity,warranty=12):
        Product.__init__(self,name,price,quantity)
        self.warranty=warranty
    def extend_warranty(self,months):
        self.warranty+=months
        print(f"보증기간 {months}개월 연장되었습니다.")
        return  self.warranty
    def display_info(self):
        super().display_info()
        print("보증기간 :",self.warranty,"개월")

tv=Electronic("스마트 TV", 15000000, 5)

tv.display_info()
tv.extend_warranty(12)
tv.display_info()

class Food(Product):
    current_date=2025-01-14
    def __init__(self,name,price,quantity,date):
        Product.__init__(self,name,price,quantity)
        self.expiration_date=date
    def is_expired(self,current_date):
        if current_date>self.expiration_date:
            print(f"이 {self.name}은 신선합니다.")
        else :
            print(f"이 {self.name}은 썩었습니다.")