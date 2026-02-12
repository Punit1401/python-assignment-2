# 5. Write a function inside another function.

def vehicle():
    print("This is vehicle function")
    def car():
        print("This is a car")
    car()
vehicle()