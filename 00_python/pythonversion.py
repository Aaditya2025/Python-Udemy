import sys
print(sys.version)

name = "Aditya"
age = 20

# WAYS TO PRINT PYTHON PROGRAMME:

# 1. Using f-strings (modern and best):
print(f"My name is {name} and I am {age} years old.")

# 2. Old-style formatting:
print("My name is %s and I am %d years old." % (name, age))

# 3. With sep and end:
print("A", "B", "C", sep="-")   # A-B-C
print("Line 1", end=" ")
print("Line 2")                 # prints on same line

# NOTES: 
# ✅ Use f-strings for all modern Python code.
# They are:
# Clean and readable
# Fast
# Expression-friendly
# Future-proof

# NOTE: In the python range is never inclusive. 