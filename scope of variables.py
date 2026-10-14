
def my_function():
    x = 10
    print(x)

my_function()

x = 20

def my_function():
    print(x)

my_function()
print(x)

x = 100

def test():
    x = 50
    print("Local:", x)

test()
print("Global:", x)

x = 10

def change_value():
    global x
    x = 50

change_value()
print(x)

def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()
