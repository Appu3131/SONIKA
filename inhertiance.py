
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):

        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")


class Cat(Animal):
    def __init__(self, name, color):

        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows.")


dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Gray")


dog.speak() 
