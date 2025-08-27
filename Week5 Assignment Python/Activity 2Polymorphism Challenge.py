class Animal:
    def move(self):
        return "The animal moves."


class Dog(Animal):
    def move(self):
        return "The dog runs on four legs."


class Bird(Animal):
    def move(self):
        return "The bird flies in the sky."


class Fish(Animal):
    def move(self):
        return "The fish swims in the water."


# Create objects
dog = Dog()
bird = Bird()
fish = Fish()

# Demonstrate polymorphism
animals = [dog, bird, fish]

for animal in animals:
    print(animal.move())
