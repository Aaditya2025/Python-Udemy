def calculate_bill(cups, pricce_per_cup): 
    return cups * pricce_per_cup

my_bill = calculate_bill(3, 15)
print(my_bill)

print(f"Order for table 2:  {calculate_bill(2, 50)}")