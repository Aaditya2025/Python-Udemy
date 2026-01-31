# Gnerators: 
# 1.You save memory
# 2. You don't want result immedietely
# 3. Lazy evaluation  ; These are things we get by using generators and it also uses a keyword called 'yield'. 


def serve_chai():
    yield "Cup 1: Masala chai "
    yield "Cup 2: Ginger chai " 
    yield "Cup 3: Elaichi chai "

stall = serve_chai() 

for cup in stall: 
    print(cup)


def get_chai_list(): 
    return ["Cup 1", "Cup 2", "Cup 3"]

#generator function: 
def get_chai_gen(): 
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(chai)  #Here we do not get the result because chai just pointing reference the generator func. 

print(next(chai))  #This is the way we get result we have to use next method. 
print(next(chai))
print(next(chai))
# print(next(chai))