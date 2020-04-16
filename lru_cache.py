class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.lru = {}
        self.cache = {}
        self.count = 0

    def put(self, key, value):
        pass
        if self.capacity <= len(self.cache):
            prev_key = min(self.lru.keys(), key = lambda k: self.lru[k])
            self.lru.pop(prev_key)
            self.cache.pop(prev_key)

        self.lru[key] = self.count
        self.cache[key] = value
        self.count += 1

    def get(self, key):
        pass
        if key in self.cache:
            self.lru[key] = self.count
            self.count += 1
            return self.cache[key]
        else:
            return -1

    def get_cache(self):
        pass
        return self.cache