def display(list,index=0):
    if index==len(list):
        return 1
    print(list[index])
    display(list,index+1)
fruit=["mango","banana"]
display(fruit)
    
