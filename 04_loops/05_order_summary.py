""" 
You're preparing an order summary with customer names and their total bill. 
Task: 
1. Use two lists: one for names and one for bills. 
2. Print: "[Name] paid ₹[amount]"
"""


names = ["Aditya", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for names, amounts in zip(names, bills):
    print(f"{names} paid {amounts} rupees")

