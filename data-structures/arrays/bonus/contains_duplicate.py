# input:
#   array - always an integer array
#       can have negative and positive elements
#       array can be null
#       no size limit
#       not sorted
#       no interval

# output:
#   boolean - always
#       true -> ANY value appears AT LEAST TWICE
#       false -> everything else


# O(n²) - Time Complexity
# O(1) - Space Complexity
def contains_duplicate(nums):
    if nums is None:
        return 'Not so good input'

    # first loop over the array
    for i in range(len(nums)):
        # second loop over the array
        for j in range(i + 1, len(nums)):
            # check if previous element == next one -> true
            if nums[i] == nums[j]:
                return True
    # at the end of the loop -> false
    return False


# print(contains_duplicate([5, 1, 7, 0, 9, 8, 3, 6, 4, 2]))


# O(n) - Time Complexity
# O(n) - Space Complexity
def contains_duplicate2(nums):
    if nums is None:
        return 'Not so good input'

    # loop over the array
    for i in range(len(nums) - 1):
        # get the element
        num = nums[i]
        # check if this element is on the rest of the array -> True
        if num in nums[i + 1:]:
            return True
    # when the loops ends -> False
    return False


# print(contains_duplicate2([1, 2, 3, 1]))


# O(1) - Time Complexity
# O(n) - Space Complexity
def contains_duplicate3(nums):
    if nums is None:
        return 'Not so good input'
    return len(set(nums)) != len(nums)


print(contains_duplicate3([1, 2, 3, 1]))
