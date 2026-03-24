def search_delete(a,size,key):
    i=0
    j=size-1
    if i<=j:
        a.remove(key)
        print(a)
    else:
        print("number is not found")
        
a=[] 
size=int(input("enter size"))
for i in range(size):
    val=int(input("enter the value"))
    a.append(val)
key=int(input("enter value for delete"))
search_delete(a,size,key)
    
