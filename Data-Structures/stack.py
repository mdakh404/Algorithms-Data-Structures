"""
A stack is a single dimension structure that's used to store and organize data, stack can be created in
either First-in, Last-out (FILO) or Last-in, Fist-out (LIFO) approaches, common stack operations are:

- push, pop, is_empty, peek, size etc...

Analysing of time complexity of the above operations using Big O notation will result in the following:

* Push : O(1)
* Pop  : O(1)
* Peek : O(1)
* Size : O(1)
"""

# Implementing a stack using a class:

class Stack:

	 def __init__(self):
	     self.items = []

	 def push(self, item):
	 	 self.items.append(item)

	 def is_empty(self):
	 	 return self.items == []

	 def pop(self):
	     return self.items.pop()

	 def peek(self):
	     return self.items[len(self.items) - 1]

	 def size(self):
	     return len(self.items) 

# Defining our first stack to experiment with it

my_stack = Stack()

# pushing three elements to our stack

my_stack.push('First')
my_stack.push('Second')
my_stack.push('Third')

print(my_stack.items)

# checking if our stack is empty

print(my_stack.is_empty()) # this will return False, our stack contains three elements

# popping-out the three elements

my_stack.pop()
my_stack.pop()
my_stack.pop()

print(my_stack.items)
# checking if our stack is empty

print(my_stack.is_empty()) # this will return True, our stack is empty now
