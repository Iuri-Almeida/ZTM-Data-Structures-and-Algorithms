# Implement a function that reverses a string using iteration...and then recursion!

# O(n) - Time Complexity
def reverse_string(s):
    return s[-1::-1]


# O(n) - Time Complexity
def reverse_string_iterative_for(s):
    reversed_word = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_word += s[i]
    return reversed_word


# O(n) - Time Complexity
def reverse_string_iterative_while(s):
    reversed_word = ""
    i = len(s) - 1
    while i >= 0:
        reversed_word += s[i]
        i -= 1
    return reversed_word


# O(n) - Time Complexity
def reverse_string_recursive(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])


print(reverse_string('yoyo mastery'))
print(reverse_string_iterative_for('yoyo mastery'))
print(reverse_string_iterative_while('yoyo mastery'))
print(reverse_string_recursive('yoyo mastery'))
# should return: 'yretsam oyoy'
