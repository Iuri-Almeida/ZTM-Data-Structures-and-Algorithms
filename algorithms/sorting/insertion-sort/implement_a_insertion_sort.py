# O(n²) - Time Complexity
# O(1) - Space Complexity
def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        if arr[i] <= arr[0]:
            aux = arr[i]
            for k in range(i, 0, -1):
                arr[k] = arr[k - 1]
            arr[0] = aux
        else:
            pos = i
            for j in range(i - 1, -1, -1):
                if arr[pos] > arr[j]:
                    break
                aux = arr[pos]
                arr[pos] = arr[j]
                arr[j] = aux
                pos -= 1


# O(n²) - Time Complexity
# O(1) - Space Complexity
def insertion_sort_02(arr):
    for i in range(1, len(arr)):
        num, j = arr[i], i - 1
        while j >= 0 and num < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertion_sort_02(array)
print(array)
