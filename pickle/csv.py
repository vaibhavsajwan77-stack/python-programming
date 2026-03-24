import csv
def search_ID():
    ID=int(input("enter the ID"))
    x=0
    f=open("employees.csv","r")
    f_new=csv.reader(f)
    next(f_new)
    for i in f_new():
        if i[0]==ID:
            print(i)
            x=x+1
        if x==0:
            print("ID not found")
def max_salary():
    max=0
    f=open("employees.csv","r")
    f_new=csv.reader(f)
    next (f_new)
    for i in f_new:
        if i[2]>max:
            r=i[0]
            n=i[1]
            m=i[2]
            max=i[1]
        print("details of maximum salary employees")
        print(r,"\t",n,"\t",m)
search()
max_salary()
