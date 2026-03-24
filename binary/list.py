l=[]
r=int(input("enter number of row"))
c=int(input("enter number of the cloumn"))
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
