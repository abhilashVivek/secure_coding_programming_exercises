# write a recursive function to calculate the factorial


def factorial(n):
    """
    input: 
        n: int
    returns: 
        factorial of n
    
    reminder: factorial 8! is
    8*7*6*5*4*3*2*1
    """
    product = 1
    counter = n
    while counter > 0:
        product = product * (counter)
        counter -= 1
    print(f"factorial {n}! is {product}")
    
factorial(10)