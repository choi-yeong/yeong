from bs4 import BeautifulSoup
import requests
html_url="https://www.metroseoul.co.kr/article/20250116500487"
res=requests.get(html_url)
soup=BeautifulSoup(res.text, "html.parser")
#print(soup)
### 제목 끌어오기 ###
title=soup.select("h1.detail-title")
print("제목 ㅣ",title[0].text.strip())
### 발행일 끌어오기 ###
date = soup.select("div > span.byline-set01")
print("발행", date[1].text.strip())
### 내용 끌어오기 ###
content=soup.select("div.row > div.col-12 p")
text=[i.text.strip() for i in content]
for i in text:
    print(i)