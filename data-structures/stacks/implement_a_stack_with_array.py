class Stack:
    def __init__(self):
        self.array = []

    def __repr__(self):
        return " -- ".join(self.array)

    def peek(self):
        return self.array[-1] if not self.is_empty() else None

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.is_empty():
            raise ReferenceError("Stack already empty! You can't remove from nothing.")

        self.array.pop()

    def is_empty(self):
        return not self.array


my_stack = Stack()
print(my_stack.is_empty())
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(my_stack)
print(my_stack.peek())
print("-" * 20)
my_stack.pop()
print(my_stack)
print(my_stack.peek())
print("-" * 20)
my_stack.pop()
print(my_stack)
print(my_stack.peek())
print("-" * 20)
my_stack.pop()
print(my_stack)
print(my_stack.peek())
print(my_stack.is_empty())
