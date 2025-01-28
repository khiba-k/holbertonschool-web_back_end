#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")

class FIFOCache(BaseCaching):
    """
    FIFOCache is a subclass of BaseCaching that implements a FIFO (First-In-First-Out) cache.

    This cache stores items with a key-value pair and provides methods to add items (`put`) 
    and retrieve items (`get`). If the key or item is `None`, the item is not added to the cache.
    """

    def __init__(self):
        """
        Initializes the FIFO Cache by calling the superclass (BaseCaching) initializer.
        """
        super().__init__()
    
    def put(self, key, item):
        """
        Adds an item to the cache.

        If either the key or the item is `None`, the item is not added to the cache.

        Args:
            key (str): The key to store the item under.
            item (str): The value to store in the cache.
        
        Returns:
            None
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        """
        Retrieves an item from the cache.

        If the `key` is `None`, returns `None`. Otherwise, returns the value associated 
        with the key in the cache in a formatted string. If the key doesn't exist, returns `None`.

        Args:
            key (str): The key to retrieve the item for.

        Returns:
            str: A formatted string `key: item` if the key exists, or `None` if the key is not found or is `None`.
        """
        self.item = self.cache_data.get(key)
        
        if key is None:
            return None
        else:
            return f"{key}: {self.item}"
