# To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:W
x = "Fantasic"


def myfunc():
    global x
    x = "Awesome"


myfunc()

print("Python is " + x)
