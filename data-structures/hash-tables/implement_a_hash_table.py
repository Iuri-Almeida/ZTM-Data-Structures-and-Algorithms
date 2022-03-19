from typing import Optional


class HashTable:
    def __init__(self, size):
        self.__data: Optional[list] = [None] * size

    def __hash(self, key):
        h = 0
        for i in range(len(key)):
            h = (h + ord(key[i]) * i) % len(self.__data)
        return h

    def set(self, key, value):
        address = self.__hash(key)
        if self.__data[address] is None:
            self.__data[address] = []
        self.__data[address].append([key, value])

    def get(self, key):
        address = self.__hash(key)
        memory_list = self.__data[address]
        if memory_list is not None:
            for item in memory_list:
                if item[0] == key:
                    return item[1]
        return None

    def keys(self):
        keys = []
        for i in self.__data:
            if i is not None:
                for j in i:
                    keys.append(j[0])
        return keys

    def values(self):
        values = []
        for i in self.__data:
            if i is not None:
                for j in i:
                    values.append(j[1])
        return values


hash_table = HashTable(50)
hash_table.set("grapes", 1000)
hash_table.set("apples", 10)
hash_table.set("oranges", 7)
hash_table.set("banana", 9929)
hash_table.set("pineapple", 3)
print(hash_table.get("grapes"))
print(hash_table.keys())
print(hash_table.values())
