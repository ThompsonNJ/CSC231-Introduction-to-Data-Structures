class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return str(self.data)
    

class Stack:
    def __init__(self):
        self.head = None
        self.list_size = 0

    def push(self, item):
        new = Node()
        new.data = item
        new.next = self.head
        self.head = new
        self.list_size += 1

    def pop(self):
        if self.head is not None and self.head.next is not None:
            self.list_size -= 1
            temp_head = self.head
            self.head = self.head.next
            return temp_head

        elif self.head is not None and self.head.next is None:
            self.list_size -= 1
            temp_head = self.head
            self.head = None
            
        else:
            temp_head = None
            
        return temp_head

    def peek(self):
        if self.head is not None:
            return self.head

    def is_empty(self):
        return self.list_size == 0

    def size(self):
        return self.list_size            
            
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr

    def __contains__(self, item):
        curr = self.head
        found = False
        while curr is not None and not found:
            if curr.data == item:
                found = True
            else:
                curr = curr.next
