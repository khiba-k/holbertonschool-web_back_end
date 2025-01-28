#!/usr/bin/env python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the BasicCache."""
        super().__init__()

    def put(self, key, item):
        """Stores an item in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache.
        """
        
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
