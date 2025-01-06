print("1,2번")
students={"Alice":85,"Bob":90,"charlie":95}
print(students)
print("3번")
students["David"]=80
print(students)
print("4번")
students["Alice"]=88
print(students)
print("5번")
del students["Bob"]
print(students)


#문제풀이
#1. 빈딕셔너리 생성
student_dict={}
#2. 학생 행성
student_dict.update({"Alice":85,"Bob":90,"Charlie":95})
print(student_dict)
#3. David 추가
student_dict.update({"David":80})
print(student_dict)
#4. Alice의 점수 수정
student_dict["Alice"]=88
print(student_dict)
#5. Bob 학생 삭제
student_dict.pop("Bob")
print(student_dict)
