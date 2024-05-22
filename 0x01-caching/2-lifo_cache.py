#!/usr/bin/env python3
"""task 2"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the item value for the key in self.cache_data."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                if self.last_key is not None:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """return the value linked to the key in self.cache_data."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
