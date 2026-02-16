

'''
Use Python's      collections.deque to implement a more efficient queue.
Instructions:
Implement a class      DequeQueue with the following methods:
enqueue(item): Adds an item to the end of the queue.
dequeue(): Removes and returns the item at the front of the queue. If the queue is empty, it should raise an exception.
is_empty(): Returns True if the queue is empty, False otherwise.
size(): Returns the number of items in the queue.
Write a few test cases to demonstrate the functionality of the queue.
'''
from asyncio import Queue
from collections import deque

# I need to create a class called 'DequeQueue' .
class DequeQueue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        # You utilize this to add items to the end
        self.items.append(item)

    def dequeue(self):
        # we're trying to remove items from the front of the queue
        if self.is_empty():
            raise Exception("Queue is empty")
        # this will remove the first item from the queue
        return self.items.popleft()

    def is_empty(self):
        #check if the list is empty
        return len(self.items) == 0

    def size(self):
        # check what's the length of the queue
        return len(self.items)


queue = DequeQueue()

print("Is the queue empty?:", queue.is_empty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Is the queue empty?:", queue.is_empty())
print("Size of queue:", queue.size())

print("Dequeued item:", queue.dequeue())
print("Size of queue:", queue.size())
