# List: It is mutable. 

ingredients = ["water", "milk", "black tea"]; 
ingredients.append("sugar"); 
print(f"Ingredients are: {ingredients}"); 
ingredients.remove("water"); 
print(f"Ingredients are: {ingredients}"); 

spice_option = ["ginger", "cardamom"]; 
chai_ingredients = ["water", "milk"]; 

chai_ingredients.extend(spice_option); 
print(f"chai:{chai_ingredients}")

chai_ingredients.insert(2, "black tea"); 
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

strong_brew = ["black tea", "water"] * 3;  #So this is Operator Overloading.
print(f"{strong_brew}"); 

raw_spice_data = bytearray(b"CINNAMON"); 
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes: {raw_spice_data}"); 