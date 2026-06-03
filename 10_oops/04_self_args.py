class ChaiCup: 
    size = 150 

    def describe(self): 
        return f"A {self.size}ml chai cup"    #Inside class if we need to use any fun. or property then we use 'self'. 


cup = ChaiCup()

print(cup.describe())
print(ChaiCup.describe(cup))  #here it need to take reference from the object also. 

large_cup = ChaiCup()
large_cup.size = 500
print(ChaiCup.describe(large_cup))  #doing the same thing so for differentiating this it needs to pass object reference. 
