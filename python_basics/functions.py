#MWANGI ERICK
#19.02.2026
#program to show how to cook an egg

def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2

    print(f"the pan is {pan} and the fire is {moto}, \
        add {oil} and cook {eggs} eggs")

print("here is statement 1")

print("here is statement 2")

cook_egg()

print("here is statement 3")


# Ride fare creating function

def create_fare(route, distance, is_rush_hour):

    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5
    print(f"your fare to {route} is {fare}")

rush_hour = True
returned_fare = create_fare("Juja_Ollsops", 7, rush_hour)
print(f"the fare is: {returned_fare}")
# passing a list as a parameter

def write_all_intrests(intrests):
    for intrest in intrests:
        print(f"I am intrested in {intrest}")

all_intrests = ("socialising", "intemacy", "balling", "partying")

write_all_intrests(all_intrests)

