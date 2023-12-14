#local variable can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
