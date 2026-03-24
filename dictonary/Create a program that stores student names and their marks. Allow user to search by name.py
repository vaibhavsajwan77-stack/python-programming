marks={}
marks["prakash"]=85
marks["rishab"]=100
marks["vikas"]=78
n=input("enter the student you want to search about: ")
if n in marks:
     print(f"{n} has marks {marks[n]}")
else:
   print("student not found")