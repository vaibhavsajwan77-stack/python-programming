import pickle
def write():
    f=open("abc.det","wb")
    record=[]
    while True:
        roll=input("enter the roll number")
        name=input("enter the name")
        marks=input("enter the marks")
        list=[roll,name,marks]
        record.append(list)
        choice=input("enter the record(y/n)")
        if choice=='n':
            break
    pickle.dump(record,f)
    print("data store successfully")
def read():
    f=open("abc.det","rb")
    data=pickle.load(f)
    for i in data:
        print(i)
def serach_roll():
    roll=input("enter the roll number")
    x=0
    f=open("abc.det","rb")
    data=pickle.dump(f)
    next(data)
    for i in data:
        if i[0]==roll:
            print(i)
            x=x+1
        if x==i:
            print("roll is not found")
write()
read()
search()
