class MyHashMap:

    def __init__(self):
        self.size=1009
        self.buckets=[[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        b=self.buckets[key % self.size]
        for pair in b:
            if pair[0] == key:
                pair[1] = value
                return 
        b.append([key,value])

    def get(self, key: int) -> int:
        for k,v in self.buckets[key % self.size]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b=self.buckets[key % self.size]
        for i,pair in enumerate(b):
            if pair[0] == key:
                b.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)