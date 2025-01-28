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

if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))