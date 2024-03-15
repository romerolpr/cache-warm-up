class Cache:
    warmish: list
    strptime = '%a, %d %b %Y %H:%M:%S %Z'
    
    def __init__(self, fetch, log) -> None:
        self.warmish = []
        self.fetch = fetch
        self.log = log
        
    def __add(self, link: str):
        if link not in self.warmish: 
            self.warmish.append(link)
    
    def warm_up(self, url: str, attempt = 1):
        if attempt > 3:
            self.log.error(self.log, message=f'attempt exceeded -> {url}')
            return
        
        response = self.fetch.request(self.fetch, url=url)
        
        if response.status_code != 200:
            self.log.error(self.log, message=f'status {response.status_code} receiving for {url}')
            return
        
        cf_cache_status = response.headers.get('cf-cache-status')

        if cf_cache_status == 'HIT':
            self.__add(link=url)
            self.log.info(self.log, message=f'CACHED -> {url} ({round(self.fetch.time_spent, 2)}ms)')
        else:
            self.warm_up(url=url, attempt=attempt+1)
            self.log.info(self.log, message=f'({attempt}) retrying request for {url}')
      