def print_fibonacci(n):
    if n <= 1:
        return n
    last = print_fibonacci(n - 1)
    second_last = print_fibonacci(n - 2)
    return last + second_last
# Driver code
N = 4
print(print_fibonacci(N))  # Output: 3

##now the iterative way to do it, preferable in production code because of better time and space complexity
def print_fibonacci(n):
    if n == 0:
        return 0
    else:
        second_last = 0
        last = 1
        print(f"The Fibonacci Series up to {n}th term:")
        print(f"{second_last} {last}", end=" ")
        for i in range(2,n+1): #n+1 because we want to include the nth term as well
            current = last + second_last
            print(current, end=" ")
            second_last = last
            last = current
# Driver code
N = 4
print_fibonacci(N)  # Output: 0 1 1 2 3            
