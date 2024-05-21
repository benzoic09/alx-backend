#!/usr/bin/env python3
""" class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """update the put and get"""
    def put(self, key, item):
        """ assign the item value for the key in self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key in self.cache_data."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
