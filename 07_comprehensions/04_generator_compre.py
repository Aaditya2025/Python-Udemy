daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]; 

total_cups = sum(sale for sale in daily_sales if sale > 5)
total_cups = (sale for sale in daily_sales if sale > 5)  #This give a stream like result not whole result. It returns generator object it needs to be consumed since it is streaming this one by one that is why we need use sum function. 
total_cups = [sale for sale in daily_sales if sale > 5]   #This will create entire list in the memory. 

print(total_cups)