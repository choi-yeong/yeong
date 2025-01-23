rainbow=['red','orange','yellow','green','blue','indigo','purple']
print("1. 2번 인덱스값 출력")
print(rainbow[2])
print("2. 알파벳 순서로 정렬한 값 출력")
rainbow.sort()
print(rainbow)
print("3. 좋아하는 색 맨 마지막에 추가하기")
rainbow.append("magenta")
print(rainbow)
print("4. 3~6번째 값 삭제하기")
del rainbow[3:7]
print(rainbow)


#풀이
rainbow=['red','orange','yellow','green','blue','indigo','purple']
print("1. 2번 인덱스값 출력")
print(rainbow[2])

print("2. 알파벳 순서로 정렬한 값 출력")
#매소드방법
print("매소드sort 방법")
metho_rainbow=rainbow.copy()
metho_rainbow.sort()
print(metho_rainbow)
#함수방법
print("함수sorted방법")
func_rainbow=sorted(rainbow)
print(func_rainbow)

print("3. 좋아하는 색 맨 마지막에 추가하기")
rainbow.append("magenta")
print(rainbow)

print("4. 3~6번째 값 삭제하기")
#새로 함수를 만들어버리는 방법
print("리스트 요소를 새로 구성해서 함수만드는 방법")
deleted_rainbow=[rainbow[0],rainbow[1],rainbow[2],rainbow[7]]
print(deleted_rainbow)
#Del로 지우는 방법
print("Del로 지워버리는 방법")
del rainbow[3:7]
print(rainbow)