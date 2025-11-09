# Tuples: It is immutable.

masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
print(masala_spices[2])

ginger_ratio, cardamom_ratio = 2, 1;  #It will divide the ratio respectively and behinc the scene tuple is responsible.

print(f"Ratio is G:{ginger_ratio} and C:{cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio #This is unique behaviour of python you easily swap the two variables. 
print(f"Ratio is G:{ginger_ratio} and C:{cardamom_ratio}")


#membership testing:It is case sensitive. 
print(f"Is cinnamon is masala spices ? {'cinnamon' in masala_spices}")