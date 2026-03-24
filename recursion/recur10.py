def gcd(p,q):
    if q==0:
        return p
    else:
        return(gcd(q,p/q))
p=int(input("enter first number"))
q=int(input("enter second nuber"))
z=gcd(p,q)
print("gcd of given number is =",z)
