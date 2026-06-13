# Method Resolution Order : 
class A: 
    label = "A: Base Class"

class B(A): 
    label = "B: Masala blend" 

class C(A): 
    label = "C: Herbal blend" 

class D(B, C):    # B is the first argument so this class consider B as the first parent and print that value. 
    pass

cup = D()

print(cup.label)