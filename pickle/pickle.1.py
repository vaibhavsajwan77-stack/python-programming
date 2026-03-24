import pickle
def write():
    f=open("myfile.det","wb")
    name=["ravi","deppak","ajay","sanjay"]
    pickle.dump(name,f)
    f.close()
def read():
    f=open("myfile.det","rb")
    data=pickle.load(f)
    print(data)
    f.close()
write()
read()
