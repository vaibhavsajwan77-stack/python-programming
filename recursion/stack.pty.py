def push(s,val):
    s.append(val)
    print("data insert successully")
def pop(s):
    s.pop()
s=[]
while True:
    choice=int(input("press 1 for push,2 for pop,3 for peek&4 for display . 5 for quit"))
    if choice==1:
        val=int(input("enter the value for insert"))
        push(s,val)
    elif choice==2:
        if ln(s)==0:
            print("stack is empty")
        else:
            print(s)
    elif choice==5:
        break
