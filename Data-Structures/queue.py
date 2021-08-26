"""
A queue is a single dimension structure that's used to store n elements, a queue is working in the
First-in, First-out (FIFO) approach, when an element is added to the rear of the queue, it's said
to be an enqueueing operation, when an element is removed from the front of the queue, it's said to be a
a dequeueing operation ... 

"""

# Implementation of a Queue using a class

class Queue:
      def __init__(self):
      	   self.items = []

      def enqueue(self, item):
      	   self.items.append(item)

      def dequeue(self):
      	   self.items.pop(0)

      def size(self):
      	   return len(self.items)

      def peek(self):
      	   return self.items[-1]

      def is_empty(self):
      	   return self.items == []


# Defining our Queue

my_queue = Queue()

# Adding three elements to our Queue using an enqueueing operation:

my_queue.enqueue('First')
my_queue.enqueue('Second')
my_queue.enqueue('Third')

print(my_queue.items)

# Removing the tree elements using a dequeueing operation (FIFO) Approach:

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()      

print(my_queue.items)

# Checking if our Queue is empty:

print(my_queue.is_empty()) # it will return True, our Queue is empty