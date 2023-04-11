def fibonacci(n):
    """Return the nth value in the Fibonacci series.

    n : The index of the Fibonacci number to be returned.
    
    Returns:
    int: The nth value in the Fibonacci series.
    """
    if n==0:
        return n
    elif n==1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
    

def lucas(n):
    """Return the nth value in the Lucas numbers.

    Parameters:
    n : The index of the Lucas number to be returned.
    
    Returns:
    int: The nth value in the Lucas numbers.
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    return lucas(n-2) + lucas(n-1)

def sum_series(n,c0=0,c1=1):
    
    """Return the nth value in a series determined by the starting values c0 and c1.
    Parameters:
    n : The index of the value to be returned.
    c0 : The first value  (default=0).
    c1 : The second value  (default=1).
    
    Returns:
    int: The nth value in the specified series.
    """
   
    if (c0==0 and c1==1):
        return fibonacci(n)
    elif (c0==2 and c1==1):
        return lucas(n)
       
    elif n == 0:
        return c0
    elif n == 1:
        return c1
    else:
        return sum_series(n-2, c0, c1) + sum_series(n-1, c0, c1)
       

