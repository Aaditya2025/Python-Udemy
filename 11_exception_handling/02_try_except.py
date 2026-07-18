chai_menu = {"masala": 30, "ginger": 40}

# chai_menu["elaichi"]   #here we get Key Error due to these type of errors program get crash which mean below code were not executed. 

# print("Hello developers")  #It will never run because above we get key error. 


# We use try and except to handle these types of errors: 

try: 
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")

print("Hello developers!")