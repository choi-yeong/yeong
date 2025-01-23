"""JSON:JavaScript(언어) Object자료형과 유사하게 생긴 텍스트형식
JavaScript Object Notaion
-가독성이 뛰어남 (컴퓨터도, 사람도 해석하기 편함.)
-네트워크를 통해 다른 시스템간 소통할 때 자주 사용.
 - 용량이 가벼움.
 - JavaScript언어에서부터 파생되었으나 현재는 다른 프로그래밍언어에서도 지원.
(예시)
{"name":Sean","age":20,"skills":["JavaScript","Python"]}

"""
import json
python_dict={
    "name":"Lily",
    "age":20,
    "city":"Busan",
    "islogin":True
}

json_str=json.dumps(python_dict) # dumps() : 딕셔너리를 JSON 문자열로 변환
print(json_str)
# python_dict : 파이썬의 딕셔너리 객체
# json_str : JSON형식의 텍스트 데이터


json_obj = json.loads(json_str) #JSON 문자열을 Python 객체로 변환
print(json_obj)
print(json_obj["name"])

""" Third-part Module : 파이썬 표준 모듈이 아니라 외부 개발자가 만든 모듈
파이썬 표준 모듈이 아니라 외부 개발자나 개발 커뮤니티에서 만든 추가적인 모듈
- conda install 모듈명
- pip install 모듈명
서드파티모듈 사용 시 특정 작업을 쉽고 효율적으로 개발할 수 있게 된다.
"""