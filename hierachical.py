
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")


dog = Dog("Rex")
cat = Cat("Whiskers")


dog.eat()
dog.speak()

cat.eat()
cat.speak()
