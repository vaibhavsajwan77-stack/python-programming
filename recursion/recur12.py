
def binary_search(a,key,low,high):
    if low>high:
        return(-1)
    mid=(low+high)//2
    if a[mid]==key:
        return(mid)
    if a[mid]>key:
        binary_search(a,low,mid,high)
a=[]
size=int(input("enter the size of list"))
for i in range(size):
    value=int(input("enter the value"))
    a.append(value)
a.sort()
key=int(input("enter value to search"))
x=binary_search(a,key,0,size-1)
if x==-1:
    print("number is not found")
else:
    print("number is found at",x+1)
