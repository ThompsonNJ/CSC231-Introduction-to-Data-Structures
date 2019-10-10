

# A Python implementation of the Linked List data structure. The code here is written for illustrative purposes and
# does not use some Pythonic tricks in the interests of clarity.
class Node:

    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None
        self.list_size = 0

    # return True or False to indicate whether the linked list is empty or not
    def is_empty(self):
        return self.head is None

    # insert a new item at the front (head) of the list
    def add(self, item):
        new = Node()
        new.data = item
        new.next = self.head
        self.head = new
        self.list_size += 1

    # return a count of the number of items in the linked list
    def size(self):
        return self.list_size

    # return True or False to indicate whether 'item' exists in the linked list
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next

        return found

    # remove 'item' from the linked list if it is in the list
    def remove(self, item):
        if self.head is not None:
            previous = None
            current = self.head
            found = False

            while current is not None and not found:
                if current.data == item:                # we found the node containing item we want to remove
                    found = True
                    self.list_size -= 1
                    if previous is None:                # handle the case where the item is at the head of the list
                        self.head = current.next
                    else:
                        previous.next = current.next    # in other cases, 'snip' out the node containing the item
                else:
                    previous = current
                    current = current.next

    # add a new item to the end (tail) of the list
    def append(self, item):
        new = Node()
        new.data = item
        new.next = None
        if self.head is None:                           # handle the case where the list is empty
            self.head = new
        else:
            current = self.head
            while current.next is not None:             # walk to the end of the list
                current = current.next
            current.next = new
        self.list_size += 1

    # remove an item from the list and return it.
    #   If pos=None, remove the last item from the list and return it
    #   If 0 <= pos <= list.size() -1, remove the item at pos and return it
    #   else, pos is invalid, so return None
    def pop(self, pos=None):
        if self.head is None:
            return None

        if pos is not None and (not isinstance(pos, int) or pos < 0 or pos > self.list_size - 1):
            return None

        target = pos
        if pos is None:                     # calling pop() is the same as pop(list.size() - 1)
            target = self.list_size - 1

        previous = None
        current = self.head
        i = 0

        while i != target:                  # move current until it is at the index we want to pop
            previous = current
            current = current.next
            i += 1

        result = current.data
        if previous is None:                # this is true when we are popping the head of the list
            self.head = current.next
        else:
            previous.next = current.next    # 'snip' out the node to pop

        self.list_size -= 1
        return result

    # support iteration of the LinkedList class using while or for loops.
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
