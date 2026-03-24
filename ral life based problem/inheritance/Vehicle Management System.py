# Base Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} has stopped.")


# Subclass: Car
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}, Doors: {self.num_doors}")


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def display_info(self):
        print(f"Bike: {self.year} {self.make} {self.model}, Type: {self.bike_type}")


# Subclass: Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_info(self):
        print(f"Truck: {self.year} {self.make} {self.model}, Capacity: {self.capacity} tons")


# ----- Usage Example -----
car = Car("Toyota", "Corolla", 2022, 4)
bike = Bike("Yamaha", "MT-15", 2021, "Sports")
truck = Truck("Tata", "Ultra", 2020, 10)

car.start()
car.display_info()
car.stop()

bike.start()
bike.display_info()
bike.stop()

truck.start()
truck.display_info()
truck.stop()
