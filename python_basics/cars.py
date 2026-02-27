#MWANGI ERICK
#23.02.2026
#program to show classes in python

class Car():
    # attributes of the car
    def __init__(self, model, make, color, year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year

    # print car details
    def print_details(self):
        print(f"{self.make} {self.model} of {self.color} was manufactured in {self.year}")


# instantiate a class object
my_Car = Car("Atenza", "Mazda", "blue", "2025")

# call the method
my_Car.print_details()

