class Node:

    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next

    def __str__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None
        self.list_size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        self.head = Node(item, self.head)
        self.list_size += 1

    # the same as .size() method. Allows calling len(linked_list)
    def __len__(self):
        return self.list_size

    # the same as .search(item). supports 'if item in linked_list:'
    def __contains__(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    # the same as .remove(item). Supports 'del list[item]'
    def __delitem__(self, item):
        if self.head is not None:
            if self.head.data == item:
                self.head = self.head.next
                self.list_size -= 1
            else:
                previous = self.head
                current = self.head.next
                while current is not None and current.data != item:
                    previous, current = current, current.next

                if current:
                    previous.next = current.next
                    self.list_size -= 1

    def append(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
        self.list_size += 1

    def pop(self, pos=None):
        if self.head is None or (pos is not None and (not isinstance(pos, int) or pos < 0 or pos > self.list_size - 1)):
            return None

        self.list_size -= 1
        target = pos if pos is None else self.list_size - 1
        if target == 0:
            result, self.head = self.head.data, self.head.next
            return result
        else:
            previous = self.head
            i = 1
            while i != target:
                previous = previous.next
                i += 1
            result, previous.next = previous.next.data, previous.next.next
            return result

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
