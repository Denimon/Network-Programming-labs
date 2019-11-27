

def fibnonacci(num):
    a,b = 0,1
    while a < num:
        yield a
        a,b = b, a+b
    
        

for i in fibnonacci(1000000):
    print(i)