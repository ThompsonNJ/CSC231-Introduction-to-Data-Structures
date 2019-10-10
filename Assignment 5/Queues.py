#==========================================================================
# AUTHOR:............ <LastName>, <FirstName>
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
#==========================================================================
from LinkedList import *
from DoublyLinkedList import *

class QueuePythonList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)


class QueueLinkedList:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, item):
        self.list.add(item)

    def dequeue(self):
        return self.list.pop()

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.size()
        

class QueueDoublyLinkedList:
    def __init__(self):
        self.list = DoublyLinkedList()

    def enqueue(self, item):
        self.list.add(item)

    def dequeue(self):
        return self.list.pop()

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.size()
