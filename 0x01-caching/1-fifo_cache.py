#!/usr/bin/env python3
"""First-In First-Out caching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and retrieving items from
    a dictionary using the FIFO method"""
    def __init__(self):
        """intializes the class with the parent's init method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(slef.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to a given key, or None"""
        if key is None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
