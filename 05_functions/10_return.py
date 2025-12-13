# There are three things functions may return: 
# 1. Nothing: imlicitly return None.  2. One Value, 3. Mulitple Value 
# 4. Early from function: Once the function returns anything then  after that lines of code are not executed. 

def make_chai(): 
    # return "Here is your masala chai" 
    print(f"Here is your masala chai")

return_value = make_chai()

print(make_chai())


def idle_chaiwala(): 
    pass

print(return_value)   #It will return None. 

def sold_cups(): 
    return 120

total = sold_cups
print(total)

def chai_status(cups_left): 
    if cups_left == 0: 
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100, 20, 10 #sold ,remaining

sold, remaining, not_paid = chai_report()  #'not_paid or _' need to use because the function return more than 2 values. 

print("Sold:", sold)
print("Remaining:", remaining)