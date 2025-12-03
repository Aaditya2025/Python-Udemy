# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)


# prepare_chai(chai)
# print(chai)

chai = [1,3,5]

def edit_chai(cup):
    cup[1] = 42
edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")  #positional  
make_chai(tea="Green", sugar="Medium", milk="No") #keywords

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="Yes")


#args: The argument without keyword is called args. 
#kwargs: The argument with keowrd is called kwargs.     