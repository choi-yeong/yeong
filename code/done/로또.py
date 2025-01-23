import random

rand_sample=random.sample(range(1,46), 6)
print("sample:", rand_sample)
print("번호 정렬",sorted(rand_sample))

# 1. 빈 set만들기
lotto_nums=set()
# 2. 6개의 숫자 뽑기
while len(lotto_nums)<6:
    #난수를 set에 추가
    lotto_nums.add(random.randint(1,45))
# 3. 오름차순 정렬
sorted_lotto_nums= sorted(lotto_nums)
print("솔루션2:",sorted_lotto_nums)