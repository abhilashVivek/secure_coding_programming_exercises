## DEBUG THIS CODE


def h_fact(n):  
    if n == 1:
        return 1
    else:
        return n * h_fact(n - 1)


print(h_fact(10))
