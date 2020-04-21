import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Add an element to the top of a stack
        # top of stack would be the tail
        self.storage.add_to_tail(value)
        self.size += 1

# there is an error in this one - go back!
    def pop(self):
        # Remove an element from the top of a stack
        if self.storage.tail is None:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_tail()
        

    def len(self):
        # now return length
        return self.size
