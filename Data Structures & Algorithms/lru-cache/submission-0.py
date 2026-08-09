class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Maps key -> Node
        
        # Dummy head (Least Recently Used) and dummy tail (Most Recently Used)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper: remove node from doubly linked list
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper: insert node at the tail (Most Recently Used position)
    def _insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update node to be Most Recently Used
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        
        # If cache exceeds capacity, evict Least Recently Used (node right after dummy head)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)