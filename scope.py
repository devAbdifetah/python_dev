a = [2,4,8]

def function1():

    global a
    a[1] = 100 
    print(a)

def function2():
     b = 200
     print(b)

function1()
function2()
print(a)     

    
