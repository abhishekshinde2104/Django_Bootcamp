"""
s = "Global Varible"

def func():
    #global s -->this will commit the changes to the  global s also
    #s=50
    #print(s)
    mylocal = 10

    print(locals())
    print(globals())
    print(globals()['s'])

func()
"""
"""
def hello(name="Aditya"):
    return "hello "+name

print(hello())

mynewgreet = hello
#new_variables = function
print(mynewgreet())
"""

"""
#function inside function
def hello(name = "Aditya"):
    print("The hello function has been run ")

    def greet():
        return "This string is inside greet"

    def welcome():
        return "This string is inside welcome"

    #print(greet())#gets printed here-----SCOPE
    #print(welcome())#gets printed here ---SCOPE
    #print("End of hello()")

    if name=='Aditya':
        return greet
    else:
        return welcome

x=hello()
print(x())
"""

"""
#Function as an argument

def hello():
    return "HI!! aditya"

def other(func):
    #here we are passing the func
    print("Heyyyy")
    print(func())
    #here we are calling the func()

print(other(hello))
"""

#Decorator

def new_decorator(func):

    def wrap_func():
        print("Code here before excuting func")
        func()
        print("Func() has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This ffunction needs a decorator")


#func_needs_decorator = new_decorator(func_needs_decorator)

#the above thing can be written assss:
