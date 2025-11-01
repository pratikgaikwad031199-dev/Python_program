# Hiding implementation details and showing only necessary features.
# 👉 Done using abstract classes (abc module in Python).
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Started")
class Bike(Vehicle):
    def start(self):
        print("Bike Started")
class Truck(Vehicle):
    def start(self):
        print("Truck Started")

# ve=Car()
# ve.start()
for V in (Car(),Bike(),Truck()):
    V.start()