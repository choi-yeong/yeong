# 이중 for문
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#요소의 합계
total_sum=0
for row in matrix :
    for elem in row:
        total_sum += elem
print(f"전체의 합:{total_sum}")

#짝수만 출력
matrix2=[
    [12,32,35],
    [47,55,46],
    [77,88,29]
]

for row in matrix2 :
    for elem in row:
        if elem%2==0:
            print(elem,end=" ")