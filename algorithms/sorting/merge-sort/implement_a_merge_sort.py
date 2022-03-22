def merge(left, right):
    aux_arr = []
    left_length = len(left)
    right_length = len(right)
    pos_left = pos_right = 0
    while pos_left < left_length and pos_right < right_length:
        if left[pos_left] < right[pos_right]:
            aux_arr.append(left[pos_left])
            pos_left += 1
        else:
            aux_arr.append(right[pos_right])
            pos_right += 1
    return aux_arr + left[pos_left:] + right[pos_right:]


# O(nlog n) - Time Complexity
# O(n) - Space Complexity
def merge_sort(arr):
    if arr is None or not arr:
        return None

    length = len(arr)
    if length == 1:
        return arr

    middle = int(length / 2)

    left_arr = arr[:middle]
    right_arr = arr[middle:]

    return merge(merge_sort(left_arr), merge_sort(right_arr))


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(array))
