class person:
    def __init__(self, name, id, contact):
        self.name=name
        self.id=id
        self.contact=contact
    def get_details(self):
        print(f"name :{self.name}")
        print(f"ID : {self.id}")
        print(f"contact: {self.contact}")
class student(person):
    def __init__(self, name, id, contact, course):
        super().__init__(name, id, contact)
        self.course=course
    def get_details(self):
        super().get_details()
        print(f"course : {self.course}")
class faculty(person):
    def __init__(self, name, id, contact, department):
        super().__init__(name, id, contact)
        self.department=department
    def get_details(self):
        super().get_details()
        print(f"department : {self.department}")
class staff(person):
    def __init__(self, name, id, contact, role):
        super().__init__(name, id, contact)
        self.role=role
    def get_details(self):
        super().get_details()
        print(f"ROLE {self.role}")
s=student("PRAKASH","25CE-53", 9286402205, "BTECH- CSE")
f=faculty("VAIBHAV","25CE-77",6396157264,"SCHOOL OF TECHNOLOGY")
c=staff("RISHAB","25CE-63",9897447663,"GATE KEEPER")
print("\nSTUDENT IS \n")
s.get_details()
print("\nfaculty is\n")
f.get_details()
print("\nstaff\n")
c.get_details()
