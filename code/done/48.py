from bs4 import BeautifulSoup
import requests

# """여러줄 주석은 사실 문자열이었다;;;"""


# html_str="""
#<html>
#    <body>
#        <div id="content">
#            <ul class="industry">
#                <li>인공지능</li>
#                <li>빅데이터</li>
#                <li>스마트팩토리</li>
#            </ul>
#            <ul class="language">
#                <li>Python</li>
#                <li>C++</li>
#                <li>Javascript</li>
#            </ul>
#        </div>
#    </body>
# </html>
# """

# soup=BeautifulSoup(html_str,"html.parser")
# print(soup)
# lxml => 속도가 빠름. pip install lxml 설치 필요.
# html5lib => 속도 느림. pip install html5lib 설치 필요. html5규격을 엄격히 지킴.

# first_ul= soup.find('ul')
# print(first_ul)
# print(first_ul.text) # 태그 없이 텍스트만 출력

# all_ul=soup.find_all('ul') # all: 리스트형태로 반환
# print(all_ul[1].text)

# class_ul = soup.find('ul', attrs={'class':"language"})
# print(class_ul.text)

# class industry를 가져오는 selector
# ul.industry
# #content > .industry
# #content .industry
# #content:first-child

# first_ul = soup.select_one('ul.industry')
# print(first_ul.text)

# all_ul= soup.select('#content > ul')
# print(all_ul)

# 서울 시청 웹 크롤링
# html_url="https://www.seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# print(res.text)
# soup=BeautifulSoup(res.text, "html.parser")
# print(soup)
# all_nav = soup.select("nav > ul > li > a") # 명시적 표현임. 간단하게 "nav a"하면 자손찾음
# print(all_nav)
# for i in all_nav:
#     print(i.text)


# 실습. 국립중앙박물관 웹 스크래핑 (관람시간, 요금)
#html_url="https://www.museum.go.kr/site/main/home"
#res = requests.get(html_url)
# print(res.text)
#soup=BeautifulSoup(res.text, "html.parser")
# print(soup)
## 전체적으로 가져오는 방법
# infos=soup.select("ul.main-info-area > li")
# print(infos)
# for i in infos:
#     print(i.text)

# 관람시간 #
#times=soup.select(".info-time > ul > li")
# print(times)
#for i in times:
#    print("관람시간 :",i.text.strip())
# 관람료 #
#pay = soup.select(".info-admission > ul > li > strong")
#print("관람료 :",pay[0].text.strip())
#pay2 = soup.select(".info-admission > ul > li > span")
#print("관람료 :",pay2[0].text.strip())

### KBS 뉴스기사 스크래핑 ###
#html_url="https://news.kbs.co.kr/news/pc/view/view.do?ncd=8153501"
#res=requests.get(html_url)
#soup=BeautifulSoup(res.text, 'html.parser')
#print(soup)
## 제목 ##
#title=soup.select_one(".headline-title")
#print("제목 :",title.text.strip())
## 내용 ##
#contents=soup.select_one("#cont_newstext")
#print("내용 :",contents.text.strip())

#with open("news.txt", "w", encoding= "utf-8") as file:
#    file.write(title.text.strip() +"\n")
#    file.write(contents.text.strip())

### 명언 사이트 스래핑 ###
html_url="https://quotes.toscrape.com/page/2/"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")
quote=soup.select(".quote > span.text")
#print(quote)
#for i in quote:
#    print(i.text.strip())
text = [i.text.strip() for i in quote]
#print(text)

speaker=soup.select(".quote .author")
#print(speaker)
author=[i.text.strip() for i in speaker]
#print(author)

zip_quote=list(zip(text,author))

for text, speaker in zip_quote:
    print("시인 :",speaker)
    print("명언 : ", text)
    print()