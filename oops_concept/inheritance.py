# Inheritance: one class inherits properties and methods of another.
# it promotes code reusability

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("I make sounds!")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meows!")

dog=Dog("Tommy")
cat=Cat("Kitty")
dog.speak()
cat.speak()