from functools import wraps    #It will preserve the metadata of functions inside decorators. 

def my_decorator(func):
    @wraps(func)
    def wrapper(): 
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet(): 
    print(f"Hello from decorators class")

greet()

print(greet.__name__) 

"""
Very tiny example to remember forever:

def deco(func):

    def wrapper():
        print("START")
        func()
        print("END")

    return wrapper


@deco
def hello():
    print("Hello")


hello()

Output:

START
Hello
END


Equivalent to:

hello = deco(hello)

Decorator — Quick Notes:
    1. Decorator = a function used to add extra functionality to another function without changing original code.
    2. A decorator takes a function as input, creates a wrapper function, and returns it.
    3. wrapper() contains the extra code (before/after logic).
    4. @decorator is shortcut for:
            function = decorator(function)
    @wraps(func) preserves original function details like __name__ and docstring.

Simple flow:

Original Function
↓
Decorator wraps it
↓
Extra behavior added

"""