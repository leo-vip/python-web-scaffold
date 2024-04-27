from datetime import timedelta, datetime

from cachetools import TTLCache


class MyCache:
    """
    缓存： 最大的缓存数量、超时清理。
    """
    source_cache = None

    def __init__(self, maxsize=100, ttl_hours=1):
        self.source_cache = TTLCache(maxsize=maxsize, ttl=timedelta(hours=ttl_hours), timer=datetime.now)

    def put(self, key, value):
        self.source_cache[key] = value

    def get(self, key):
        return self.source_cache.get(key, None)

    def clear(self, key):
        if key in self.source_cache.keys():
            del self.source_cache[key]
