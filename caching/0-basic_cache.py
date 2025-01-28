#!/usr/bin/env python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic caching system that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the BasicCache."""
        super().__init__()

    def put(self, key, item):
        """Stores an item in the cache.

        Args:
            key (str): The key for the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            str or None: The item with the key, or None if not found.
        """
        self.item = self.cache_data.get(key)
        
        if key is None:
            return None
        else:
            return f"{key}: {self.item}"
