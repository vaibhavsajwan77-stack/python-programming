l=[]
r=int(input("enter no of row"))
c=int(input("enter hte no of the coloumn"))
for i in range(r):
    row=[]
    for j in range(c):
        val=int(input("enter the value"))
        row.append(val)
    l.append(row)
print("2D list is",l)
print("\t[")
for i in range(r):
    print("\t[",end="")
    for j in range(c):
        print(l[i][j],end="\t")
    print("]")
print("\t]")
s=0
key=int(input("enter value for search"))
for i in range(r):
    if s==r*c:
        print("not founded")
    if l[i][j]==key:
        print("position of given value is=",i+1,"row",j+1,"col")
    else:
        s=s+1
