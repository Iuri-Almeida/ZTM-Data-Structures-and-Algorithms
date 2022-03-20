class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class MyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.length == 1:
            raise PermissionError("You can't delete the head.")
        node = self.__traverse_to_index(self.length - 2)
        node.next = None
        self.tail = node
        self.length -= 1

    def get(self, index):
        if index >= self.length:
            raise IndexError("Linked List index out of range")

        return self.__traverse_to_index(index).data

    def __traverse_to_index(self, index):
        i = 0
        node = self.head
        while i != index:
            node = node.next
            i += 1
        return node

    def insert(self, value, index):
        if index >= self.length:
            return self.append(value)

        node = self.__traverse_to_index(index - 1)
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        self.length += 1

    def delete(self, index):
        if index >= self.length:
            return self.pop()

        node = self.__traverse_to_index(index - 1)
        node.next = node.next.next
        self.length -= 1


my_linked_list = MyLinkedList(10)
my_linked_list.append(5)
my_linked_list.prepend(16)
my_linked_list.insert(3, 1)
print(my_linked_list)
print(my_linked_list.get(1))
my_linked_list.delete(2)
print(my_linked_list)
print(my_linked_list.tail.data)
my_linked_list.insert(200, 99999)
print(my_linked_list)
print(my_linked_list.tail.data)
my_linked_list.delete(9999992828)
print(my_linked_list)
print(my_linked_list.tail.data)
my_linked_list.pop()
print(my_linked_list)
print(my_linked_list.tail.data)
