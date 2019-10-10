# An implementation of the Map (a.k.a., Dictionary) ADT using a hash table
class HashTable:

    def __init__(self, size=11):
        self.size = size
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
        start = self.hash(key)
        done = False
        pos = start
        while self.keys[pos] is not None and not done:
            if self.keys[pos] == key:
                self.keys[pos] = self.values[pos] = None
                done = True
            else:
                pos = self.rehash(pos)
                if pos == start:
                    done = True

    def put(self, key, val):
        pos = self.hash(key)

        if self.keys[pos] is None:      # key not yet in table
            self.keys[pos] = key
            self.values[pos] = val
        elif self.keys[pos] == key:     # key is in table in expected position
            self.values[pos] = val
        else:                           # a different key is in that position
            start = pos
            pos = self.rehash(pos)
            done = False

            while not done:
                if self.keys[pos] is None:        # found an empty key slot
                    self.keys[pos] = key
                    self.values[pos] = val
                    done = True
                elif self.keys[pos] == key:       # found the key in a rehashed position
                    self.values[pos] = val
                    done = True
                elif pos == start:                # no empty slots
                    raise RuntimeError('No empty slots in hash table!')
                else:
                    pos = self.rehash(pos)

    def get(self, key):
        start = self.hash(key)
        data = None
        done = False
        pos = start
        while self.keys[pos] is not None and not done:
            if self.keys[pos] == key:
                data = self.values[pos]
                done = True
            else:
                pos = self.rehash(pos)
                if pos == start:
                    done = True
        return data, pos

    # You must edit this method to return an integer hash based on the key.
    # key will be a string containing a phone number in the format 'XXX-XXX-XXXX'
    def hash(self, key):
        newkey = ''
        for char in str(key):
            if char in '0123456789':
                #newkey += char
                newkey = newkey.join('-')
    
        print(newkey)
        newkey = str(int(newkey)**2)     
    
        return int(str(newkey[(len(newkey)//2)-1])
                   +str(newkey[(len(newkey)//2)])
                   +str(newkey[(len(newkey)//2)+1])) % self.size

    def rehash(self, key):
        return (key + 1) % self.size
