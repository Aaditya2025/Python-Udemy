chai_type = "Plain"

def front_desk(): 

    def kitchen(): 
        global chai_type  
        chai_type = "Irnai"

    kitchen()
    print(f"After kitchen update", chai_type)

front_desk()
print(f"Final global chai: ", chai_type)