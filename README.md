# Human OOp

## OOP
Object oriented programming (OOP) is a computer programming model that organises software around concepts or 'objects', rather than focusing on functions and concrete logic.
### 4 Pillars
OOP has four primary pillars of theory:
- Abstraction: means to simplify and foucs only on the data and processes relevant to the application being built. it helps developers to easily make changes to a program over time.
- Encapsulation: means to hide data and complexity from the user. By only presenting necessary interface/interaction. It enables objects to be self-contained, therefore making troubleshooting easier and increasing program security.
- Inheritance: a class can derive its methods and attributes from another class. Inheritance defines types of relationships (superclass, subclass, baseclass). It reduces development time and increases code reusability.
- Polymorphism: is the process of implementing different types of objects using the same inteface/method. It allows for flexability, reducing logical computation.

## Diagram
Here is an example of OOP in design

## Code
Here is an example of several classes being used to implement the four pillars of OOP.
### Human class

```commandline
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
```

### Male class


```commandline
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
```

### Female class

```commandline
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
```

### Girl class

```commandline
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
```

### Boy class

```commandline
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
```
