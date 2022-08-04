class Human: # create base/superclass - Human
    def __init__(self): # use constructor to initialise attributes
        self.name = "Homo Sapien"
        self.age = 1000
        self.car = "fiat panda"
        self.get_pregnant = True






    def eat(self): # class method which returns a string
        return self.name, "is eating"

    def sleep(self): # class method which returns a string
        return self.name, "is sleeping"

    def walk(self): # class method which returns a string
        return self.name, "is walking"

    def talk(self): # class method which returns a string
        return self.name, "is talking"