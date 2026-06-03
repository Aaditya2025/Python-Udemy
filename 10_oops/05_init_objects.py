class chaiOrder: 
    def __init__(self, type_, size):  # __init__: It is same as constructor. 
        self.type = type_             # Here we use type_ because 'type' is keyword in python so we don't use it as var.  
        self.size = size              # only in constructor you are allowed to declare and use any variable inside that.

    def summary(self): 
        return f"{self.size}ml  of {self.type} chai"
    
order = chaiOrder("Masala", 200)
print(order.summary())

order_two = chaiOrder("Ginger", 220)
print(order_two.summary())