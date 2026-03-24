def power(x,y):
    if y==0:
        return(1)
    else:
        return(x*power(x,y-1))

x=int(input("enter the value of base"))
y=int(input("enter the value of power"))
z=power(x,y)
print("answer is=",z)
