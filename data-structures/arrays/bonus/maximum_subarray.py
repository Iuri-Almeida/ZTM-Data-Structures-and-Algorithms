# input:
#   array
#       items always int
#       not size limit
#       not sorted
#       can have negative and positive integers
#       can be null
#       always an array

# subarrys must be in order

# output:
#   integer
#       largest sum of subarrays
#       if did not find the largest sum -> []


def maximum_subarray(nums):  # Time Limit Exceeded
    if nums is None or not nums:
        return []
    largest_sum = None
    # loop over the arr
    for i in range(len(nums)):
        # get the element
        cur_element_sum = nums[i]
        # check if the element alone is the largest sum -> largest_sum = element
        if largest_sum is None or cur_element_sum > largest_sum:
            largest_sum = cur_element_sum
        # loop over other elements
        for j in range(i + 1, len(nums)):
            # create sub_arrays
            sub_array = nums[i:j + 1]
            sub_array_sum = sum(sub_array)
            # check if the sum of sub_arrays are the largest sum -> largest_sum = sum(sub_arrays)
            if sub_array_sum > largest_sum:
                largest_sum = sub_array_sum
    return largest_sum


# print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maximum_subarray2(nums):  # Time Limit Exceeded
    s = None
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            cur_sum = sum(nums[i:j + 1])
            if s is None or cur_sum > s:
                s = cur_sum
    return s


# print(maximum_subarray2([-2, -1]))

# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maximum_subarray3(nums):
    if nums is None or not nums:
        return 0
    max_subarray = nums[0]
    cur_sum = 0
    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num
        max_subarray = max(max_subarray, cur_sum)
    return max_subarray


print(maximum_subarray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
