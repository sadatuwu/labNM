def f(x):
    return x*x*x -x - 1

def main():
    a,b,e = 1,2,0.0001
    while (b-a)/2 > e:
        m = (a+b)/2
        print(a,b,m,f(m))
        if(f(m)==0):
            print(m,"is the root")
            return 
        elif(f(a)*f(m) < 0):
            b = m
        elif(f(m)*f(b)< 0):
            a = m
    
    print("aproximate root : ", (a+b)/2)
        
main()