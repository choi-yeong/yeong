import math, random
print(math.pi)
print(math.sqrt(25)) #제곱근
print(math.factorial(4))

print(math.ceil(3.14))#올림
print(math.floor(3.14))#내림
print(round(3.14)) # 반올림 # math모듈에 속한 함수가 아닌 파이썬 내장함수

rand_int = random.randint(1,10) # 1<= x <=10
print("rand_int:",rand_int)

rand_float=random.uniform(1.5,6.5) # 1.5<= x <=6.5
print("uniform:",rand_float)

rand_between=random.random()
print("random:",rand_between) #0 <= x <1

rand_range=random.randrange(10,1000) # 10 <= x < b 정수
print("randrange:", rand_range)


nums=[1,2,3,4,5,6,7,"가","나","다"]
rand_choice=random.choice(nums)
print("choice:",rand_choice)

# sample(population, k)
# population : 모집단 (리스트, 튜플, 문자열, range())
# k : 선택할 요소 개수
fruits=["사과","오렌지","바나나","포도","귤"]
rand_sample=random.sample(fruits, 4)
print("sample:", rand_sample)