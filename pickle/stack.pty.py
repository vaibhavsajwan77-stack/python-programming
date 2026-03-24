def push(s,val):
    s.append(val)
    print("data insert successully")
def pop(s):
    s.pop(val)
def peek(s):
    index=len(s)-1
    print("peek element is=",s[index])
def display(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i])
s=[]
while True:
    choice=int(input("press 1 for push,2 for pop,3 for peek & 4 for display . 5 for quit"))
    if choice==1:
        val=int(input("enter the value for insert"))
        push(s,val)
    elif choice==2:
        if len(s)==0:
            print("empty stack")
    elif choice==3:
        if len(s)==0:
            print("empty stack")
        else:
            print(s)
    elif choice==4:
        if len(s)==0:
            print("empty stack")
        else:
            display(s)
    elif choice==5:
        break
    else:
        print("this is invalid choice")
