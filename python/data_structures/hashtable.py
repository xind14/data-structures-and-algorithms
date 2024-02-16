from data_structures.linked_list import LinkedList

class Hashtable:
    """
    A hashtable implementation.
    """

    def __init__(self, size=1024):
        """
        Initializes the hashtable with a specified size.
        """
        self._size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """
        Computes the hash value for the given key.
        """
        index = sum(ord(char) for char in key)
        index = (index * 599) % self._size
        return index

    def set(self, key, value):
        """
        Sets the key-value pair in the hashtable.
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self._buckets[index] = bucket

        current = bucket.head
        while current:
            if current.value[0] == key:
                current.value[1] = value  # Update value
                return
            current = current.next

        bucket.insert([key, value])  # No existing key found, add new entry

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            return None

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        return None


    def keys(self):
        """
        Returns a list of all keys in the hashtable.
        """
        key_list = []
        for bucket in self._buckets:
            current = bucket.head if bucket else None
            while current:
                key_list.append(current.value[0])
                current = current.next
        return key_list


    def has(self, key):
        """
        Checks if the given key exists in the hashtable.
        """
        for bucket in self._buckets:
            current = bucket.head if bucket else None
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False




