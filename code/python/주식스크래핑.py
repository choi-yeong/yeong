from bs4 import BeautifulSoup
import requests

###S&P500 증권 따오기###
res=requests.get("https://finance.naver.com/world/sise.naver?symbol=SPI@SPX")
soup=BeautifulSoup(res.text, "html.parser")
##이름##
name = soup.select_one("div.section_world > div.group_h > div.h_area > h2")
print(name.text)
##시가##
cost= soup.select_one("p.no_today em.no_up")
print(cost.text)

##전일##
bef_cost=soup.select_one("table.no_info>tbody>tr>td")
print(bef_cost.text)

##표##
table=soup.select("#dayTable")
li=[i.text.strip() for i in table]
print(li[0])

## 차라리 이미지를 가져오자.... ##