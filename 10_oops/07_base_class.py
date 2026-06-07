# Way for Accessing of Base Class: 1. Code Duplication 2. Explicit call 3. super()

# Base Class: 
class Chai: 
    def __init__(self, type_, stregth):
        self.type = type_
        self.strength = stregth


# 1. Code Duplication : Using this way

class GingerChai(Chai): 
    def __init__(self, type_, stregth, spice_level):
        self.type = type_
        self.strength = stregth
        self.spice_level = spice_level

# 2. Explicit Call : Using this way to call Base Class

class GingerChai(Chai): 
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level

# 3. super() : Using this way to call Base Class

class GingerChai(Chai): 
    def __init__(self, type_, stregth, spice_level):
        super().__init__(type_, stregth)
        self.spice_level = spice_level
