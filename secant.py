def f(x):
    return x*x*x -2*x - 5
def df(x):
    return 3*x*x- 2

def main():
    xn,e = 2,0.0001

    while True:
        xn1 = xn - (f(xn)/df(xn))
        print(xn, f(xn), abs(xn1-xn))
        if(abs(xn1-xn)<e):
            print("aprox root:", xn1)
            return 
        xn = xn1


main()