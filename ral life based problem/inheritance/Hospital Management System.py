class person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_info(self):
        print(f"name:{self.name}")
        print(f"age : {self.age}")
        print(f"gender : {self.gender}")
class doctor(person):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.specialization=specialization
    def show_info(self):
        super().show_info()
        print(f"specialization : {self.specialization}")

class patient(person):
    def __init__(self, name, age, gender, ailment):
        super().__init__(name, age, gender)
        self.ailment=ailment
    def show_info(self):
        super().show_info()
        print(f"ailment : {self.ailment}")
class nurse(person):
    def __init__(self, name, age, gender, shift):
        super().__init__(name, age, gender)
        self.shift=shift
    def show_info(self):
        super().show_info()
        print(f"shift : {self.shift}")
d=doctor("VAIBHAV",25,"MALE","HEART SURGEN")
p=patient("RISHAB",23,"MALE","HEART DISEASE")
n=nurse("PRAKASH",19,"FEMALE","FIRST")
print("\nDOCTOR DETAILS \n")
d.show_info()
print("\nPATIENT DETAILS\n")
p.show_info()
print("\nNURSE DETAILS\n")
n.show_info()
            
