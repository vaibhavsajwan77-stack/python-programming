def count(n):
    if n<10:
        return 1
    return(1+count(4//10))
n=int(input("enter any number"))
print(count(n))
