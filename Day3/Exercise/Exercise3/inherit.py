class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Doors: {self.doors}"
class Bike(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: {self.type}"
# Example usage
car = Car("Toyota", "Camry", 2020, 4)
bike = Bike("Yamaha", "MT-07", 2021, "Sport")       
print(car.display_info())  # Output: 2020 Toyota Camry, Doors: 4
print(bike.display_info()) # Output: 2021 Yamaha MT-07, Type: Sport