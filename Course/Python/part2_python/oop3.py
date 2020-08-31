#Inheritance
#Special Methods
"""Inheritance is the used to reuse of code reduction of complexity

class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):
    def  __init__(self):
        #Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Whooff")

    #overriding the function
    def eat(self):
        print("DOg eatingg")

myd=Dog()
myd.whoAmI()
myd.eat()
myd.bark()


"""



class Book():

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        #this is a special function which will be called whenever u want to print the object directly
        return ("Title:{} , Author:{} , Pages:{}".format(self.title,self.author,self.pages))
        #return "hello"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed")


b=Book("Python","Jose",200)
print(b)
print(len(b))#this goes inside the class and return the __len__ function
#print(len(b))-->Errorrr
del b#this will goto to class of the object and search for __del__ function 
