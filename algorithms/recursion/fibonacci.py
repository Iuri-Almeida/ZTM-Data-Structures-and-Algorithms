# O(2^n) - Time Complexity
def fibonacci_recursive(n):
    n = abs(n)
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# O(n) - Time Complexity
def fibonacci_iterative_for(n):
    n = abs(n)
    if n < 2:
        return n

    n1 = 0
    n2 = 1
    n3 = 0
    for _ in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3


# O(n) - Time Complexity
def fibonacci_iterative_for_list(n):
    n = abs(n)
    if n < 2:
        return n

    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


# O(n) - Time Complexity
def fibonacci_iterative_while(n):
    n = abs(n)
    if n < 2:
        return n

    n1 = 0
    n2 = 1
    n3 = 0
    i = 2
    while i < n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1
    return n3


# O(n) - Time Complexity
def fibonacci_iterative_while_list(n):
    n = abs(n)
    if n < 2:
        return n

    fib = [0, 1]
    i = 2
    while i < n:
        fib.append(fib[-1] + fib[-2])
        i += 1
    return fib[-1]


print(fibonacci_recursive(1))
print(fibonacci_iterative_for(1))
print(fibonacci_iterative_for_list(1))
print(fibonacci_iterative_while(1))
print(fibonacci_iterative_while_list(1))
