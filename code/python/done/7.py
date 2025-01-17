#딕셔너리(dictionary)
#빈 딕셔너리 생성
dict1={}
dict2=dict()
print(dict1)
print(dict2)

#딕셔너리 생성
dict1={
    "name":"홍길동",
    "age":"20",
    "city":"Seoul",
    "hobby":["런닝","등산","헬스"]
}
print(dict1)

dict2=dict(name="홍길동",age="21")
print(dict2)

#값 접근하기
print(dict1["name"])
print(dict1["hobby"][2])

#값 수정하기
dict1["age"]=30
print(dict1)

#요소 추가
dict1["birthday"]="19900101"
print(dict1)

#키 삭제
del dict1["birthday"]
print(dict1)

#딕셔너리 메서드
fluits={"apple":"사과","banana":"바나나"}
print(fluits.get("apple"))
#존재하지 않는 키 반환
print(fluits.get("peach","복숭아")) #peach라는 키가 없으면 none표시를 "복숭아"라고 표현해줘

#여러요소 추가
fluits.update({"grapes":"포도","melon":"멜론"})
print(fluits)
print(fluits.keys()) #키들만 출력
print(fluits.values()) #값들만 출력
print(fluits.items()) #키와 값을 출력

fluits.clear()
print(fluits)

"""
내장함수
sum():숫자 시퀀스의 모든 요소를 더해 합계를 반환
 시퀀스 : 문자열, 리스트, 튜플, reange() 등
max() : 최대값 반환
min() : 최소값 반환
len() : 길이 반환
zip() : 여러시퀀스를 병렬로 묶음.
 길이가 짧은 시퀀스에 맞춰서 반환
"""
names=["Alice","Bob","Charlie"]
scores=[85,90,95,100]
print(list(zip(names,scores))) #list 리스트로 출력
print(dict(zip(names,scores))) #dict 딕셔너리로 출력
