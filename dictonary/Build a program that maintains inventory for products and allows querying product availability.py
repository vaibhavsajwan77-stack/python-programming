INVENTORY={
"laptop":10,
"mouse":25,
"keyboard":15
}
product=input("enter the product name to check availability: ")
if product in INVENTORY:
  print(f"{product} is available with quantity {INVENTORY[product]}")
else:
  print(f"{product} is not available in inventory")
check_quantity=int(input("enter the product you want to check quantity for: "))
for item,quantity in INVENTORY.items():
  if quantity>=check_quantity:
    print(f"{item} has sufficient quantity: {quantity}")
  else:
    print("item is out of stock")