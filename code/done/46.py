'''예외 처리 (한개씩)
try:
    x=int(input("숫자를 입력하세요."))
    result=10/x
except ZeroDivisionError as e:
    print("예외 메세지 :",e)
except ValueError as e:
    print("예외 메세지 :",e)
else : 
    print(result,"입니다.")
finally:
    print("예외처리 종료.")
'''

'''예외처리 (두개이상  에러 동시)
try:
    x=int(input("숫자를 입력하세요."))
    result=10/x
except (ZeroDivisionError,ValueError) as e: # 괄호로 묶어서 여러 에러 동시처리 가능
    print("예외 메세지 :",e)
else : 
    print(result,"입니다.")
finally:
    print("예외처리 종료.")'''

#''' raise 명시적으로 예외를 발생
def divide(a,b):
    if b==0:
        #ZeroDivisionError 발생
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a/b

try:
    result = divide(10,0)
except ZeroDivisionError as e:
    print("예외 발생:", e)