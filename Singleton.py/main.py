# The Singleton class defines a private class variable _instance to hold the single instance of the class.
# The __new__  method is overridden to ensure that only one instance of the class is created. If the _instance variable is None, a new instance is created and assigned to it.
# Subsequent calls to create instances of Singleton will return the same instance created earlier

# cls is a conventional name used as the first parameter in class methods. It stands for "class" and is used to refer to the class itself within the method.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


Singleton1 = Singleton()
Singleton2 = Singleton()

print(Singleton1 == Singleton2)


# #######  or     #####


class Person:
    _instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls, name):
        if cls._instance is None:
            cls._instance = cls(name)
        return cls._instance


# Usage
person1 = Person.get_instance("Alice")
person2 = Person.get_instance("Bob")

print(person1 is person2)  # Output: True
print(person1.name)  # Output: Alice
print(person2.name)  # Output: Alice
