# Google Question

# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array = [2, 3, 4, 5]
# It should return undefined


# input:
#   array - always an array of integers
#       negative and positive
#       no size limit
#       can be empty or None

# output:
#   integer
#       find the first recurring element
#       if not -> None


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def first_recurring_character(arr):
    smaller_index_diff = len(arr) - 1
    element = None
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and (j - i) < smaller_index_diff:
                smaller_index_diff = j - i
                element = arr[i]
    return element


print(first_recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]))


# O(n) - Time Complexity
# O(n) - Space Complexity
def first_recurring_character2(arr):
    my_map = {}
    for i in range(len(arr)):
        if arr[i] in my_map.keys():
            return arr[i]
        else:
            my_map[arr[i]] = i
    return None


# print(first_recurring_character2([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
