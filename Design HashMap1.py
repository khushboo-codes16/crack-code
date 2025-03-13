class ListNode:
    """A node in the linked list used for separate chaining."""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        """Initialize the hash map with a fixed-size array of buckets."""
        self.size = 1000
        self.buckets = [None] * self.size
    
    def _hash(self, key: int) -> int:
        """Compute the hash index."""
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        """Insert (key, value) or update existing key."""
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while True:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)  # Add new node

    def get(self, key: int) -> int:
        """Return the value associated with the key, or -1 if not found."""
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        """Remove key from the hash map if it exists."""
        index = self._hash(key)
        current = self.buckets[index]
        if not current:
            return
        
        if current.key == key:
            self.buckets[index] = current.next
            return
        
        prev = None
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev, current = current, current.next
