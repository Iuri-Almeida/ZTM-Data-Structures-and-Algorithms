# O(n²) - Time Complexity
# O(1) - Space Complexity
def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        pos = i
        for j in range(i + 1, length):
            if arr[j] < arr[pos]:
                pos = j
        aux = arr[i]
        arr[i] = arr[pos]
        arr[pos] = aux


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection_sort(array)
print(array)
