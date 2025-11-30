def update_order(): 
    chai_type = "Elaichi" 

    def kitchen(): 
        nonlocal chai_type   #'nonlocal' keyword helps to access the above variable(chai_type). 
        chai_type = "Kesar"

    kitchen()

    print("After kitchen update", chai_type)

update_order()

#NOTE: 'nonlocal' keyword is designed to access the just above variable. 