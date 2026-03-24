class human:
  print("it is form init human")
  def __init__(self,num_shirts):
    self.hands=2
    self.num_shirts= num_shirts
  def eat(self):
    print("i can eat more")
  def work(self):
    print("i can work hard")
class male:
  print("it is form init male")
  def __init__(self,num_nose):
    self.eyes=2
    self.num_nose=num_nose
  def gym(self):
    print("i like to go gym")
class boy(human,male):
  def __init__(self):
    human.__init__(self,12)
    male.__init__(self,1)
  def name(self):
    print("ronny")
boy_2=boy()
print(boy_2.num_nose)
print(boy_2.num_shirts)
boy_2.name()