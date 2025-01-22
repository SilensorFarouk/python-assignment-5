# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # Base class move method, to be overridden by subclasses

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Creating objects for each class
car = Car()
plane = Plane()
boat = Boat()

# Calling the move() method for each class
print(car.move())    # Output: Driving 🚗
print(plane.move())  # Output: Flying ✈️
print(boat.move())   # Output: Sailing 🚤
