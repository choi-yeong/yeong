from bs4 import BeautifulSoup
import requests

def stock(code):
    html_url=f"https://finance.naver.com/item/main.naver?code={code}"
    res=requests.get(html_url)
    soup=BeautifulSoup(res.text, "html.parser")
    print()

    company = soup.select_one("div.wrap_company > h2 > a")
    print("회사명 :",company.text.strip())

    price=soup.select_one("div.rate_info > div.today > p.no_today > em.no_up > .blind")
    print("종  가 :",price.text)

    prev=soup.select("p.no_exday > em.no_up > span.blind")
    print("전일대비 :", prev[0].text,"원")

    prev_per=soup.select("p.no_exday > em.no_up > span.blind")
    print("전일대비 :", prev_per[1].text,"%")
# 000680 : LS네트웍스
# 010120 : LS전선
stock("000680")
# stock("010120")
# stock("005930")