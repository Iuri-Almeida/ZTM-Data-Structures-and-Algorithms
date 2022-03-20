class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __repr__(self):
        node = self.top
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)

    def peek(self):
        return self.top.data if self.top is not None else self.top

    def pop(self):
        if self.is_empty():
            raise ReferenceError("Stack already empty! You can't remove from nothing.")

        if self.bottom == self.top:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.bottom = self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def is_empty(self):
        return self.top is None and self.bottom is None and self.length == 0


my_stack = Stack()
print(my_stack.is_empty())
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(my_stack)
# print(my_stack.peek())
# print(my_stack.top.data)
# print(my_stack.bottom.data)
# print(my_stack.length)
print("-" * 20)
my_stack.pop()
print(my_stack)
# print(my_stack.peek())
# print(my_stack.top.data)
# print(my_stack.bottom.data)
# print(my_stack.length)
print("-" * 20)
my_stack.pop()
print(my_stack)
# print(my_stack.peek())
# print(my_stack.top.data)
# print(my_stack.bottom.data)
# print(my_stack.length)
print("-" * 20)
my_stack.pop()
print(my_stack)
# print(my_stack.peek())
print(my_stack.is_empty())
