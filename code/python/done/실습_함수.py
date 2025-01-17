#실습1
def muxNadd(a,b):
    if a==b:
        return a*b
    else :
        return a+b
    return 0
print(muxNadd(2,3))

#실습2
def cost(pay):
    if pay<20000:
        return pay
    else:
        return pay+2500
    return 0
print(f"상품 1 가격 : {cost(50000)}")
print(f"상품 2 가격 : {cost(5000)}")

#실습3
