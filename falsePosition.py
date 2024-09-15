
def f(x):
    return x*x*x -2*x - 5

def main():

    a,b,e = 2,3,0.0001
    while (b-a) >= e:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        print(a,b,c,f(c))
        if(abs(f(c))<e):
            print(c,"is the root")
            return 
        elif(f(a)*f(c) < 0):
            b = c   
        else:
            a = c
    
    print("aproximate root : ", (a*f(b)-b*f(a))/(f(b)-f(a)))
        
main()