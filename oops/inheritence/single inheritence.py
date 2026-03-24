class human:
    def __init__(self, num_heart):
        self.num_eyes=2
        self.num_heart=num_heart
        self.num_nose=1
    def eat(self):
       print("I can eat food")
    def work(self):
        print("I can work hard")
class male(human):
    def __init__(self, name, heart):
       super().__init__(heart)
       self.name=name
male_1=male("vaibhav", 1)
print(male_1.name)
print(male_1.num_heart)
print(male_1.num_eyes)