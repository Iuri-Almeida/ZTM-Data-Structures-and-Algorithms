# O(n²) - Time Complexity
# O(1) - Space Complexity
def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        if arr[i] <= arr[0]:
            arr.insert(0, arr.pop(i))
        else:
            for j in range(i - 1, -1, -1):
                if arr[i] > arr[j]:
                    arr.insert(j + 1, arr.pop(i))
                    break


array = [0, 1, 2, 3, 5, 4, 6]
insertion_sort(array)
print(array)
