class MyHashMap:
    def __init__(self):
        self.data = [[] for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        has = key % 10000
        for idx, (k, v) in enumerate(self.data[has]):
            if k == key:
                self.data[has][idx] = (key, value)
                return
        self.data[has].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        has = key % 10000
        if len(self.data[has]) == 0:
            return -1
        for k, value in self.data[has]:
            if k == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        has = key % 10000
        for idx in range(len(self.data[has])):
            k, value = self.data[has][idx]
            if k == key:
                del self.data[has][idx]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
