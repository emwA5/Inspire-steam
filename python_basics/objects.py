#MWANGI ERICK
#19.02.2026
#program to create objects

class Human:
    # First we define the attributes of a human being
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True

    # we the create a constructor for the class/object
    # the constructor will be used to create copies of the objects
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self, story): 
        print(f"Hello, I am {self.human_name}Here is a story")
        print(story)

# create the humans
Amani = Human("Amani", 17)
Triza = Human("Triza", 17)

# Let the humans created do things
Amani.tell_story("there was once a bot that said hello world")
print("Amani's age is",Amani.human_age)

#accessing class attributes
print("Amani is a", Amani.type)
