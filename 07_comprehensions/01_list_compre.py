# Comprehension: Are a concise way to create list, sets, dictionaries, or generators in python using a single line of code. 

# Where are they used in Real life?: filter item, transform item, create a new collection, flatten nested structure 

# What purpose Do they serve?: cleaner code, Faster execution

# Types of comprehensions: List , Sets, Dictionary, Generators 

menu = [
    "Masala Chai", 
    "Iced Lemon Tea", 
    "Green Tea", 
    "Iced Peach Tea", 
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)