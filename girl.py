# use inheritance to import parent class from another file
from female import Female

class Girl(Female): # implement class with parent class

    def __init__(self): # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.name = "girl"
        self.gender = "boy"
        self.adams_apple = False

    def education(self): # class method which returns a concatenated string using attributes
        return self.name, "goes to school"

    def play(self): # class method which returns a concatenated string using attributes
        return self.name, "is playing with a football in a gender neutral way"

    def join_WNBA(self): # class method which returns a concatenated string using attributes
        return self.name, "dreams of joining the WNBA"

    def talk(self):  # class method which returns a string using polymorphism to implement a different process with the same interface to other classes.
        return self.name, "can talk about weird stuff"

# creates an object instance of the Boy() class
some_gal = Girl()

# implements prints of the methods within the instance class
print(some_gal.play())
print(some_gal.join_WNBA())

try: # create try catch exception which attempts to access protected method
    print(some_gal.__have_kids())
except: # provides exception for case of try failure
    print("you're to young for this kid")


