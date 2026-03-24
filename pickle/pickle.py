import pickle
def write():
    f=open("my file.det","wb")
    name=["ravi","deppak","ajay","sanjay"]
    pickle.dump(name,f)
    f.close()
def read():
    f=open("my file.det","rb")
    data=pickle.read(f)
    print(data)
    f.close()
write()
read()
