class MyArray:
    def __init__(self):
        self.__length = 0
        self.__data = {}

    def __str__(self):
        return f"MyArray - length: {self.__length}, data: {self.__data}"

    def get(self, index):
        return self.__data[index]

    def push(self, item):
        self.__data[self.__length] = item
        self.__length += 1
        return self.__length

    def pop(self):
        last_item = self.__data[self.__length - 1]
        del self.__data[self.__length - 1]
        self.__length -= 1
        return last_item

    def delete(self, index):
        item = self.__data[index]
        self.__shift_items(index)
        return item

    def __shift_items(self, index):
        for i in range(index, self.__length - 1):
            self.__data[i] = self.__data[i + 1]
        del self.__data[self.__length - 1]
        self.__length -= 1


arr = MyArray()

arr.push('hi')
arr.push('you')
arr.push('!')
arr.delete(1)
arr.push('Are')
arr.push('having')
arr.push('a')
arr.push('good')
arr.push('day')
arr.push('?')
arr.delete(1)
print(arr)
