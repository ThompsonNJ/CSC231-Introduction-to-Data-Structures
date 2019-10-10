import hashing

FREE = -1


# An implementation of the Map (a.k.a., Dictionary) ADT using a hash table
class HashTable:

    def __init__(self, size=11, load_factor=0.66):
        self.size = size
        self.load_factor = load_factor
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __len__(self):
        return len(self.keys) - self.keys.count(None)

    def __contains__(self, key):
        return key in self.keys

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        k = self.hash(key)
        done = False
        i = 0

        while not done:
            pos = (k + i * i) % self.size
            if self.keys[pos] == key:
                self.values[pos] = None
                self.keys[pos] = FREE
                done = True
            elif self.keys[pos] is None:
                done = True
            i += 1

    def put(self, key, val):
        if (len(self) + 1) / self.size >= self.load_factor:
            print('Load factor exceeded! Old size was {}. Calling resize_table().'.format(self.size))
            self.resize_table()

        k = self.hash(key)
        done = False
        i = 0
        while not done:
            pos = (k + i * i) % self.size
            if self.keys[pos] is None or self.keys[pos] == FREE or self.keys[pos] == key:  # key slot
                self.keys[pos] = key
                self.values[pos] = val
                done = True
            i += 1

    def get(self, key):
        k = self.hash(key)
        done = False
        i = 0
        result = None
        pos = 0
        while not done:
            pos = (k + i * i) % self.size
            if self.keys[pos] == key or self.keys[pos] is None:
                result = self.values[pos]
                done = True
            i += 1

        return result, pos

    def hash(self, key):
        return hashing.secret_hash(key, self.size)

    # This method is called by put() when adding a new item to the hash table would exceed the load factor threshold
    # Implement this method to double the size of the hash table, and reinsert the old data.
    # This method should not return anything.
    def resize_table(self):
        pass


