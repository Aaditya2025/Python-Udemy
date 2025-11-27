""" You're creating a tea menu board. 
Each item must be numbered. 
Task: 
 1. Use enumerate() to print menu items with numbers. 
"""

menu = ["Green", "Lemon", "Spiced", "Mint"]

for index, item in enumerate(menu, start=1):
    print(f"{index} : {item} chai")

# Note: 'enumerate' help you to manipulate the indexing and print that however you want. 