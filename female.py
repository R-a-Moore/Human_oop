# use inheritance to import parent class from another file
from human import Human

class Female(Human): # implement class with parent class

    def __init__(self): # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.name = "female"
        self.avg_height = 5.5
        self.educated = True


    def education(self): # class method which returns a concatenated string using attributes
        return "The", self.name, "has an education"

    def __have_kids(self): # class method which returns a concatenated string using attributes
        return "It is", self.get_pregnant, "that the", self.name, "can have children"

    def __look_after_kids(self): # class method which returns a concatenated string using attributes
        return self.name, "isn't looking after their kids this weekend"
