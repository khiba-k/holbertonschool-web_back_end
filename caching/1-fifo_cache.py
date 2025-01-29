#!/usr/bin/python3
"""FIFO Caching Code
"""
BaseCaching = __import__('base_caching').BaseCaching
    

class FIFOCache(BaseCaching):
    """FIFO caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to cache using FIFO eviction policy.
        Args:
            key (str): Key for the item.
            item (any): Item to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                firstkey = next(iter(self.cache_data))
                self.cache_data.pop(firstkey)
                print(f"DISCARD: {firstkey}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.
        Args:
            key (str): Key to retrieve.
        Returns:
            any: Cached value or None if key doesn't exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
