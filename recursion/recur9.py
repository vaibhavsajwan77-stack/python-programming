ndef prime(n,i):
    if i==1:
        return 1
    if n>i==0:
        return 0
    return(prime(n,n-1))
n=int(input("enter any number"))
z=prime(n,n-1)
if z==1:
    print("all are prime")
if z==0:
    print("number is not prime")
        
