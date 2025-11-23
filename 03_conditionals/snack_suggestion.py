#TASK: A local cafe wants a program that suggests a snack.
"""
If a customer asks for cookies or samosa, it confirms the order.
Otherwise, it says it's not available. 

Task: 
1. Take snack input.
2. If it's "cookies" or "samosa", confirm the order. 
3. Else, show unavailability. 

"""

snack = input("Enter your preferred snack:").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll server you {snack}")
else:
    print(f"Sorry, we only server cookies or samosa with tea")