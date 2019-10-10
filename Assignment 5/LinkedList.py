#==========================================================================
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
#==========================================================================
class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def add(self, item):
        self.count += 1
        node = Node()
        node.data = item
        node.next = self.head
        self.head = node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        self.count += 1
        node = self.head
        if node is not None:
            while node.next is not None:
                node = node.next
        
            new_node = Node()
            new_node.data = item
            node.next = new_node
        else:
            node = Node()
            self.head = node
            node.data = item
    
    def pop(self, pos=None):
        if self.is_empty():
            return None
        elif self.count == 1:
            self.count = 0
            temp_head = self.head
            self.head = None

            return temp_head
        elif pos is None:
            node = self.head
            if node is not None:
                for i in range(self.count-2):
                    node = node.next

                next_node = node.next
                node.next = None
                self.count -= 1

                return next_node

        elif pos is not None and pos in range(self.count):
            node = self.head
            if node is not None:
                if pos == 0:
                    self.count -= 1
                    temp_head = self.head
                    self.head = self.head.next
                    return temp_head

                for i in range(pos-1):
                    node = node.next

                next_node = node.next
                node.next = node.next.next
                self.count -= 1

                return next_node

        elif pos not in range(self.count):
            return None

    def search(self, item):
        if self.is_empty():
            return None
        else:
            node = self.head
            if node is not None:
                for i in range(self.count):
                    if node.data == item:
                        return True                    
                    node = node.next
            
                return False

    def remove(self, item):
        if self.is_empty():
            return None
        else:
            node = self.head
            if node is not None:
                if node.data == item:
                    self.head = self.head.next
                    self.count -= 1
                else:                    
                    for i in range(self.count):
                        if node.next is not None:
                            if node.next.data == item:
                                node.next = node.next.next
                                self.count -= 1

                                break
                        
                        node = node.next
