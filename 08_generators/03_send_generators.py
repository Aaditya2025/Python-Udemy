def chai_customer(): 
    print("Welcome! What chai would you like?")
    order = yield
    while True: 
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer(); 

next(stall)   #start the generator

stall.send("Masala Chai")  #When you pass the value only then it will start printing.x
stall.send("Lemon Chai")