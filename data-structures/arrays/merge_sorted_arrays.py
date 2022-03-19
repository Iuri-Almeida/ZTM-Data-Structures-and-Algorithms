# inputs:
#     2 arrays
#     array elements always integers
#     no size limit
#     sorted

# output:
#     sorted arr of intergers


def merge_sorted_arrays(arr1, arr2):
    if (not arr1 and not arr2) or type(arr1) != list or type(arr2) != list:
        return 'Not so good inputs'
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    return sorted(arr1 + arr2)


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
