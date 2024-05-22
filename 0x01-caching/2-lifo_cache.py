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
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                discard_key, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """return the value linked to the key in self.cache_data."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
