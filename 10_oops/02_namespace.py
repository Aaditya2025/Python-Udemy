class Chai: 
     origin = "india" 

print(Chai.origin) 

Chai.is_hot = True
print(Chai.is_hot) 

#Creating objects from class Chai

masala = Chai()

print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False

print("Class: ", Chai.is_hot)
print(f"Masala : {masala.is_hot}")

masala.flavor = "Masala" 

print(masala.flavor)