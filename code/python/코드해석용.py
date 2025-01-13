# 날짜, 지역, 온도, 강수량
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]

# 1. 도시별 평균 기온 계산
def cal_temp(n):
    count = 0 # 기록 갯수
    total_temp = 0 # 총 기온

    specific_list = filter(lambda x: x[1] == n, weather_data)
    temperature_list = list(map(lambda x: x[2], specific_list))

    for i in range(len(temperature_list)):
        total_temp += temperature_list[i]
        count += 1
    

    return total_temp / count

def get_avg_temp():
    city = input("도시 이름을 입력하세요: ")
    
    return f"{city}의 평균 기온: {cal_temp(city): .2f}℃"

# 2. 도시별 최고/최소 기온 찾기
def max_min_temp(n):
    specific_list = filter(lambda x: x[1] == n, weather_data)
    temperature_list = list(map(lambda x: x[2], specific_list))
    
    return (max(temperature_list), min(temperature_list))


def get_min_max_temp():
    city = input("도시 이름을 입력하세요: ")

    max, min = max_min_temp(city)

    return f"{city}의 최고 기온: {max}℃, 최저 기온: {min}℃"

# 3. 도시별 강수량 분석
def total_rain(n):
    count = 0 # 기록 갯수
    total_rain = 0 # 총 강수량

    a = filter(lambda x: x[1] == n, weather_data)
    rain_list = list(map(lambda x: x[3], a))

    for i in range(len(rain_list)):
        total_rain += rain_list[i]
        if rain_list[i] != 0:
            count += 1

    return (total_rain, count)

def get_rain():
    city = input("도시 이름을 입력하세요: ")

    total, count = total_rain(city)

    return f"{city}의 총 강수량: {total}mm \n{city}의 강수량이 있었던 날: {count}일"
    

# 4. 날씨 데이터 추가
def add_weather():
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시를 입력하세요: ")
    avg_temp = float(input("평균 기온을 입력하세요 (℃): "))
    rain = float(input("강수량을 입력하세요 (mm): "))

    weather = [date, city, avg_temp, rain] # 날짜, 도시, 기온, 강수량
    weather_data.append(weather)
    weather_data.sort() # 날짜 중심으로 정렬

    return f"{city}의 날씨 데이터가 추가되었습니다."


# 5. 전체 데이터 출력
def total_print():
    for i in range(len(weather_data)):
        print(weather_data[i])
    
    return ""


while True:
    print("--------------------------------")
    print("[날씨 데이터 분석 프로그램]")
    print("1. 평균 기온 계산")
    print("2. 최고/최저 기온 찾기")
    print("3. 강수량 분석")
    print("4. 날씨 데이터 추가")
    print("5. 전체 데이터 출력")
    print("6. 종료")

    func_num = input("원하는 기능의 번호를 입력하세요: ")

    if func_num == '1':
        print(get_avg_temp())

    elif func_num == '2':
        print(get_min_max_temp())

    elif func_num == '3':
        print(get_rain())

    elif func_num == '4':
        print(add_weather())

    elif func_num == '5':
        print(total_print())

    elif func_num == '6':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 값을 입력했습니다.")

    print("--------------------------------")