class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr__(self):
        node = self.first
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise ReferenceError("Queue already empty! You can't remove from nothing.")

        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1

    def is_empty(self):
        return self.first is None and self.last is None and self.length == 0


my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue("Brad")
my_queue.enqueue("John")
my_queue.enqueue("Samantha")
print(my_queue)
print(my_queue.peek())
print(my_queue.first)
print(my_queue.last)
print(my_queue.length)
print("-" * 20)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
print(my_queue.first)
print(my_queue.last)
print(my_queue.length)
print("-" * 20)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
print(my_queue.first)
print(my_queue.last)
print(my_queue.length)
print("-" * 20)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
print(my_queue.first)
print(my_queue.last)
print(my_queue.length)
