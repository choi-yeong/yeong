class TestClass:
    pass

test_instance=TestClass()

class Car :
    #2개의 속성을 가짐.
    model=""
    cc=0

    def __init__ (self,model,cc): #생성자
        self.model=model
        self.cc=cc

    def info(self):
        print(f"모델명:{self.model}, 배기량:{self.cc}cc")
"""
car1=Car()
car1.model="아반떼"
car1.cc=1600
car2=Car()
car2.model="K5"
car2.cc=2000

print("모델명 :",car2.model)
print("배기량 :",car2.cc)
print("모델명 :",car1.model)
print("배기량 :",car1.cc)
"""
car3=Car("싼타페",2000)
car4=Car("BMW",2200)

#car1.info()
#car2.info()  #생산물(instance)
car3.info()  #생산물(instance)
car4.info()  #생산물(instance)