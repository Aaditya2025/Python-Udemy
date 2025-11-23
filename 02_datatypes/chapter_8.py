# Set {}: It is also mutable data type and the elements present in a set is always unique. 

essential_spices = {"cardamom", "ginger", "cinnamon"}; 
optional_spices = {"cloves", "ginger", "black pepper"}; 

all_spices = essential_spices | optional_spices  # Using '|' this operator we apply the union on a set. 
print(f"All spices are: {all_spices}");     

common_spices = essential_spices & optional_spices; # Using '&' this operator we apply the intersection on a set.  
print(f"Common spices are: {common_spices}"); 

# How to checkout the only items which are only present in any set.

only_in_essential = essential_spices - optional_spices; # '-' is used to extract the item which are only present in the set. 
print(f"Only in essential spices: {only_in_essential}")

#Membership testing: 
print(f"Is 'cloves in optional spices? {'cloves' in optional_spices}")