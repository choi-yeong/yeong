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
import numpy as np
service=Service() #생략 귀찮으면 대소문과 구분 후 괄호 다 치면 됨.
driver = webdriver.Chrome(service=Service())
# array_1d=np.array([1,2,3,4,5])
# print(array_1d)

# array_2d=np.array([[1,2,3],[4,5,6]])
# print(array_2d)

# array_3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(array_3d)

# print(array_2d.shape) #배열모양
# print(array_2d.ndim) #차원
# print(array_2d.dtype) # 원소의 자료형
# print(array_2d.itemsize) #요소의 크기
# print(array_2d.size) # 원소의 개수

# arr= np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# row=[0,2]
# col=[2,2]
# print(arr[row,col])

# arr=np.array([10,20,30,40,50])
# print(arr[arr>20]) #20이상인것들 프린트
# print(arr[arr%20==0]) #20으로 나눠떨어지는 것들 프린트

# arr[arr>20]=0 #20보다 큰걸 0으로 바꾸기
# print(arr)

# lists=[2,3,4]
# print(arr[lists])

# 배열 생성 #######################################
# zero = np.zeros((3,3)) # 3x3 행렬을 0의 요소를 넣어서 생성
# print(zero) 
# ones=np.ones((5,5)) #5x5 행렬을 1의 요소를 넣어서 생성
# print(ones)
# ranges = np.arange(1,20) # 1차원 행렬에 1~19 요소를 넣어서 생성
# print(ranges)
# linespaes = np.linspace(0,2, 10) # 0 에서 2 까지의 10가지의 요소를 균등하게 배분해서 생성
# print(linespaes) #[0.         0.22222222 0.44444444 0.66666667 0.88888889 1.11111111 1.33333333 1.55555556 1.77777778 2.        ]

# 1차원 배열을 2x3 배열로 변환 #########################
# array= np.array([1,2,3,4,5,6,7,8,9])
# reshaped = np.reshape(array, (3,3)) # 요소의 사이즈가 맞지 않으면 에러가 뜸.
# print(reshaped)
# resized= np.resize(array, (4,8)) # 요소가 부족하면 기존 요소를 반복시켜서 채움.
# print(resized)

# 연산 #########################################################
# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])
# print(a+b) # [ 6  8 10 12]
# print(a*b) # [ 5 12 21 32] # 개수가 다르면 오류
# c = np.array([1,4,9,16,25,36,49])
# print(np.sqrt(c))  # 제곱근
# print(np.exp(c))  # 지수함수
# print(np.log(c)) # 로그함수
# 삼각함수
# angles = np. array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
# print(angles)
# print(np.sin(angles))
# print(np.cos(angles))

# 합치기 ######################################################
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# #수평 합치기
# print(np.hstack((a,b)))
# #수직 합치기
# print(np.vstack((a,b)))
# #열기준 합치기
# print(np.column_stack((a,b)))
# # 분할하기
# a=np.array([[1,2,3],[4,5,6]])
# #수평분할
# print(np.hsplit(a,3))
# #수직분할
# print(np.vsplit(a,2))

# 야구 기록 데이터 정렬
url="https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
res=requests.get(url)
soup=BeautifulSoup(res.text, "html.parser")
# print(soup.text.strip())
tb=soup.select_one(f'#cphContents_cphContents_cphContents_udpRecord > table')
tb_data=[]
rows = tb.select('tr')
for row in rows:
    cols = row.select('td')
    if cols :
        tb_data.append([col.text.strip() for col in cols])
# 이건 리스트로 만드는 것
print(" 순위   |  팀명 |  승   |   패  |   무  |  승률 |")
for i in range(10):
    print(" ",tb_data[i][0],"\t|",tb_data[i][1],"\t|",tb_data[i][3],"\t|",tb_data[i][4],"\t|",tb_data[i][5],"\t|",tb_data[i][6],"|")
print()
# 이건 numpy로 만드는 것
table=np.array(tb_data)
print(" 순위   |  팀명 |  승   |   패  |   무  |  승률 |")
for i in range(10):
    print(" ",table[i,0],"\t|",table[i,1],"\t|",table[i,3],"\t|",table[i,4],"\t|",table[i,5],"\t|",table[i,6],"|")
