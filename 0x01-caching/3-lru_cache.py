#!/usr/bin/env python3
"""LRUCache module"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching and is an
    LRU caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move the key to the end to show that it was recently used
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item (least recently used)
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to show that it was recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
