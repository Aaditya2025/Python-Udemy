# List[]: It is mutable. Just like an array.

ingredients = ["water", "milk", "black tea"]; 
ingredients.append("sugar"); 
print(f"Ingredients are: {ingredients}"); 
ingredients.remove("water"); 
print(f"Ingredients are: {ingredients}"); 

spice_option = ["ginger", "cardamom"]; 
chai_ingredients = ["water", "milk"]; 

chai_ingredients.extend(spice_option); # Use '.extend' when you want to merge any other list to your list. 
print(f"chai:{chai_ingredients}")

chai_ingredients.insert(2, "black tea"); # Use '.insert' when you want to add any thing on a specific place.
print(f"Update chai: {chai_ingredients}")

last_added = chai_ingredients.pop(); 
print(f"{last_added}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

chai_ingredients.sort(); 
print(f"chai: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]; 
print(f"Maximum Sugar levers: {max(sugar_levels)}"); 
print(f"Minimum Sugar levels: {min(sugar_levels)}"); 


# Operator Overloading: When any operator used to do more than one task then that is called operator overloading.

base_liquid = ["water", "milk"]; 
extra_flavor = ["ginger"]; 
print(f"Liquid mix: {base_liquid + extra_flavor}");  

strong_brew = ["black tea", "water"] * 3;  #So this is Operator Overloading, we get our list 3 times.
print(f"{strong_brew}"); 

raw_spice_data = bytearray(b"CINNAMON"); # Using 'bytearray' you able to
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes: {raw_spice_data}"); 