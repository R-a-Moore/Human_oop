# use inheritance to import parent class from another file
from Male import male

class Boy(male): # implement class with parent class

    def __init__(self):  # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.name = "boy"
        self.gender = "girl"
        self.adams_apple = True


    def education(self): # class method which returns a concatenated string using attributes
        return self.name, "goes to school"

    def play(self): # class method which returns a concatenated string using attributes
        return self.name, "is playing with badminton in a gender neutral way"

    def join_WNBA(self): # class method which returns a concatenated string using attributes
        return self.name, "can't join the WNBA"

    def talk(self):  # class method which returns a string using polymorphism to implement a different process with the same interface to other classes.
        return self.name, "can talk about weird stuff"

    def do_somehting(self):
        pass # uses pass to avoid errors being thrown for not having any code written in the definition of teh do_something() method

# creates an object instance of the Boy() class
dat_boy = Boy()

# implements prints of the methods within the instance class
print(dat_boy.talk())
print(dat_boy.play())
print(dat_boy.join_WNBA())

try: # create try catch exception which attempts to access protected method
    print(dat_boy.__have_kids())
except: # provides exception for case of try failure
    print("you're to young for this kid")