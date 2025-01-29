#!/usr/bin/python3
"""MRU Caching Code
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system that inherits from BaseCaching.
    Implements a Most Recently Used (MRU) cache replacement policy.
    When the cache reaches its limit, the most recently used entry is discarded.
    """

    def __init__(self):
        """
        BasicCache class represents a simple caching
        __init__(): Initializes the BasicCache object.
        put: Adds an item to the cache.
        get: Retrieves an item from the cache based on the key.
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.
        If the cache exceeds the maximum size, the least recently used item is removed.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache and mark it as recently used.
        Moves the accessed item to the end to indicate recent use.
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
