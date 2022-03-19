# inputs:
#   array - integers
#   target - integer
#   array item's always int
#   target is always an int
#   no size limit
#   arr can be empty
#   input always (array, int)

# output:
#   array - integer (indices)


# O(n²) - Time Complexity
# O(1) - Space Complexity
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


# print(two_sum([0, 0, 1, 5, 4, 6], 1))


# O(n) - Time Complexity
# O(n) - Space Complexity
def two_sum2(arr, target):
    if not arr or type(arr) != list or type(target) != int:
        return []

    # loop over the arr
    for pos in range(len(arr) - 1):
        # result = get the difference between target and element
        result = target - arr[pos]

        # other elements of the list
        elements_on_right = arr[pos + 1:]

        # check if result is on the rest of the list -> return [p1, p2]
        if result in elements_on_right:
            length_of_elements_on_left = pos + 1
            sum_target = elements_on_right.index(result) + length_of_elements_on_left
            return [pos, sum_target]
    return []


print(two_sum2([1, 0, 3, 1], 4))
