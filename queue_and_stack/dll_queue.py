import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add an element to end of queue
        self.storage.add_to_tail(value)
        self.size += 1
        

    def dequeue(self):
        # remove an element from front of the queue
        if self.storage.head is None:
            return None
        else:
            # when we dequeue, we have to change it to -1
            self.size -= 1
            # then we remove from front of queue
            return self.storage.remove_from_head()

    def len(self):
        # now we return the new length
        return self.size
