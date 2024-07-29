## Implementing Stack in Python


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Underflow detected")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Underflow detected")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Use stack from our class

print("----------Stack Implementation----------")

stack = Stack()

iterable = [1, 2, 3, 4, 5]

for item in iterable:
    stack.push(item)

print("Stack after pushing:", stack)

stack.pop()

print("Stack after popping:", stack)

print("Top element:", stack.peek())

print("Size of the stack:", stack.size())

while not stack.is_empty():
    print("Popped element:", stack.pop())

print("Is the stack empty?", stack.is_empty())

print("---------- Implementation Over----------")


## Implementing Queue in Python


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Underflow detected")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Underflow detected")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Queue usage:

print("----------Queue Implementation----------")
queue = Queue()
iterable = [1, 2, 3, 4, 5]

for item in iterable:
    queue.enqueue(item)

print("Queue after enqueuing:", queue)

print("Dequeued element:", queue.dequeue())

print("Queue after dequeuing:", queue)

print("Front element:", queue.front())

print("Size of the queue:", queue.size())

while not queue.size() == 0:
    print("Dequeued element:", queue.dequeue())

print("Is the queue empty?", queue.is_empty())

print("---------- Implementation Over----------")


## Implementing Linked List in Python
