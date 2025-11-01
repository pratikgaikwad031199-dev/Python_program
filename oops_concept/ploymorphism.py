# method overriding
class Animal():
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.speak())

dog=Dog()
cat=Cat()
animal_sound(dog)
animal_sound(cat)