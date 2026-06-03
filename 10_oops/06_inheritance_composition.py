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
        self.chai.prepare() 

class FancyChaiShop(ChaiShop): 
    chai_cls = MasalaChai

shop = ChaiShop() 
fancy = FancyChaiShop() 
shop.serve()
shop.serve() 
fancy.chai_cls.add_spices()