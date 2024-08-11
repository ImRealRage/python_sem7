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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Example usage:
print("----------Linked List Implementation----------")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete(2)
ll.print_list()  # Output: 0 -> 1 -> 3 -> None

ll.delete(0)
ll.print_list()  # Output: 1 -> 3 -> None

ll.delete(3)
ll.print_list()  # Output: 1 -> None

print("---------- Implementation Over----------")


## Implementing Doubly Linked List in Python


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.data == key and curr_node == self.head:
                if not curr_node.next:
                    curr_node = None
                    self.head = None
                    return
                else:
                    next_node = curr_node.next
                    next_node.prev = None
                    curr_node.next = None
                    curr_node = None
                    self.head = next_node
                    return

            elif curr_node.data == key:
                if curr_node.next:
                    next_node = curr_node.next
                    prev_node = curr_node.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    curr_node.next = None
                    curr_node.prev = None
                    curr_node = None
                    return
                else:
                    prev_node = curr_node.prev
                    prev_node.next = None
                    curr_node.prev = None
                    curr_node = None
                    return
            curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# Example usage

print("----------Doubly Linked List Implementation----------")
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.print_list()  # Output: 1 2 3
dll.prepend(0)
dll.print_list()  # Output: 0 1 2 3
dll.delete(2)
dll.print_list()  # Output: 0 1 3
dll.delete(3)
dll.print_list()  # Output: 0 1

## This one is not pushed to my private repo

print("---------- Implementation Over----------")
