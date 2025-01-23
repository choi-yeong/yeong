password=input("비밀번호를 입력하세요 :")
if password=="abc123":
    print("비밀번호가 맞습니다.")
else :
    print("비밀번호가 틀렸습니다.")
num=input("숫자를 입력하세요 :")
if int(num)%2==0:
    print("짝수입니다.")
else :
    print("짝수가 아닙니다.")

grade=input("점수를 입력하세요 : ")
score=int(grade)
#score=int(input("점수를 입력하세요. :")) 라고 하면 한 줄로 줄일 수 있었다.

if score>90:
    print("학점 : A")
elif score>80:
    print("학점 : B")
elif score>70:
    print("학점 : C")
elif score>60:
    print("학점 : D")
else :
    print("학점 : F")

"""
깊은카피vs얕은카피
불변성(immutable) 객체 : int, str, float, boolean, tuple
불변성(mutable0) 객체 : list, dict, set
불변성 객체를 b=a로 카피할 경우 얕은 복사가 일어나서 주소값을 복사해온다.
따라서 a값을 변경하면 주소값이 같은 b값도 주소가 바뀌어 b값이 같이 바뀐다.

import copy로 b=copy.deepcopy(a) 스크립트로 깊은 카피를 하여 값자체를 복사할 수 있다.
이때 서로 독립된 주소값을 가져서 a값을 변경하더라도 b값은 변하지 않는다. 

그럼 얕은복사vs깊은복사를 왜 알아야할까?
원본의 값은 바꾸더라도 복사한 객체의 값은 바뀌지 않아야할 경우가 있다.
"""