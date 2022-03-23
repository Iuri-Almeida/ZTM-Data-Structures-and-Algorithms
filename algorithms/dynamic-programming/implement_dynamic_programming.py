cache = {}
calc_1 = calc_2 = 0


# O(2^n) - Time Complexity
# Smaller Space Complexity
def fibonacci(n):
    global calc_1
    calc_1 += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# O(n) - Time Complexity
# Bigger Space Complexity (Was worth it?)
def fibonacci_dynamic_programming(n):
    global cache, calc_2
    calc_2 += 1

    if n in cache.keys():
        return cache[n]

    if n < 2:
        return n
    cache[n] = fibonacci_dynamic_programming(n - 1) + fibonacci_dynamic_programming(n - 2)

    return cache[n]


print(fibonacci(30))
print(f"Calc_1: {calc_1}")
print(fibonacci_dynamic_programming(30))
print(f"Calc_2: {calc_2}")
