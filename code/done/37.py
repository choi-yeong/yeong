# 모듈 불러오기
import calculator

# 모듈의 함수 사용
print(calculator.add(5,7))
print(calculator.sub(5,9))
# 모듈의 변수 사용.
print(calculator.PI)
# 모듈의 클래스 사용.
calc1=calculator.Calculator()
print(calc1.multiply(4,3))

#퀴즈 확인
print()
print(calculator.ln)
print(calculator.divide(4,0))
print(calculator.divide(4,2))
squre=calculator.Calculator()
print(squre.square(5))

"""
"""
# 모듈 불러오기 여러가지 방법
# 1. 별칭 붙이기 ailas
"""
import calc as a   # calc라는 모듈을 a라는 별칭으로 사용하겠다.
print(a.add(5,2))
print(calc.add(5,2))  #둘은 같은 기능이다.
# 모듈명이 너무 길때 주로 사용한다.
"""
# 2. 부분 불러오기
"""
from calc imort *  # calc 라는 모듈을 전부 불러오겠다.
from calc imort add as a   #calc 라는 모듈의 add 시퀀스 기능을 a라는 별칭으로 불러 사용하겠다.

print(add(5,2))
"""