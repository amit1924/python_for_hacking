# call inside function from outside function
# def hello():
#     print("hello world!")

#     def hi():
#         print("Hi function inside hello function")

#     hi()


# hello()

# call function from another function
# below code is for callback function


# def hello(callback):
#     print("this is hello function")
#     callback()


# def hi():
#     print("this is hi function")


# hello(hi)


################################################################

# decorator function


# def decorator_function(callback):
#     def wrapper():
#         print("this is wrapper function,it will be called first")
#         callback()
#         print("after wrapper this function will be called")

#     return wrapper


# def hello():
#     print("this is hello function")


# # Applying the decorator manually
# hello_decorator = decorator_function(hello)

# # Now, when you call hello(), it will execute the decorated version
# hello_decorator()


# or #$$$$$$$$$$
def decorator_function(callback):
    def wrapper():
        print("this is wrapper function,it will be called first")
        callback()
        print("after wrapper this function will be called")

    return wrapper


# In this example, the @decorator_function syntax is used to apply the decorator_function to the hello function. When you call hello(), it actually calls the wrapper function returned by the decorator_function, which then calls the original hello function within it.
@decorator_function
def hello():
    print("this is hello main  function")


hello()
