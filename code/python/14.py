#냐장 함수
#bs(정수)절대값을 구하는 내장함수
print(abs(-99))
print(abs(0))
print(abs(10))

#pow(x,y):x^y를 구하는 내장함수
print(pow(10,2))
print(pow(2,10))
print(pow(3,4))

#실습4. 함수만들기
#1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 저의해라

def mepow(i):
    count=0
    print(f"{i}의 배수의 개수:",end="")
    for i in range(i,31,i):
        print(i,end=" ")
        count=count+1
    print()
    print(f"{i}의 배수의 개수 :",count)

i=int(input("구할 배수의 개수?"))
mepow(i)

#max(), min() 내장함수 구현
def memax(a,b):
    if a>b:
        print(a)
    elif a<b:
        print(b)
    else :
        print("같다.")
#min()의 경우 크기비교부등호(<,>)를 반대로 작성.
memax(5,10)
max(5,10)


# 문제풀이 meMax 리스트로 풀기 (출력값으로 배수와 배수갯수 동시 출력)
def count(num):
    lists=[i for i in range(1,31) if i % num==0]
    counts=len(lists)

    return (lists, counts)

n = 3 #구할 배수

print(count(n))
my_lists, my_counts = count(n)
print(my_lists)
print(my_counts)