#datetime 날짜와 시간의 조작 및 형식화를 제공하는 기본 모듈
from datetime import datetime, timedelta, date
import time

#datetime 모듈 사용
now = datetime.today() #현재 날짜 및 시간

print(now)
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")


now=datetime.now()
print(now)

# 특정 날짜 연산
next_week=now+timedelta(weeks=1,hours=1)
print(next_week)
next_week=now-timedelta(weeks=1,hours=2)
print(next_week)

open_day=date(year=2024,month=12,day=30) #12월30일 날짜 생성

print(date.today())# today : 오늘 날짜 출력
print(date.today().weekday()) # weekday : 요일을 숫자로 반환 # 0:월요일~6:일요일

week=["월","화","수","목","금","토","일"]
print(week[date.today().weekday()]) # 인덱싱으로 요일을 숫자에서 문자로 표현

pass_day= date.today()-open_day
print(pass_day.days)


# import time 이후
print(time.time())
# 타임스탬프 값 출력
# 1970년 1월 1일 00:00:00을 기준으로 했을때 현재까지의 시간 초 단위
# 따라서 현재 시점에 따라 값이 달라짐.


print(time.localtime()) # 로컬 시간대 출력
#서울을 기준으로 한 시간대 (윈도우 세팅)

print("2초대기")
time.sleep(2)
print("대기완료")

start_time= time.perf_counter() #시간측정
time.sleep(1)
end_time=time.perf_counter()


print(end_time-start_time)