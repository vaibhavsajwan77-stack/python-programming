import pickle
def write:
    f=open("redo.det","wb")
    name=["name","class","roll number"]
    pickle.dump(nmae,f)
    f.close()
def read():
    f=open("redo.det","rb")
    data=pickle.load(f)
    f.close()
write()
read()
