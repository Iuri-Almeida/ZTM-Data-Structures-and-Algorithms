from random import randint


# https://realpython.com/sorting-algorithms-python/#implementing-quicksort-in-python
def quick_sort(arr, pivot=None):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = arr[randint(0, len(arr) - 1)] if pivot is None else pivot

    for item in arr:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quick_sort(low) + same + quick_sort(high)


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(array))
