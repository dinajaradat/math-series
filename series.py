def fibonacci(n):
    if n==0:
        return n
    elif n==1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
    

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    return lucas(n-2) + lucas(n-1)

def sum_series(n,c0=0,c1=1):
   
    if (c0==0 and c1==1):
        return fibonacci(n)
       
    else :
        return lucas(n)
       