from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By #By 사용하기 위한 모듈
from selenium.webdriver.common.keys import Keys #Keys 사용하기 위한 모듈 (엔터, 리턴 등)
from selenium.webdriver.support.ui import WebDriverWait #webdriverwait를 사용하0기 위한 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options #옵션
import requests, time, os
#옵션객체 생성
service=Service() #생략 귀찮으면 대소문과 구분 후 괄호 다 치면 됨.
chrome_option = Options()
#옵션추가
# chrome_option.add_argument("--start-maximized") #최대크기로 열기
# chrome_option.add_argument("--headless") #GUI창 안열고 백그라운드 실행(리소스절약)
driver = webdriver.Chrome(service=Service(), options=chrome_option)



# # 실습3. 여행사이트
# url="https://www.agoda.com/ko-kr/?ds=V4Kkl7A1dZk6NXk3"
# driver.get(url)
# time.sleep(2)
# departure = driver.find_element(By.ID, "textInput").send_keys("도쿄")
# search= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="destination_suggestion_card"]')))
# search.click()

# # 마지막으로 열린 탭으로 전환
# driver.switch_to.window(driver.window_handles[-1])

# 실습4. 이미지 크롤링하기 ################################
driver.get("https://www.google.com/imghp")
time.sleep(2)
search = driver.find_element(By.ID, 'APjFqb')
search.send_keys("토끼")
search.send_keys(Keys.ENTER)
print("토끼 검색 완료.")
time.sleep(2)

# 무한 스크롤
for i in range(1,4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(i,"회 스크롤.")
    time.sleep(2)

images = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")
# images = WebDriverWait(driver,10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"img.YQ4gaf"))
#     )
os.makedirs("images", exist_ok=True) # 폴더 신규 생성, 존재시 무시한다.
code=1
for image in images :
    # print(image.get_attribute("src"))
    src = image.get_attribute("src")
    if "FAVICON" not in src and "https://" in src:
        print(src)
        res = requests.get(src)
        with open(f"images/image_{code}.png", 'wb') as file:
            file.write(res.content)
            code +=1

print("서치 끝")