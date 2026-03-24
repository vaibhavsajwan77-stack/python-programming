if prime(n,i):
    if i==1:
        return 1
    if i==0:
        return 0
        return(prime(n,n-1))
n=int(input("enter any number"))
z=prime(n,n-1)
if z==1:
    print("given number is prime number")
if z==0:
    print("given bumber is prime number")
    
