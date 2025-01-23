#실습. 타자연습게임
import random, time

words=["world","word","mountain","flower","over","power","game","sunlight","knight"]

def game():
    print("영어 타자 연습 게임")
    print("게임 종료를 원하시면 exit를 입력하세요.")
    
    total_words=0 # 맞춘 단어 갯수
    start_time=time.time() #게임 시작 시간
    while 1:
        word=random.choice(words)
        print("단어 :",word)
        while 1:
            enter=input("입력 : ")
            if enter=="exit": # 게임 종료
                end_time=time.time()
                total_time=end_time-start_time
                print("\n 게임 종료")
                print("총 입력 단어한 단어 :",total_words)
                print("총 걸린 시간 :",total_time)
                print("단어당 평균 입력시간 :", total_time/total_words)
                return 0
            if enter==word : # 단어 정답
                print("통과!")
                total_words +=1
                break
            else :
                print("땡! 다시 입력하세요!")


game()