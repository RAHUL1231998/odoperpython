def fib1(n):
    a,b=0,1
    ls=[]
    for i in range(0,n):
        a,b=b,a+b
        ls.append(a)
    return ls



   
print(fib1(10))
