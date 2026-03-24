class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity

    def display(self):
        print(f"Item: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


class Beverage(MenuItem):
    def __init__(self, name, price, quantity, volume):
        super().__init__(name, price, quantity)
        self.volume = volume

    def display(self):
        super().display()
        print(f"Volume: {self.volume}")


class FoodItem(MenuItem):
    def __init__(self, name, price, quantity, ingredient):
        super().__init__(name, price, quantity)
        self.ingredient = ingredient

    def display(self):
        super().display()
        print(f"Ingredient: {self.ingredient}")


class Dessert(MenuItem):
    def __init__(self, name, price, quantity, calories):
        super().__init__(name, price, quantity)
        self.calories = calories

    def display(self):
        super().display()
        print(f"Calories: {self.calories}")




items = [
    Beverage("Cold Coffee", 150, 2, "300 ml"),
    FoodItem("Burger", 200, 1, "Cheese"),
    Dessert("Cake", 120, 3, "250 kcal")
]

total_bill = 0

print("\n----- RESTAURANT BILL -----\n")

for item in items:
    item.display()
    item_total = item.calculate_price()
    print(f"Item Total: {item_total}")
    print("-" * 25)
    total_bill += item_total

print(f"\nTotal Bill Amount: {total_bill}")

