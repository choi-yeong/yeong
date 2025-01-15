from abc import ABC, abstractmethod
electricity_usage = [
    {"date":"2024-11-01","usage":12.5},
    {"date":"2024-11-02","usage":15.3},
    {"date":"2024-11-03","usage":10.8},
    {"date":"2024-11-04","usage":14.2},
    {"date":"2024-11-05","usage":13.6}
]
class ElectricityData(ABC): #추상클래스
    def __init__(self, usage_data, total_usage=0):
        self._usage_date=usage_data
        self._total_usage=total_usage
    
    #getter
    @property
    def usage_data(self):
        return self._usage_date
    
    @property
    def total_usage(self):
        return self._total_usage
    
    #setter
    @usage_data.setter
    def usage_data(self, new_data):
        self._usage_date=new_data
    
    @total_usage.setter
    def usage_data(self, new_total):
        self._total_usage=new_total

    #추상메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass
    @abstractmethod
    def get_usage_on_data(self,date):
        pass

    #일반 메서드
    def add_usage(self,date,usage):
        #self._usage_data 리스트에 {"data":date,"usage":usage} 형식으로 요소 추가.
        self._usage_data.append({"date":date,"usage":usage})

    def remove_usage(self, date):
        self._usage_data=[i for i in self._usage_data if i["date"] != date ]
    

class HomeElectricityData(ElectricityData): #추상클래스인 부모클래스를 상속받는 자식클래스
    #(부모클래스에 있는) 추상메서드 구분
    def calculate_total_usage(self):
        usage_list= [i["usage"] for i in self._usage_data]
        self.total_usage=sum(usage_list)
    
    def get_usage_on_data(self, date):
        for i in self.usage_data:
            if i["date"]==date:
                return i["usage"]
    
    #클래스 메서드 : 인스턴스(객체)가 아닌 "클래스"가 주인인 메서드
    @classmethod
    def filter_date(cls,usage_data, start_data, end_data):
        filter_data=[i for i in usage_data if start_data<=i["date"]<=end_data]
        return cls(filter_data)
    
    #정적 메서드
    @staticmethod
    def max_usage(usage_data):
        return max(usage_data, key=lambda x: x["usage"])
    
    def __str__(self):
        return f"전력 사용량 데이터ㅣ{self.usage_data}"
    
home = HomeElectricityData(electricity_usage)
home.calculate_total_usage()
print("총 전력 소비량", home.total_usage)
my_date="2024-11-03"
print(f"{my_date}의 사용량 : {home.get_usage_on_data(my_date)}")
end_data="2024-11-05"
between_list=HomeElectricityData.filter_date(home.usage_data, my_date, end_data)
print("특정 날짜 범위 내의 사용량", between_list)