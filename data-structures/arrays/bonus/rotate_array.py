# inputs:
#   array - anything
#       not sorted
#       can be empty
#       can be None
#       no interval for items
#       no size limit
#   int - non-negative
#       can be 0

# output:
#   array - anything
#       if empty or None return empty array
#       rotated array based on int param


# O(n * m) - Time Complexity
# O(1) - Space Complexity
def rotate_array(nums, k):  # Time Limit Exceeded
    if len(nums) == 1:
        return nums
    # loop k times
    for _ in range(k):  # O(n)
        # pop last item
        pop_item = nums.pop()
        # insert on first position
        nums.insert(0, pop_item)  # O(m)
    return nums


# print(rotate_array([-1, -100, 3, 99], 2))


# O(1) - Time Complexity
# O(1) - Space Complexity
def rotate_array2(nums, k):  # if we just have to return the array modified
    if len(nums) == 1:
        return nums
    # last k items (array)
    last_k_items = nums[-k:]
    # [last_k_item_array] unify [nums_array_without_last_k_item]
    nums_without_last_k_items = nums[:len(nums) - k]
    return last_k_items + nums_without_last_k_items


# print(rotate_array2([1, 2, 3, 4, 5, 6, 7], 3))


def rotate_array3(nums, k):  # Time Limit Exceeded
    for _ in range(k):
        # get the last item
        last_item = nums[-1]
        # shift to the right
        aux = nums[0]
        for i in range(len(nums) - 1):
            aux_2 = nums[i + 1]
            nums[i + 1] = aux
            aux = aux_2
        # add the last item on the first position
        nums[0] = last_item
    print(nums)


# rotate_array3([1, 2, 3, 4, 5, 6, 7], 3)


# O(n) - Time Complexity
# O(n) - Space Complexity
def rotate_array4(nums, k):
    k = k % len(nums)
    # create new arr
    new_arr = []
    # add last k items on new arr
    for i in range(k):
        new_arr.append(nums[-k + i])
    # add the other items on the new arr
    for j in range(len(nums) - k):
        new_arr.append(nums[j])
    # copy every item to the older one
    for m in range(len(new_arr)):
        nums[m] = new_arr[m]
    print(nums)


rotate_array4([1, 2, 3, 4, 5, 6, 7], 3)


def do_rotation(left, right, arr):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left, right = left + 1, right - 1


# O(n) - Time Complexity
# O(1) - Space Complexity
def rotate_array5(nums, k):
    k = k % len(nums)
    do_rotation(0, len(nums) - 1, nums)
    do_rotation(0, k - 1, nums)
    do_rotation(k, len(nums) - 1, nums)
    print(nums)


# rotate_array5([1, 2, 3, 4, 5, 6, 7], 3)
