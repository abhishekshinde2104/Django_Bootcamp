#Syntax error
#Name error
#Exception handling
#using try except and finally

#try:
    #You do you operations here
#except Exception 1
    #If there is some exception 1
#except Exception 2
    #if there is some exception 2
#    ...

#else:
    #If there is exception then execute this

try:
    f = open("simple.txt",'r')
    f.write("Test to write to simple text !")
except IOError:
    print("Error : Could not file or read data")
#IOError is an input/output error and this exception will check for this specific error
except:
    print("This is a general error..if you dont know the error name")

finally:
    print("I was work no matter what")
#else:
#    print("Success")
#    f.close()
#print("Hello world")

#try-except helps to get the error and then continue with your code
#finally keyword the block will always run regardless there is an error
