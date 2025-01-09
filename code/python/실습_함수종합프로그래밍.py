weather_data=[
    ["2024-11-20","서울",15.2,0.0],
    ["2024-11-20","부산",18.1,0.0],
    ["2024-11-21","서울",10.5,2.3],
    ["2024-11-21","부산",14.6,1.2],
    ["2024-11-22","서울",8.3,0.0],
    ["2024-11-22","부산",12.0,0.0],
]
"""
도시별 평균기온 계산
도시별 최고/최소 기온찾기
도시별 강수량 분석
데이터 추가
전체 데이터 출력
"""
#평균기온 계산
def avg_dgre(city):
    rows=len(weather_data)
    sum=0
    count=0
    for i in range(0,rows):
        if city in weather_data[i]:
            sum=sum+weather_data[i][2]
            count +=1
        else:
            pass
    return sum/count
#최고/저 기온
def max_min(city):
    rows=len(weather_data)
    max=0
    min=999
    for i in range(0,rows):
        if city in weather_data[i]:
            if weather_data[i][2]>max:
                max=weather_data[i][2]
            if weather_data[i][2]<min:
                min=weather_data[i][2]
            else:
                pass
        else:
            pass
    return max, min
#강수량분석
def rain(city):
    rows=len(weather_data)
    water=0
    days=0
    for i in range(0,rows):
        if city in weather_data[i]:
            water=water+weather_data[i][3]
            if weather_data[i][3]>0:
                days +=1
            else :
                pass
        else:
            pass
    return water,days
#데이터추가
def plusdata():
    date=input("날짜를 입력하세요.")
    city=input("도시를 입력하세요.")
    temp=float(input("평균기온을 입력하세요."))
    rain=float(input("강수량을 입력하세요."))
    weather_data.append([date,city,temp,rain])
    print(f"{city}의 날씨 데이터가 추가되었습니다.")
    return

#전체 데이터 출력
def looks():
    rows=len(weather_data)
    for i in range(0,rows):
        print(f"날짜:{weather_data[i][0]}, 도시:{weather_data[i][1]}, 평균 기온:{weather_data[i][2]}, 강수량:{weather_data[i][3]}")



while 1:
    print("======[날씨 데이터 분석프로그램]======")
    print("1.평균 기온 계산")
    print("2.최고/최저기온 찾기")
    print("3.강수량 분석")
    print("4.날씨 데이터 추가")
    print("5.전체 데이터 출력")
    print("6.종료")
    enter=int(input("원하는 기능의 번호를 입력하세요 :"))
    if enter == 1:
        city=input("도시이름을 입력하세요. :")
        print("서울의 평균기온 : ",avg_dgre(city))
    elif enter==2:
        city=input("도시이름을 입력하세요. :")
        print(f"{city}의 최고 기온 : ",max_min(city)[0])
        print(f"{city}의 최저 기온 : ",max_min(city)[1])
    elif enter==3:
        city=input("도시이름을 입력하세요. :")
        print(f"{city}의 총 강수량 :",rain(city)[0])
        print(f"{city}의 강수일 :",rain(city)[1])
    elif enter==4:
        plusdata()
    elif enter==5:
        looks()
    else:
        print("프로그램을 종료합니다.")
        break