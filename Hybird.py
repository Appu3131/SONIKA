
class Animal:
    def speak(self):
        print("Animal speaks.")


class Vehicle:
    def drive(self):
        print("Vehicle is driving.")


class Dog(Animal, Vehicle):
    def bark(self):
        print("Dog barks.")


class Car(Animal, Vehicle):
    def honk(self):
        print("Car honks.")


dog = Dog()
car = Car()

dog.speak()
dog.drive()
dog.bark()

car.speak()
car.drive()
car.honk()
