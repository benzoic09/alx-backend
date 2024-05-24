#!/usr/bin/env python3
"""MRUCache module"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching and is an
    MRU caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the last item (most recently used)
            most_recent_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        value = self.cache_data[key]
        self.cache_data.move_to_end(key)
        return value
