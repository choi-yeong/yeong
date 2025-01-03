# 한 줄 주석 (ctrl+/)

'''
여기는
여러줄
주석입니다.
'''

"""
쌍따옴표 세 개도
여러줄
주석입니다.
"""

print("Hello World")
print("Hello","World")#자동으로 두 단어 사이에 공백이 생김.
print("Hello","World",sep="") #seperate를 없앰.
print("010","2134","4567",sep="-") #seperate에 다른 단어를 넣음.

print("Hello","Python",1,2,sep="_") #자료형이 달라도 됨(파이썬만)
print() #괄호 안에 아무것도 없으면 줄바꿈 역할이 됨.
print(11111) #문자열의 경우 "1111"을 넣어야하지만 숫자라서 그냥 1111넣음.

print("안녕하세요, ", end="") #문장끝의 후미어를 지정할수있다.
print("코딩온입니다.")
print("안녕하세요", end=", ") #문장끝의 후미어를 지정할수있다.
print("코딩온입니다.")

ive='I AM'
print(ive)
ive='장원영'
print(ive)

print(f"제가 좋아하는 가수는 {ive}입니다.") #f문자열포매팅, python 3.6버전부터 가능
print("제가 좋아하는 가수는 ", ive, "입니다.",sep="") #f문자열포매팅이 없던 시절 코딩법. sep를 사용하지 않으면 띄어쓰기가 달라진다.

