from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        value = self.values.get(key, -1)
        if value != -1:
            self.values.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        self.values[key] = value
        self.values.move_to_end(key)
        if len(self.values) > self.capacity:
            k, v = self.values.popitem(0)


class LRUCache1:
    def __init__(self, capacity: int):
        self.N = 0
        self.capacity = capacity
        self.queue = []
        self.values = {}

    def get(self, key: int) -> int:
        value, count = self.values.get(key, (-1, 0))
        if value != -1:
            self.queue.append(key)
            self.values[key] = (value, count + 1)
        return value

    def cleanup(self) -> None:
        while self.N > self.capacity:
            oldest_key = self.queue.pop(0)
            val, count = self.values.get(oldest_key)
            if count == 1:
                self.N -= 1
                self.values.pop(oldest_key)
            else:
                self.values[oldest_key] = (val, count - 1)

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            # if existing mark the count in the queue
            val, count = self.values[key]
            self.values[key] = (value, count + 1)
            self.queue.append(key)
        else:
            # append it to queue
            self.queue.append(key)
            self.values[key] = (value, 1)
            self.N += 1
            self.cleanup()
