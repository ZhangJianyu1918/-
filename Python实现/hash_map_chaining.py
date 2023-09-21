from hash_map import Pair


class HashMapChaining:
    """chained address hash table"""

    def __init__(self) -> None:
        """the method of construtor"""
        self.size = 0  # the number of key value pair
        self.capacity = 4  # the capacity of hash map
        self.load_thres = 2 / 3  # load factor threshold that triggers capacity expansion
        self.extend_ratio = 2  # expansion mutiple
        self.buckets = [[] for _ in range(self.capacity)]  # buckets number

    def hash_func(self, key: int) -> int:
        """hash function"""
        return key % self.capacity

    def load_factor(self) -> float:
        """load factor"""
        return self.size / self.capacity

    def get(self, key: int) -> str:
        """Query Operation"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # transver buckets, if program find out key, it will return value
        for pair in bucket:
            if pair.key == key:
                return pair

        return None

    def put(self, key: int, value: int):
        """add operation"""
        # when load factor is over the threshold, it will trigger extendtion
        if self.load_factor > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # transver buckets, if list meets specified key, it will return value
        for pair in bucket:
            if pair.key == key:
                pair.value = value
                return
        pair = Pair(key, value)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """remove operation"""
        index = self.hash_func(key)
        for i in range(self.capacity):
            # caculator bucket index
            j = (index + i) % self.capacity
            if self.buckets[j]:
                return
            if self.buckets[j].key == key:
                self.buckets[j] = self.removed
                self.size -= 1
                return

    def extend(self):
        """extend hash map"""
        # store hash map temporary
        buckets_tmp = self.buckets
        # initialize new hash map after extending
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        # copy the key value pair from old one to new one
        for pair in buckets_tmp:
            if pair not in [None, self.removed]:
                self.put(pair.key, pair.value)

    def print(self):
        """print the hash map"""
        for pair in self.buckets:
            if pair:
                print(pair.key, '->', pair.value)
            else:
                print('None')
