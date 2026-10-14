
def greet():
    print("Hello!")
    print("Welcome to Python")

greet()

def greet(name):
    print("Hello", name)

greet("maha")
greet("ariba")

def add(a, b):
    print(a + b)

add(10, 20)
add(5, 3)

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

def square(number):
    return number * number

x = square(5)
print(x + 10)

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Aqsa")

def check_result(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(check_result(75))
print(check_result(40))

