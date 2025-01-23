#실습. 야구 데이터 해답편

import requests
import numpy as np
from bs4 import BeautifulSoup

url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

table=soup.select_one("table.tData") #tData클래스가 3개 있으나 select_one으로 가장 위 한개만 가져옴.
trs=table.select("tr")[1:]  #순위,팀 등 필요없는 내용을 잘라서 1부터 시작

lists=[]
for tr in trs :
    td = tr.select("td")
    td = [i.text.strip() for i in td] #[td]와 공백 지우기
    lists.append([td[0],td[1],td[3],td[4],td[5],td[6]])
    
print(lists)
array=np.array(lists)
fine_name ="kbo_2024rank.txt"
header="순위\t 팀 \t 승\t 패 \t 무 \t 승률"

with open(fine_name, 'w', encoding='utf-8') as file:
    file.write(header+"\n")
    for data in array:
        file.write("\t".join(data)+"\n")
# join():문자열리스트를 하나의 문자열로 결합할 때 사용한다.
# "\t".join(['순위', '팀명', '승', '패']) -> ['\t순위 \t팀명 \t승 \t패']

with open(fine_name, "r", encoding='utf-8') as file:
    print(file.read())