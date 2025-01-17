from bs4 import BeautifulSoup
import requests

res=requests.get("https://finance.naver.com/marketindex/")
soup=BeautifulSoup(res.text, "html.parser")
###달러지표 끌고오기###
##이름##
usa=soup.select_one("div.data > ul.data_lst > li > a > h3.h_lst")
##환율##
dalor=soup.select_one("div.data > ul.data_lst > li > a > div.head_info > span.value")
print(usa.text,"의 가치:", dalor.text)

###엔화지표 끌고오기###
##이름##
jap=soup.select_one("a.jpy > h3.h_lst")
##환율##
yen=soup.select_one("a.jpy > div.head_info > span.value")
print(jap.text,"의 가치:", yen.text)

###유럽달러 끌고오기###
##이름##
eu=soup.select_one("a.eur > h3.h_lst")
##환율##
eur=soup.select_one("a.eur > div.head_info > span.value")
print(eu.text,"의 가치:", eur.text)

###중국원화 끌고오기###
##이름##
cino=soup.select_one("a.cny > h3.h_lst")
##환율##
cny=soup.select_one("a.cny > div.head_info > span.value")
print(cino.text,"의 가치:", cny.text)
