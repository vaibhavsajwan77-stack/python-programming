def num(n):
    if n<=0:
        return
    print(n,end=",")
    num(n-1)
def num1(n):
    print(n,end=",")
    num(n-1)
num1(10)
