
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1
    
    M = [None] * (n+1)
    
    M[0] = 0
    M[1] = 1

    for i in range(2, n+1):
        M[i] = M[i-1] + M[i-2]

    return M




def main():
    #n:                 0   1   2   3   4   5   6   7   8   9   10
    #nth Fibonacci #:   0   1   1   2   3   5   8   13  21  34  55
    print(fibonacci_recursive(100))

    print(fibonacci_iterative(100))

if __name__ == "__main__":
    main()