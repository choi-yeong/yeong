import random, time
words_list=["sunlight","cloud","exit"]



def typegame():
    word=random.choice(words_list)
    point=0
    print("단어 :",word)
    enter=input("입력 : ")
    if enter==word:
        print("통과! +1 포인트")
        point += 1
        typegame()
    else :
        return point


while 1:
    start_time=time.perf_counter()
    typegame()
    end_time=time.perf_counter()
    clock=start_time-end_time
    print("수고하셨습니다.")
    print("총 진행시간 :",clock)
    print("획득 포인트 :",typegame())  
    
        