l=[]
r=int(input("enter the row"))
c=int(input("enter the coloumn"))
for i in range(r):
    row=[]
    for j in range(c):
        val=int(input("enterhte value"))
        row.append(val)
    l.append(row)
print("2D list is ",l)
