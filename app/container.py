from app import Fetch, Sitemap, Log, Cache

class Container:
    sitemap = Sitemap(fetch=Fetch, log=Log)
    cache = Cache(fetch=Fetch, log=Log)
    log = Log()