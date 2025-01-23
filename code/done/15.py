def sos(i):
    print(f"{i}번째 도움요청")
    
    if i ==1:
        return ""
    else : return sos(i-1)

sos(10)

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(10))

#피보나치 수열 만들기
def nacci(p):
    if p==0 :
        return 0
    elif p==1 :
        return 1
    else :
        return nacci(p-1)+nacci(p-2)
    
print(nacci(7))