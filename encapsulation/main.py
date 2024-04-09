# class Car:
#     def __init__(self, make, model):
#         self.__make = make  # Private attribute
#         self.__model = model  # Private attribute

#     def get_make(self):
#         return self.__make

#     def set_make(self, make):
#         self.__make = make

#     def get_model(self):
#         return self.__model

#     def set_model(self, model):
#         self.__model = model

#     def display_info(self):
#         print(f"Car: {self.__make} {self.__model}")


# # Create an instance of the Car class
# my_car = Car("Toyota", "Camry")


# # Accessing attributes using getter methods
# print("Make:", my_car.get_make())
# print("Model:", my_car.get_model())

# # Modifying attributes using setter methods
# my_car.set_make("Honda")
# my_car.set_model("Accord")

# # Displaying car information
# my_car.display_info()


##############################################
class Car:
    def __init__(self, make):
        self._make = make  # Private attribute with underscore convention

    @property
    def Make(self):
        return self._make

    @Make.setter
    def Make(self, new_make):
        self._make = new_make

    # Static methods are associated with the class itself rather than its instances.
    @staticmethod
    def model():
        print("this is new model")


print(Car.model())

# Creating an instance of the Car class
car1 = Car("Toyota")


# Accessing the make attribute using the getter method
print(car1.Make)

# Changing the make attribute using the setter method
car1.Make = "Honda"

# Accessing the updated make attribute
print(car1.Make)
print(car1.model())
