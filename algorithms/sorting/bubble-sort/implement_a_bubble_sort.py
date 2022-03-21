# O(n²) - Time Complexity
# O(1) - Space Complexity
def bubble_sort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = aux


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubble_sort(array)
print(array)
