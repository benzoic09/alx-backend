#!/usr/bin/env python3
""" class FIFOCache that inherits from BaseCaching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ class FIFOCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the item value for the key in self.cache_data."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.cache_data:
                    print(f"DISCARD: {next(iter(self.cache_data))}")
                    self.cache_data.popitem(last=False)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key in self.cache_data."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
