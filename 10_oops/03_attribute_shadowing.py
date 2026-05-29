class Chai: 
    temperature ="hot"
    strength = "Strong" 

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild" 
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("Cup size is: ", cutting.cup)
print("Direct look into the class ", Chai.temperature) 

del cutting.temperature
del cutting.cup
print(cutting.temperature)  #it will take value from the class after del still not show error. 
print(cutting.cup)  #this is called shadowing it will through error 