from core.cache_manager import MyCache

# handler cache used by api
cache_source_interface = MyCache(ttl_hours=24)

