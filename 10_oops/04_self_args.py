class ChaiCup: 
    size = 150 

    def describe(self): 
        return f"A {self.size}ml chai cup"    #Inside class if we need to use any fnc. or property then we use 'self'. 


cup = ChaiCup()

print(cup.describe())
print(ChaiCup.describe(cup))  #here it need to take reference from the object also. 

large_cup = ChaiCup()
large_cup.size = 500
print(ChaiCup.describe(large_cup))  #doing the same thing so for differentiating this it needs to pass object reference. 


"""
"self Keyword": self refers to the current object.

Ex.:
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

When you write: s1.display()

Python internally does: Student.display(s1)

So self becomes s1.
"""