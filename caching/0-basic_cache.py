#!/usr/bin/env python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        self.item = self.cache_data.get(key)
        
        if key is None:
            return None
        else:
            return f"{key}: {self.item}"
