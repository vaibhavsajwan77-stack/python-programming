def linear_search(a,size,key):
    a.sort()
    flag=0
    for i in range(size):
        if a[i]==key:
            flag=1
            pos=i+1
            break
    if flag==1:
        print("position of given number=",pos)
    else:
        print("given value is not found")
a=[]
size=int(input("enter size of list"))
for i in range(size):
    value=int(input("enter the value"))
    a.append(value)
key=int(input("enter the value for search"))
linear_search(a,size,key)

