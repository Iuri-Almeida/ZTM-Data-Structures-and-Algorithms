# O(n) - Time Complexity
# O(n) - Space Complexity
def find_factorial_recursive(n):
    if n == 0:
        return 1
    return n * find_factorial_recursive(n - 1)


# O(n) - Time Complexity
# O(1) - Space Complexity
def find_factorial_iterative(n):
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
    return fat


print(find_factorial_recursive(3))
print(find_factorial_iterative(3))
