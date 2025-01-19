from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By #By 사용하기 위한 모듈
from selenium.webdriver.common.keys import Keys #Keys 사용하기 위한 모듈 (엔터, 리턴 등)
from selenium.webdriver.support.ui import WebDriverWait #webdriverwait를 사용하0기 위한 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options #옵션
import time, random
#옵션객체 생성
chrome_option = Options()
#옵션추가
# chrome_option.add_argument("--start-maximized") #최대크기로 열기
# chrome_option.add_argument("--headless") #GUI창 안열고 백그라운드 실행(리소스절약)

service=Service() #냅두시오 
driver = webdriver.Chrome(service=service, options=chrome_option)

#-----------------------------------------위는 import 구문이므로 주석처리 안해도 됨.--------------------------------------------
# driver = webdriver.Chrome()
# driver.get("https://naver.com")

# # input("대기") # 필요없는 구문이지만 크롬이 열리는걸 눈으로 보기 위해 일부러 넣음.
#-----------------------------------------------------------------------------------------------------------------------------

# # service=Service(ChromeDriverManager().install()) # 인스톨 한번 하면 이 구문이 필요없어짐.
# driver=webdriver.Chrome#(service=service) #인스톨 한번하면 이 구문이 필요없어짐.

# driver.get("https://www.google.com")

# input("")
# 여기까지 웹 드라이버 설정 방법을 배운 것!!!
#-----------------------------------------------------------------------------------------------------------------------------


# driver.get("https://google.com")
# # print(driver.title) # 윈도우 제목 불러오기
# # print(driver.current_url) # 윈도우 주소 불러오기
# # driver.maximize_window() # 화면 전체화면
# # time.sleep(2)
# # driver.get("https://www.wikipedia.org")
# search_input=driver.find_element(By.NAME, "q")
# # search_input=driver.find_element(By.ID, "input") #위 구문과 같은 역할이다.
# # print(search_input)
# # time.sleep(2)
# # search_input.send_keys("s")
# # time.sleep(random.uniform(0.2,1.3))
# # search_input.send_keys("e")
# # time.sleep(random.uniform(0.2,1.3))
# # search_input.send_keys("l")
# # time.sleep(random.uniform(0.2,1.3))
# # search_input.send_keys("en")
# # time.sleep(random.uniform(0.2,1.3))
# # search_input.send_keys("i")
# # time.sleep(random.uniform(0.2,1.3))
# # search_input.send_keys("um")
# # time.sleep(random.uniform(0.2,1.3))  # 로봇감지를 피하려고 별짓을 다해봤지만 구글에서 자꾸 감지해냄.
# # search_input.send_keys(Keys.ENTER)
# # time.sleep(4)
# # input("")

# driver.get("https://naver.com")
# time.sleep(2)
# driver.execute_script("alert('hello, selenium')")
# time.sleep(2)
# alert=driver.switch_to.alert
# print(alert.text)
# time.sleep(2)
# alert.accept() # 메시지 확인버튼 클릭
# # 엘레멘트 찾기
# search_input=driver.find_element(By.XPATH, '//*[@id="query"]') #XPATH값은 검사에서 오른쪽마우스클릭했음.
# search_input.send_keys("selenium")
# search_input.send_keys(Keys.ENTER)

# input("")


## 무한 스크롤 ###--------------------------------------------------
# driver.get("https://www.google.com/imghp?hl=ko&authuser=0&ogbl")
# search_input=driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# driver.maximize_window() # 화면 전체화면
# search_input.send_keys("토끼")
# search_input.send_keys(Keys.ENTER)
# driver.implicitly_wait(10)

# for i in range(3):
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#     #driver.implicitly_wait(5)
#     time.sleep(2)

# input("")
##====================================================================================

#대기#==============================================================================
# driver.get("https://google.com")
# driver.implicitly_wait(10)

# EC 메서드 :대기조건
# EC.title_is(문자열) : 현재페이지 제목이 지정된 '문자열'과 일치할 때 까지 대기
# EC.title_contains(문자열) : 현재페이지 제목에 '문자열'이 포함될 때 까지 대기
# EC.presence_of_element_located((By.ID,"아이디값")) # DOM이 존재할 때 (화면에 표시 안 되어도 됨.)
# EC.visibility_of_element_located(By.CSS_SELECTOR, "선택자이름") # DOM이 존재할 때 (화면에 표시되는 애들만)
# EC.presence_of_all_elements_located((By.CSS_SELECTOR,"선택자이름")) # DOM에 모든 요소가 존재할 때
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"선택자이름")) #화면에 표시되는 DOM의 모든 요소가 존재할 때
# EC.element_to_be_clickable((By.CSS_SELECTOR,"선택자이름")) # 요소가 화면에 표시되고 클릭이 가능할 때
# EC.element_to_be_selected((By.CSS_SELECTOR,"선택자이름")) # 요소가 선택된 상태가 될 때

# 검색입력필드 대기
# search_input= WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME,'q'))
#     )

# # search_input.send_keys('python')
# # search_input.send_keys(Keys.ENTER)

# email_text=driver.find_element(By.XPATH,'//*[@id="gb"]/div/div[1]/div/div[1]/a')
# href=email_text.get_attribute("href")
# print(href)

###################### 스크린샷 ###################################
driver.get("https://www.nate.com/")
time.sleep(2)
search_input=driver.find_element(By.XPATH,'//*[@id="q"]')
print(search_input)
#search_input.send_keys("파이썬")
#search_input.send_keys(Keys.ENTER)
#time.sleep(2)
#driver.save_screenshot("python.png")

#input("")
#--------------------------------------------------------------------
# --start-maximized : 브라우저를 최대화된 상태로 실행
# --window-size=width,height : 브라우저 크기를 지정 (예: --window-size=1920,1080)
# --headless : 브라우저 GUI 없이 백그라운드에서 실행 (리소스 절약)
# --disable-notifications : 알림 창 비활성화
# --incognito : 시크릿 모드 실행
# --disable-gpu : GPU 렌더링 비활성화 (Linux에서 Headless 모드에서 사용 권장)
# --no-sandbox : 샌드박스 모드 비활성화 (권한 문제 해결에 유용)
# --disable-extensions : 확장 프로그램 비활성화


