#리스트 내포 : 리스트 안에 for문 사용
"""
표현식 : 각 요소에 대해 계산되어 리스트에 추가될 값
요소 : 시퀀스(리스트,튜플,문자열 등)에서 가져온 각 요소를 나타낸 변수
if조건:필터링을 위해 사용되며 조건이 True인 요소만 포함
"""
numbers=[1,2,3,4,5]
squares=[n**2 for n in numbers]
print(squares)

squares2=[n**2 for n in range(1,6)]
print(squares2)

#조건문과 함꼐 사용
even_squares=[x**2 for x in range(1,6) if x %2==0]
print(even_squares)
