#requests

import requests, json
#requets 를 불러올 수 없을땐 인터프리터를 conda로 하거나, "pip install requests"를 하지 않은 것이다.

url="https://api.sampleapis.com/avatar/info"
res = requests.get(url)


print("상태코드 :",res.status_code)
if res.status_code == 200 : #서버가 정상적으로 get 되었을 때(200)
    data=res.json()
    print(data[0]["synopsis"])
    print(data[0]["yearsAired"]) #json 특정키 받아오기
    print(res.text) #json 본문내용 전부 받아오기
    print(res.url) #요청 url주소 가져오기
    