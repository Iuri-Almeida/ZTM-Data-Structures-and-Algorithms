class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return self.data


class DoublyLinkedList:
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
        return " <--> ".join(nodes)

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.length == 1:
            raise PermissionError("You can't delete the head.")

        node = self.__traverse_to_index_head_2_tail(self.length - 2)
        node.next = None
        self.tail = node
        self.length -= 1

    def __traverse_to_index_head_2_tail(self, index):
        i = 0
        node = self.head
        while i != index:
            node = node.next
            i += 1
        return node

    def get(self, index):
        if index >= self.length:
            raise IndexError("Linked List index out of range")

        return self.__traverse_to_index_head_2_tail(index).data

    def insert(self, value, index):
        if index >= self.length:
            return self.append(value)

        node = self.__traverse_to_index_head_2_tail(index - 1)
        new_node = Node(value)
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node
        self.length += 1

    def delete(self, index):
        if index >= self.length - 1:
            return self.pop()

        node = self.__traverse_to_index_head_2_tail(index - 1)
        node.next = node.next.next
        node.next.prev = node
        self.length -= 1


my_linked_list = DoublyLinkedList(10)
my_linked_list.append(5)
my_linked_list.prepend(16)
my_linked_list.insert(3, 1)
print(my_linked_list)
print(my_linked_list.get(1))
my_linked_list.delete(2)
print(my_linked_list)
print(my_linked_list.tail.data)
my_linked_list.insert(200, 4)
print(my_linked_list)
print(my_linked_list.tail.data)
my_linked_list.delete(9999992828)
print(my_linked_list)
print(my_linked_list.tail.data)
