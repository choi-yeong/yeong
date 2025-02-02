#로또 당첨번호 확인 앱
#로또 복권 사이트 웹 스크래핑 하세요
#회차를 입력하면 당첨번호가 나오게 프로그래밍하세요

#601회~1155까지의 당첨기록
url="https://dhlottery.co.kr/gameResult.do?method=allWinPrint&gubun=byWin&nowPage=&drwNoStart=601&drwNoEnd=1155"

from bs4 import BeautifulSoup
import requests

res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
def LoTTo():
    numbers=[]
    # data=int(input("검색할 회차는?"))
    data=entry.get()  #엔트리에 입력한 값을 불러옴.
    if data.isdigit():
        number=1156-int(data)  # 입력한 회차의 html경로가 반대로 되어있어서 역계산해줌.
        if int(data)<601:
            messagebox.showwarning("죄송합니다.","600회 미만의 당첨결과를 준비하지 못 했습니다.")
    else :
        messagebox.showwarning("오류","회차를 정수의 숫자로 입력하세요!")
    if not soup.select_one(f"body > div.popup_wrap_common.popup_print_winnum_645 > table > tbody > tr:nth-child({number}) > td:nth-child(1)"):
        print(f"{data}회차의 정보는 없습니다. 죄송합니다.")
    else :
        title=soup.select_one(f"body > div.popup_wrap_common.popup_print_winnum_645 > table > tbody > tr:nth-child({number}) > td:nth-child(1)")
        print("회차 :",title.text.strip())
        luckyball=soup.select(f"body > div.popup_wrap_common.popup_print_winnum_645 > table > tbody > tr:nth-child({number}) > td:nth-child(2) > span")
        for i in luckyball:
            numbers.append(i.text.strip())
        print("당첨번호 :",numbers)
        bonusball=soup.select_one(f"body > div.popup_wrap_common.popup_print_winnum_645 > table > tbody > tr:nth-child({number}) > td:nth-child(3)")
        print("보너스번호 :",bonusball.text.strip())
        sign.config(text=f"당첨번호 : {numbers}\n\n보너스번호 : {bonusball.text.strip()}",anchor='nw',justify="left")
        entry.delete(0,END) #엔트리에 있는 문자열 삭제

# 여기까지 일단 로또 당첨번호를 가져오는 함수를 구축함.####
# 이제부터 창을 띄워볼 것임.
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("로또 당첨 확인")
sign=Label(root,width=40, height=5, text="당첨 번호는 여기 표시 됩니다.",background="skyblue") # 당첨번호를 표시하는 텍스트 공간
sign.pack(side="bottom")
label = Label(root,text="당첨 회차 입력")
label.pack(side="top", anchor='w')
entry=Entry(root,width=15,background="skyblue") #entry : 한줄 입력
entry.pack(side="top", anchor="w")
check=Button(root,command=LoTTo, text="당첨 번호 확인") #버튼 공간
check.pack(side="right")

root.mainloop()