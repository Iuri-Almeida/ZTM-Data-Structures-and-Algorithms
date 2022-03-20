class Queue:
    def __init__(self):
        self.array = []

    def __repr__(self):
        return " -- ".join(self.array)

    def __unshift(self):
        for i in range(len(self.array) - 1):
            self.array[i] = self.array[i + 1]

    def peek(self):
        return self.array[0] if not self.is_empty() else None

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        self.__unshift()
        self.array.pop()

    def is_empty(self):
        return not self.array


my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue("Brad")
my_queue.enqueue("John")
my_queue.enqueue("Samantha")
print(my_queue)
print(my_queue.peek())
print("-" * 20)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
print("-" * 20)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
print("-" * 20)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
