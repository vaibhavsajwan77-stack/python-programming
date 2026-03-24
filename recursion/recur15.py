def search_insert(a,size,key):
    a.sort()
    a.append(None)
    i=size-1
    while i>=0 and a[i]>key:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=key
    print("after increation name list is=",a)
a=[]
size=int(input("enter size"))
for i in range(size):
    val=int(input("enter the vlaue"))
    a.append(val)
key=int(input("enter value for insert"))
search_insert(a,size,key)
