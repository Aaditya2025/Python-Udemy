def local_chai(): 
    yield "Masala Chai"
    yield "Ginger Chai" 

def imported_chai(): 
    yield "Matcha" 
    yield "Oolong" 

def full_menu(): 
    yield from local_chai() 
    yield from imported_chai() 

for chai in full_menu(): 
    print(chai) 

def chai_stall():
    try: 
        while True: 
            order = yield "Waiting for chai order" 
    except: 
        print("Stall Closed, No more chai")

stall = chai_stall() 
print(next(stall))
stall.close()   #This is not only close the generators it also cleaup your memory. 

"""
NOTES:

1.Yield: It is responsible for converting any function into generators. yield produces values one at a time and pauses the function, saving memory and state.

2.next(): It is used to manually getting the value which generators gives. 

3.send(): It is used to send data to generators. 

4.yield from: yield from is used to delegate yielding to another iterable or generator.

5.close(): It stop the generators. 
"""