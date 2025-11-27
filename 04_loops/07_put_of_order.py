flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours: 
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued": 
        print(f"{flavour} chai found") 
        break
    print(f"{flavour} chai found") 

print(f"Out side of loop")