""" Your shop adds a 10% VAT on every order. You want this to be consistent and traceable. 
Task: 
1. Write add_vat(price, vat_rate)
2. Use it to compute final prices for 3 orders. 
"""

def add_vat(price, vat_rate): 
    return price * (100 + vat_rate)/100

orders = [100, 120, 150]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original Price: {price}, Final Price with VAT: {final_amount}")