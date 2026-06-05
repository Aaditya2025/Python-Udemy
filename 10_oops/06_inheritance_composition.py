class BaseChai: 
    def __init__(self, type_):
        self.type = type_

    def prepare(self): 
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):   #here we just use inheritance which mean now Masalachai  
    def add_spices(self):     #instances able to use all property and method of BaseChai.
        print("Adding cardamom, ginger, cloves.")

class ChaiShop: 
    chai_cls = BaseChai
        
    def __init__(self): 
        self.chai = self.chai_cls("Regular") 

    def serve(self): 
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()      #See this is called composition we are doing getting access of parent class method. 

class FancyChaiShop(ChaiShop): 
    chai_cls = MasalaChai

shop = ChaiShop() 
fancy = FancyChaiShop()    #fancy: Now this variable get access of all the methods present in the FancyChaiShop() Class. 
shop.serve()
shop.serve() 
fancy.chai.add_spices()  #here we are inheriting ChaiShop so for getting access of methods of MasalaChai we need to use variable which have reference of MasalaChai.       