staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff: 
    if age >= 18: 
        print(f"{name} is eligible to manage the staff")
        break
else: 
    print(f"No one is eligible to manage the staff")

# Note: So the above else is not part of the if condition it is the part of the for condition that means when for loop doesn't found anything to print then this else condition will print otherwise it will not printed. 