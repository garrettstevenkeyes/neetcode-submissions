class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        #left=LRU, right = most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #remove from the list
    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    #insert at right, because its more recently used
    def insert(self, node):
        prev, nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    #everytime with get the value we want to update it to the most recent
    #remove and insert helper functions help here
    def get(self, key: int) -> int:
        if key in self.cache:
            #since we are getting we remove and reinsert at right most
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #remove if the key value already exists
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from the list and delete from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
