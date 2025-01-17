class Health:
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name=name
    def get_hp(self):
        return self._hp 
    def set_hp(self,value):
        if value>100:
            self._hp=100
        elif value<1:
            self._hp=1
        else:
            self._hp=value
    def exercise(self, hour):
        #시간당 hp값 증가
        self.set_hp(self._hp+hour)
        #얼마나 운동했는지 정보출력
        print(f"{hour}시간 운동하다.")
    
    def drink(self, cups):
        #시간당 hp값 증가
        self.set_hp(self._hp-cups)
        #얼마나 운동했는지 정보출력
        print(f"술을 {cups}잔 마셨다.")

    def info(self):
        print(f"{self.get_name()}님의 hp는 {self.get_hp()}입니다.")
    
p1 = Health("나몸짱")
p1.set_hp(80)
p1.exercise(4)
p1.drink(2)
p1.info()

p2 = Health("나약해")
p2.set_hp(20)
p2.exercise(2)
p2.drink(4)
p2.info()