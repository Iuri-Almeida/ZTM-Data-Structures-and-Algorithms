# input:
#   array - always integer items
#       can be empty
#       can have negative and positive numbers
#       no interval
#       no size limit
#       0's can be together or not

# output:
#   array - always integer items
#       can be empty
#       can have negative and positive numbers
#       0's must be at the end of the array

# NOTE: cannot make a copy of the array


# O(n) - Time Complexity
# O(1) - Space Complexity
def move_zeroes(nums):
    # nums is None or empty
    if nums is None or not nums:
        return []
    # contains 0's
    if 0 not in nums:
        return nums

    i = 0
    number_of_non_0_elements = len(nums) - nums.count(0)
    # loop over the arr
    while i < number_of_non_0_elements:
        # check n == 0 -> remove -> push
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
        else:
            i += 1
    # at the end -> nums
    return nums


# print(move_zeroes([0, 1, 0, 2, 0]))


# O(n) - Time Complexity
# O(1) - Space Complexity
def move_zeroes2(nums):
    # nums is None or empty
    if nums is None or not nums:
        return []

    count_zeroes = 0
    # while 0 in arr
    while 0 in nums:
        # remove 0
        nums.remove(0)
        # count how many 0's are going to be removed
        count_zeroes += 1
    # append how many times 0 was removed
    for _ in range(count_zeroes):
        nums.append(0)
    return nums


print(move_zeroes2([1, 1, 2, 3, 4, 5, 6]))
