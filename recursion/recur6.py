def fibo(m):
    if m==1:
        return(0)
    if m==2:
        return(1)
    recursion(fibo(n-1)+fibo(n-2))
n=int(input("enter limit value"))
for i in range(1,n+1):
    print(fibo(1))
