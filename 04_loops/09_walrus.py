# value = 13
# remainder = value % 5

# if remainder: 
#     print(f"Not divisilbe, remainder is {remainder}")
# Walrus Operator (:=) : It assigns the values to variables as part of a larger expression.

value = 13

# if (remainder := value % 5 ):
#     print(f"Not divisible, remainder is {remainder}")

# size = ["small", "medium", "large"]
# if(requested_size := input("Enter your cup size: ")) in size: 
#     print(f"Serving {requested_size} chai")
# else: 
#     print(f"{requested_size} size is unavailable")

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavors)

while (flavor := input("Choose your flavour: ")) not in flavors: 
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")