class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        
    def _remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _insert(self, node: Node):
        prev = self.mru.prev
        next = self.mru
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        self._remove(node)
        self._insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)

        node = Node(key, value)
        self._insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self._remove(lru)
            self.cache.pop(lru.key, None)




# class Node:
#     def __init__(self, key: int, val: int):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}  # key → node

#         # Dummy head and tail (sentinels) to avoid edge cases
#         self.head = Node(0, 0)  # LRU side
#         self.tail = Node(0, 0)  # MRU side
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def _remove(self, node: Node) -> None:
#         """Detach a node from the linked list."""
#         prev, nxt = node.prev, node.next
#         prev.next = nxt
#         nxt.prev = prev

#     def _insert(self, node: Node) -> None:
#         """Insert node at the MRU side (before tail)."""
#         prev, nxt = self.tail.prev, self.tail
#         prev.next = node
#         node.prev = prev
#         node.next = nxt
#         nxt.prev = node

#     def get(self, key: int) -> int:
#         """Return value if key exists, else -1. Move accessed node to MRU."""
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self._remove(node)
#         self._insert(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         """Insert or update key. Evict LRU if over capacity."""
#         if key in self.cache:
#             # Remove old node before updating
#             self._remove(self.cache[key])
#         # Create new node and insert at MRU
#         node = Node(key, value)
#         self.cache[key] = node
#         self._insert(node)

#         # Evict LRU if capacity exceeded
#         if len(self.cache) > self.capacity:
#             lru = self.head.next
#             self._remove(lru)
#             del self.cache[lru.key]
