class Supermarket:
    """
    location = ""
    name=""
    product=""
    customer=""
    """ #안 넣어도 되는 코드
    total_customer=0 #전체 고객수


    def __init__(self,location,name,product,customer):
        self.location=location
        self.name=name
        self.product=product
        self.customer=customer
        Supermarket.total_customer+=customer

    def print_location(self):#위치를 출력하는 함수
        print("위치 :",self.location)
    def change_category(self, new_product): #파는 물건 설정
        self.product=new_product
    def show_list(self): #현재 파는 물건 출력
        print("상품 : ",self.product)
    def enter_customoer(self): #손님의 수를 1씩 늘리는 함수
        #self.customer +=1
        Supermarket.total_customer+=1
    def show_info(self): #가게의 모든 정보 출력
        #print(f"위치:{self.location}, 이름:{self.name}, 상품:{self.product}, 고객수:{self.customer}")
        print(f"위치:{self.location}, 이름:{self.name}, 상품:{self.product}, 총 고객수:{self.total_customer}")


maketon=Supermarket("마포구 도화동", "마켓온 도화점", "음료", 10)
maketon.enter_customoer()
maketon.print_location()
maketon.show_list()
maketon.show_info()

print("**상품 카테고리를 변경합니다. **")
maketon.change_category("빵")
maketon.show_list()
print("**손님이 한분 더 입장힙니다. **")
maketon.enter_customoer()
maketon.show_info()

s2=Supermarket("마포구 염리동","마켓온 염리점","아이스크림",20)
s2.enter_customoer()
s2.print_location()
s2.show_list()
s2.show_info()