# wrtie a recursive fibonacci function


def fib(n):
    """
    input: 
        n: int

    return:
        fibbonacci number for n
    """
    fibonacci_seq = [0,1]
    
    
    for i in range (n-2):
        current_index = len(fibonacci_seq)
        fibonacci_seq.append((fibonacci_seq[current_index-1])+(fibonacci_seq[current_index-2]))
        
    print(fibonacci_seq[len(fibonacci_seq)-1])
        

fib(10)

# fib(6) should return 5
# fib(10) should return 34
