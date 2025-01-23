class Product: #부모클래스
    def __init__(self,name,price,quantity): #생성자
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
        print("가격:",self.price,"원")
        print("재고:",self.quantity,"개")

#자식 클래스들....
class Electronic(Product): #자식클래스 1
    def __init__(self,name,price,quantity,warranty=12):
        Product.__init__(self,name,price,quantity)
        self.warranty=warranty

    #보증기간 연장하는 메서드
    def extend_warranty(self,months):
        self.warranty+=months
        print(f"보증기간이 {months}개월 연장되었습니다. 현재 보증기간:{self.warranty}개월")
        return  self.warranty
    #오버라이딩 메서드
    def display_info(self):
        super().display_info() #부모 메서드 호출
        print("보증기간 :",self.warranty,"개월") #추가내용 입력

tv=Electronic("스마트 TV", 15000000, 5, 24)

tv.display_info()
tv.extend_warranty(12)
tv.display_info()
tv.update_quantity(3)
tv.update_quantity(-2)
tv.display_info()

class Food(Product):
    def __init__(self,name,price,quantity,expiration_date):
        super().__init__(name,price,quantity)
        self.expiration_date=expiration_date
        
    #유통기한 확인하는 메서드
    def is_expired(self,current_date): #현재날짜
        if current_date>self.expiration_date:
            print(f"{self.name}은 유통시간이 지났습니다.")
        else:
            print(f"{self.name}은 유통기한이 지나지 않았습니다.")
    #오버라이딩 메서드
    def display_info(self):
        super().display_info()
        print(f"유통기한:{self.expiration_date}")


milk=Food("초코우유",3000,30,"2025-01-31")
milk.is_expired("2025-01-14")
milk.is_expired("2025-02-14")
milk.display_info()