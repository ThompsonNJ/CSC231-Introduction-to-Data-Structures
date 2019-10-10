#==========================================================================
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
#==========================================================================
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def add(self, item):
        node = Node()
        self.count += 1
        node.data = item
        node.next = self.head
        node.previous = None
        self.head = node
        if self.count == 1:
            self.tail = node
        elif self.count == 2:
            self.tail = node
            self.tail.previous = self.head

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        node = Node()
        self.count += 1
        node.data = item
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
    
    def pop(self, pos=None):
        if self.is_empty():
            return None
        elif self.count == 1:
            temp_head = self.head
            self.count -= 1
            self.head = None
            self.tail = None
            
            return temp_head
        elif pos is None or pos == self.count-1:
            node = self.tail.previous
            temp_tail = self.tail
            self.count -= 1
            node.next = None
            self.tail = node
                
            return temp_tail
        if str(pos).strip('-').isdigit() and pos is not None and pos in range(-self.count, self.count):
            if pos < 0:
                pos = self.count + pos

            node = self.head
            if node is not None:
                if pos == 0:
                    self.count -= 1
                    temp_head = self.head
                    self.head = self.head.next

                    return temp_head

                counter = 0
                while counter < pos:
                    counter += 1
                    node = node.next

                node.previous.next = node.next
                if node.next is not None:
                    node.next.previous = node.previous

                self.count -= 1
                return node
        else:
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
                                
                                if node.next is None:
                                    self.tail = node
                                else:
                                    node.next.previous = node
                                break
                            
                            node = node.next
