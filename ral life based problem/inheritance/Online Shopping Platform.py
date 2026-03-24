class product:
  def __init__(self,  name, price, stock):
    self.name=name
    self.price=price
    self.stock=stock
  def display_product(self):
    print(f"product name is {self.name}")
    print(f"product price is :{self.price}")
    print(f"stock of the product is :{self.stock}")
class electronic(product):
  def __init__(self, name, price, stock, warrenty):
    super().__init__(name, price, stock)
    self.warrenty=warrenty
  def display_product(self):
    super().display_product()
    print(f"warrety : {self.warrenty}")
class clothing(product):
  def __init__(self,name, price, stock, size):
    super().__init__(name, price, stock,)
    self.size=size
  def display_product(self):
    super().display_product()
    print(f"size : {self.size}")
class grocery(product):
  def __init__(self,name, price, stock, expire_date):
    super().__init__(name, price, stock)
    self.expire_date=expire_date
  def display_product(self):
    super().display_product()
    print(f"expire_date : {self.expire_date}")
e=electronic("LG",34000,12,"12/09/2026-12/10/2030")
c=clothing("hood", 1200, 3000,12)
g=grocery("atta",750,3000,"12/9/2026")
print("electronic info")
e.display_product()
print("clothes info")
c.display_product()
print("grocery info ")
g.display_product()
