# import recipes.flavors

# print(recipes.flavors.elachai_chai())

# from recipes.flavors import elachai_chai, gigner_chai

# print(gigner_chai())

from .recipes.flavors import gigner_chai, elachai_chai   #Not recommended to use this. 

from recipes.flavors import *    #It also not recommended to use: That means you want to use everything. 