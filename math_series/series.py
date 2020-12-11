# The name of fibonacci Function should have one paramenter (n) and return the nth value in the fibonacci series.
# The name of lucas Function that returns the nth value in the lucas numbers again

# The name of sum_series Function with one required parameter and two optinoal paramenters.
# The required parameter will determine which element in the series to print.
#The two optional parameters will have default value of 0 and 1, and will determine the first two values for the series to be produce.  

def fibonacci(n):

    a = 0
    b = 1

    if n == 1:
        return(a)

    else:
    # return(a)
    # return(b)

        for i in range(n):
            c = a + b
            a = b
            b = c
        return(c)

# fibonacci(10)        

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

# lucas(10)
  
def sum_series(n, x=0, y=1):
    if x == 0 and y == 1:
        if n - 1 == 0:
             return x
        if n - 1 == 1:
             return y
        return sum_series(n-1, x, y) + sum_series(n-2, x,y)
    else:
        if n ==0:
            return x
        if n == 1:
            return y
        return sum_series(n-1, x, y) + sum_series(n-2, x, y)              
    
# sum_series(10)





    