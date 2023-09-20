from typing import Optional 
class Pair:
    # key value pair
    def __init__(self, key:int, value:str) -> None:
        self.key = key
        self.value = value

class ArrayHashMap:
    # relize hash table based on array
    def __init__(self) -> None:
        self.buckets: list[Optional[Pair]] = [None] * 100

    def hash_func(self, key: int) -> int:
        index = key % 100
        return index
    
    def get(self, key: int) -> int:
        # serach operate
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.value
    
    def put(self, key: int, value: str):
        # add operate
        pair = Pair(key, value)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key:int):
        index: int = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        # get all key value pair
        result: list[Pair] = []
        for pair in self.buckets:
            if pair:
                result.append(pair)
        return result
    
    def key_set(self) -> list[int]:
        # get all keys
        result = []
        for pair in self.buckets:
            if pair:
                result.append(pair.key)
        return result
    
    def value_set(self) -> list[str]:
        # get all value
        result = []
        for pair in self.buckets:
            if pair:
                result.append(pair.value)
        return result
    
    def print(self):
        # print hash table
        for pair in self.buckets:
            if pair:
                print(pair.key,'->',pair.value)