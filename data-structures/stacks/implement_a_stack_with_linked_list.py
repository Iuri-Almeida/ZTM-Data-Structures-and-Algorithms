class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __traverse_to_index(self, index):
        i = 0
        node = self.bottom
        while i != index:
            node = node.next
            i += 1
        return node

    def peek(self):
        return self.top.data if self.top is not None else self.top

    def pop(self):
        if self.length == 1:
            self.top = self.bottom = None
        else:
            node = self.__traverse_to_index(self.length - 2)
            node.next = None
            self.top = node
        self.length -= 1

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.bottom = new_node
        else:
            self.top.next = new_node
        self.top = new_node
        self.length += 1

    def is_empty(self):
        return self.top is None and self.bottom is None and self.length == 0


my_stack = Stack()
print(my_stack.is_empty())
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
print(my_stack.top.data)
print(my_stack.bottom.data)
print(my_stack.length)
print("-" * 20)
my_stack.pop()
print(my_stack.peek())
print(my_stack.top.data)
print(my_stack.bottom.data)
print(my_stack.length)
print("-" * 20)
my_stack.pop()
print(my_stack.peek())
print(my_stack.is_empty())
