# use inheritance to import parent class from another file
from human import Human

class male(Human): # implement class with parent class

    def __init__(self): # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.name = "male"
        self.get_pregnant = False
        self.avg_height = 5.8
        self.educated = False



    def education(self): # class method which returns a concatenated string using attributes
        return self.name, "has no education"

    def __have_kids(self): # class method which returns a concatenated string using attributes
        return "It is", self.get_pregnant, "that the", self.name, "can have children"

    def __look_after_kids(self): # class method which returns a concatenated string using attributes
        return self.name, "is looking after their kids this weekend"