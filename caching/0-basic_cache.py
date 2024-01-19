#!/usr/bin/python3
"""
BasicCache class that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Define BasicCache """

    def put(self, key, item):
        """ Add key/value pair to the cache """
        if key is None and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve value from the cache based on given key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
