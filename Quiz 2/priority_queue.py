class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        i = 0
        while i < len(self.queue) and self.queue[i].priority < item.priority:
            i += 1
        self.queue.insert(i, item)
##        if self.is_empty():
##            self.queue.append(item)
##        else:        
##            current = 0
##            found =  False
##            while not found:
##                if item.priority == self.queue[current].priority:
##                    self.queue.insert(current-1, item)
##                    found = True
##                elif item.priority > self.queue[current].priority:
##                    self.queue.insert(current, item)
##                    found = True
##                elif item.priority < self.queue[current].priority:
##                    current += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)
