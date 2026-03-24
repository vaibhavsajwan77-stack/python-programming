import pickle
def write():
    f=open("abc.det","wb")
    record=[]
    while True:
        roll=input("enter the roll number")
        name=input("enter the name")
        marks=input("enter the marks")
        list=[roll,name,marks]
        records.append(list)
        choice=input("enter the record(y\n)")
        if choice=='n':
            break
    pickle.dump(record,f)
    print("data store successfully")
def read():
    f=open("abc.det","rb")
    data=pickle.load(f)
    for i in data:
        print(i)
write()
read()
