class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.val={}
        self.freq={}
        self.buckets=defaultdict(OrderedDict)
        self.min_freq=0

    def _touch(self,key: int) -> None:
        f=self.freq[key]
        del self.buckets[f][key]
        if not self.buckets[f]:
            del self.buckets[f]
            if self.min_freq == f:
                self.min_freq = f + 1
        self.freq[key] = f+1
        self.buckets[f+1][key]=None

    def get(self, key: int) -> int:
        if key not in self.val:
            return -1
        self._touch(key)
        return self.val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.val:
            self.val[key] = value
            self._touch(key)
            return 
        if len(self.val) == self.cap:
            old, _ = self.buckets[self.min_freq].popitem(last=False)
            if not self.buckets[self.min_freq]:
                del self.buckets[self.min_freq]
            del self.val[old]
            del self.freq[old]
        self.val[key]=value
        self.freq[key]=1
        self.buckets[1][key]=None
        self.min_freq=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)