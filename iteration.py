
def f(x):
    return 1/ ((x+1)**.5)

def main():

    xn, e= 0.5,  1e-4
    while True:
        xn1 = f(xn)
        print(xn,xn1, abs(xn1-xn))
        if(abs(xn1 - xn)<e):
            print("aprox root is",xn1)
            return 
        xn = xn1









    
        
main()