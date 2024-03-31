def out():
    print("this is output function")
    a = 1

    def inner():
        print("this is inner function")

    b = int(input("Enter any number: "))
    if b > 0:
        inner()


out()
