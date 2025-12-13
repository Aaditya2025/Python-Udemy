#Types of function: 1. Pure vs impure,  2. Recursive functions,  3. Lambdas(Anonymous function)


def pure_fnc(value):
    return value * 10; 

total_sum = 0
# not recommended to use. 
def impure_fnc(value):
    global total_sum
    total_sum += value


# 2. Recursive functions: 

def pour_chai(n): 
    print(n)
    if n == 0: 
        return "All cups poured"
    return pour_chai(n-1)

result = pour_chai(3)

print(result)


# 3. Lambdas (Anonymous function):

chai_types = ["kadak", "masala", "lemon", "ginger", "masala"]

strong_chai = list(filter(lambda chai: chai != "masala", chai_types))

print(strong_chai)


# Rules of Python lambdas:

# ❌ Only one expression

# ❌ No statements (if, for, while)

# ❌ No assignments

# ✔️ Implicit return




# Step-by-step (Python view):

# 1. lambda chai: chai != "masala"

# Anonymous function

# Takes one element at a time

# Returns True or False

# 2. filter(function, iterable)

# Goes through each item in chai_types

# Keeps items where function returns True

# 3. list(...)

# Converts the filtered result into a list

# (Important: filter returns an iterator, not a list)