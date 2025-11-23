chai_order = dict(type = "Masala chai", size = "large", sugar = 2); 
print(f"Chai order: {chai_order}"); 

chai_recipe = {} 
chai_recipe["base"] = "black tea"; 
chai_recipe["liquid"] = "milk"; 
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = dict(type = "Masala chai", size = "large", sugar = 1); 

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_recipe = {"cardamom": "crushed", "ginger": "sliced"}; 
chai_recipe.update(extra_recipe); 
print(f"Updated chai recipe: {chai_recipe}")

# DON'T USE THIS: 
# chai_size = chai_order["customer note"] 
# print(f"Chai size is: {chai_size}")

# USE THIS INSTEAD OF ABOVE: 
chai_size = chai_order.get('amount', "N/A")
print(f"Size is : {chai_size}")

# NOTE: So all operation we do in the SET is also applicable in DICTIONARY.
