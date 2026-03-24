def binary_search(a,size,key):
    i=0
    j=size-1
    s=0 
    while i<=j and s==0:
        mid=(i+j)//2
        if a[mid]==key:
            s=1
            pos=mid+1
        if a[mid]>key:
            j=mid-1
        if a[mid]<key:
            i=mid+1
    if s==1:
        print("number is found at",pos)
    else:
        print("not found")
a=[3,5,7,9,12,15,16]
key=int(input("entervalue for search:"))
size=len(a)
binary_search(a,size,key)
