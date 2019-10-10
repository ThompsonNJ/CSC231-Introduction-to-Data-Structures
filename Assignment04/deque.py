class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.deque)