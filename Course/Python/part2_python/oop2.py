"""
How to attributes and methods to the class
attributes-->characteristics of object
method-->operation performed by object

SYNTAX FOR CREATING AN attributes:
self.attribute_name = something
__specialmethod__

class_object_attributes are always the same for any instance of the class
"""

"""class Dog():

    #CLASS OBJECT Attribute
    species = 'mammal'

    def __init__(self,breed,name):
        #initialization
        #this method is called automatically
        #self keyword tells that this refers to itself i.e the actual class object

        self.breed = breed
        self.name = name




#mydog = Dog(breed = "Lab",name="Sammy")
mydog = Dog("Lab","Sammy")
#otherdog=Dog("husky")
print(mydog.breed)
print(mydog.name)
#print(otherdog.breed) --> o/p : husky
print(mydog.species)"""


class Circle():
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

    #self keyword in the area() mtd tells that its a function of the class and not any free floating function
    def area(self):
        return self.radius * self.radius * Circle.pi
        #here self.radius will tell to use the radius of the class and not any variable radius

    #resetting radius
    def set_radius(self,new_r):
        self.radius = new_r

myc=Circle(7)
myc.set_radius(100)
print(myc.area())
