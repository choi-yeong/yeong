# 파일 입출력
"""파일 쓰기
with open("test.txt","w",encoding="UTF-8") as file:
    file.write("안녕하세요!\n")
    file.write("파이썬 파일 쓰기 예제입니다!")
"""
"""내용 추가
with open("test.txt","a",encoding="utf-8") as file:
    file.write("내용추가\n")
    file.write("1111")
"""
""" writelines()
lines=["첫번째 내용\n","두번째 내용\n","세번째 내용", "네번째애용"]

with open("test2.txt","w",encoding="utf-8") as file:
    file.writelines(lines)
"""
""" 사용자로부터 입력받은 내용을 파일로 만들기
with open("user.txt","w",encoding="utf-8") as file:
    while True:
        line=input("파일에 넣을 문자열 입력(종료하려면 '종료'입력)")
        if line=="종료":
            print("\n입력을 종료합니다.")
            break
        file.write(line+"\n")
"""
"""파일 읽기
with open("user.txt","r",encoding="utf-8") as file:
    print(file.read() ) #파일 전체 내용을 가져온다.

with open("user.txt","r",encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline()) #파일을 한줄씩 가져온다.

with open("user.txt","r",encoding="utf-8") as file:
    print(file.readlines()) #파일 내용을 한줄마다 리스트로 가져온다.
"""
"""한줄 씩 전체 읽기
with open("user.txt","r",encoding="utf-8") as file:
    line=file.readline()
    while line:
        print(line.strip()) #.strip() : 양쪽 공백 제거
        print(line.rstrip()) #.strip() : 우측 공백 제거
        print(line.lstrip()) #.strip() : 좌측 공백 제거
        line = file.readline()
"""

''' enumerate() 리스트를 튜플형태로 반환, 반환값이 2개
with open("user.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    #["아리랑","아리랑","아라리요"...]
    for idex,value in enumerate(lines):
        #(0, "아리랑\n"), (1,"아리랑\n"), (2,"아라리요\n")...
        print(f"{idex}, {value.strip()}")
'''

# 바이너리 파일
''' 
with open("owl.png","rb") as file:
    #data = file.read()
    #print(f"{len(data)} byte")
    header=file.read(10)
    print(f"{header}")
'''
'''바이너리파일 읽기 예제
def files(file_path):
    with open(file_path, "rb") as file:
        header=file.read(4)
        print(header)
        if header==b'\x89PNG':  #b: 바이너리 파일 형식으로 읽음.
            return "png"
        if header[:2]==b'\xff\xd8':
            return "jpg"

# files("owl.jpg")
# files("owl.png")

print(files("owl.png"))
print(files("owl.jpg"))
'''

''' 바이너리 파일 쓰기 (복사)
with open("owl.png","rb") as file:
    data = file.read() #데이터 복제
with open("owl_copy.png","wb") as file:
    file.write(data) #복제한 데이터 쓰기
'''

