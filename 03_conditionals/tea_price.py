"""
A tea stall offers different prices for different cup sizes. Write a program that calculates the price based on size.
Task:
1. Input: "small", "medium", "large".
2. Small = 10Rs. , Medium = 15Rs. , Large = 20Rs.
3. If invalid: show "Unknown cup size".

"""

cup_size = input("Choose you cup size (small/medium/large):").lower()

if cup_size == "small": 
    print(f"The price of {cup_size} cup is 10Rs.")
elif cup_size == "medium": 
    print(f"The price of {cup_size} cup is 15Rs.")
elif cup_size == "large": 
    print(f"The price of {cup_size} cup is 20Rs.")
else: 
    print(f"Unknown cup size!")
