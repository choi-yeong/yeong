########################## [ 기본 세팅 ] ##############################
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By #By 사용하기 위한 모듈
from selenium.webdriver.common.keys import Keys #Keys 사용하기 위한 모듈 (엔터, 리턴 등)
from selenium.webdriver.support.ui import WebDriverWait #webdriverwait를 사용하0기 위한 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options #옵션
import requests, time
chrome_option = Options()
#옵션추가
chrome_option.add_argument("--start-maximized") #최대크기로 열기
# chrome_option.add_argument("--headless") #GUI창 안열고 백그라운드 실행(리소스절약)
service=Service() #생략 귀찮으면 대소문과 구분 후 괄호 다 치면 됨.
driver = webdriver.Chrome(service=Service(), options=chrome_option)
#====================================================================#

########################[ 깃 크 롤 링 ]####################################
# def git_crol(git_id):
#     res=requests.get(f"https://github.com/{git_id}")
#     soup=BeautifulSoup(res.text, "html.parser")
#     name=soup.select_one('span.p-nickname')
#     print("이름 :",name.text.strip())

#     lastline=soup.select_one('relative-time.no-wrap')
#     print("가입일 :",lastline.text.strip())

#     repo=soup.select('span.repo')
#     print("[자주 이용하는 레포지토리]")
#     for i in repo:
#         print(i.text.strip())

# git_crol('choi-yeong')

#=====================================================================#
##########################[ 쇼핑몰 크롤링 ]#############################

# driver.get("https://www.vans.co.kr/")
# search_shoe= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/header/div[1]/div[1]/div[1]/nav/ul[1]/li[2]/a/span')))
# search_shoe.click()
# # search_cost=[WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="wrapper"]/main/section/div[4]/section/ul/li[1]/div/div[2]/p[2]/span')))]
# # value1=search_cost[0].text.replace(" 원","")
# # value=value1.replace(",","")
# # print(value)
# # if int(value)>50000:


# for i in range(1,10):
#     search_name=[WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="wrapper"]/main/section/div[4]/section/ul/li[{i}]/div/div[2]/p[1]/a')))]
#     search_cost=[WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="wrapper"]/main/section/div[4]/section/ul/li[{i}]/div/div[2]/p[2]/span')))]
#     value1=search_cost[0].text.replace(" 원","")
#     name=search_name[0].text
#     value=value1.replace(",","")
#     if int(value) > 50000:
#         print(i,"번째 상품 이름 :",name, "| 가격 :",value)



# //*[@id="wrapper"]/main/section/div[4]/section/ul/li[1]/div/div[2]/p[2]/span
# //*[@id="wrapper"]/main/section/div[4]/section/ul/li[2]/div/div[2]/p[2]/span
# //*[@id="wrapper"]/main/section/div[4]/section/ul/li[3]/div/div[2]/p[2]/span
#=====================================================================#
##########################[ 여행사이트 크롤링 ]#############################
# service=Service() #생략 귀찮으면 대소문과 구분 후 괄호 다 치면 됨.
# driver.get("https://www.booking.com/")
# print("부킹 페이지로 이동 완료")
# driver.implicitly_wait(10) #모든요소가 로딩될때까지 기다린다.
# time.sleep(5)#넉넉하게 5초 더 기다려준다.
# print("모든요소가 갱신됨.")
# driver.refresh()
# print("새로고침 완료") #첫방문 팝업창 제거용
# driver.implicitly_wait(10) #모든요소가 로딩될때까지 기다린다.
# print("모든요소가 재갱신됨.")
# time.sleep(2)
# search_button=WebDriverWait(driver,10).until( EC.element_to_be_clickable((By.XPATH, '//*[@id=":rh:"]')))
# print("장소선택창을 찾았습니다.")
# search_button.click() # 서울 버튼 클릭
# search_button=WebDriverWait(driver,10).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="autocomplete-result-0"]/div/div/div')))
# print("서울 버튼 찾았습니다.")
# search_button.click() # 서울 버튼 클릭
# time.sleep(2)
# search_button=WebDriverWait(driver,10).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[4]/td[6]')))
# print("2월21일 버튼 찾았습니다.")
# search_button.click() # 서울 버튼 클릭
# time.sleep(1)
# search_button=WebDriverWait(driver,10).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[4]/td[7]')))
# print("2월22일 버튼 찾았습니다.")
# search_button.click() # 서울 버튼 클릭
# time.sleep(2)
# search_button=WebDriverWait(driver,10).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="indexsearch"]/div[2]/div/form/div/div[4]/button')))
# print("검색 버튼 찾았습니다.")
# search_button.click() # 서울 버튼 클릭
# time.sleep(1)
# driver.implicitly_wait(10) #모든요소가 로딩될때까지 기다린다.
# time.sleep(2)
# print("검색된 모든요소가 갱신됨.")
# hotel_name=WebDriverWait(driver,15).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]')))
# print("이름을 찾았습니다.")
# print("호텔명 :",hotel_name.text)
# time.sleep(10)
# hotel_cost=WebDriverWait(driver,10).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/span')))
# print("가격을 찾았습니다.")
# print("가격 :",hotel_cost.text)


#===================================[ 구글 이미지 서치 ]======================================#

driver.get("https://www.google.com/imghp?hl=ko&tab=ri&authuser=0&ogbl")

search_input=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
print(search_input)
search_input.send_keys("토끼")
search_input.send_keys(Keys.ENTER)
for i in range(1,101):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    print(f"스크롤{i}회")
    driver.implicitly_wait(5)
    print(f"{i}회 요소불러오기 완료")
    time.sleep(2)
    driver.save_screenshot(f"text_toki/toki{i}.png")