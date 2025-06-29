class Student:
    name="Pooja"

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

"""There is a __init__() [constructor] always present (doesnt matter you define the fn or not)
Which executes when object is initiated."""

#parameterized constructor::
class Cars:
    company="Toyota"     #same for every obj(car) do not vary so not in self.__ form[class attr.]

    def __init__(self,colour,price):    #self param is must. It can be given any name.    
        print("Properties of car to be constructed.")
        self.colour=colour   #varies for every obj(car) varies so in self.__ form[obj attr]
        self.price=price

"""c1 same as self (both points at the obj. cars)"""

c1=Cars("brown",900000000)    #Object creation () is to call the fn,automatically call fn.
print(c1.colour,c1.price,c1.company)
c2=Cars("black",100000000)
print(c2.colour,c2.price,c2.company)  #The var,data stored is called attribute


#METHOdS:::
class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome student",self.name)
    def get_marks(self):
        return self.marks
    
s1=Student("Pooja",97)
s1.welcome()
print(s1.name,s1.marks)
print(s1.get_marks())


