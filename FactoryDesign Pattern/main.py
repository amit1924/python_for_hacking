class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")


# Usage
animal_factory = AnimalFactory()
dog = animal_factory.create_animal("Dog")
print(dog.speak())  # Output: Woof!

cat = animal_factory.create_animal("Cat")
print(cat.speak())  # Output: Meow!


################################
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass


class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()


class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle()


# Usage
circle_factory = CircleFactory()
circle = circle_factory.create_shape()
circle.draw()  # Output: Drawing Circle

rectangle_factory = RectangleFactory()
rectangle = rectangle_factory.create_shape()
rectangle.draw()  # Output: Drawing Rectangle
