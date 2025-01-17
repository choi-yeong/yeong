
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
value = matrix[1][2] #2번째 행의 3번째 열
print(value) #6

#요소(열)추가
matrix[1]=matrix[1]+[100]
print(matrix) #[[1, 2, 3], [4, 5, 6, 100], [7, 8, 9]]
#행추가
matrix=matrix+[[10,11,12]]
print(matrix) #[[1, 2, 3], [4, 5, 6, 100], [7, 8, 9], [10, 11, 12]] 
#요소(열) 수정
matrix[0][0]=11
print(matrix) #[[11, 2, 3], [4, 5, 6, 100], [7, 8, 9], [10, 11, 12]] 
#행삭제
del matrix[1]
print(matrix) #[[11, 2, 3], [7, 8, 9], [10, 11, 12]]
#행의 개수
rows=len(matrix)
#열의 갯수 (첫번째 행의 길이로 판단)
cols=len(matrix[0])
print(f"행:{rows}, 열 :{cols}")


#이차원 메서드
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#요소추가
matrix[0].append(10)
print(matrix)
#행추가
matrix[0].append([10,11,12])
print(matrix)
#요소삽입
matrix[1].insert(1,100)
print(matrix)
#행삽입
matrix.insert(2,["안녕","반가워","어서와"])
print(matrix)