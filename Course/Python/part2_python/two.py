import one
print("Top level two.py")

one.func()

if __name__ == '__main__':
    print("Two.py being run directly")
else:
    print("two.py is run directly")


#whenever the twp.py is run
#__name__ is set to __main__ and the corresponding if is true
