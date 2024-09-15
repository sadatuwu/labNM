def f(x):
    return x*x*x -2*x - 5


def main():
    x0, x1, e = 3,16, 0.0001

    while True:
        
        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
        print(x0, x1, x2)
        if(abs(x2-x1)<e):
            print("aprox root:", x2)
            return 
        x0=x1
        x1 = x2


main()