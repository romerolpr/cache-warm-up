import xml.etree.ElementTree as ET

class Sitemap:
    def __init__(self, fetch, log):
        self.fetch = fetch
        self.links = []
        self.log = log
        
    def __add(self, urls: list, arr: list):
        for url in urls:
            arr.append(url)
        return self

    def __crawl_sitemap_index(self, index_url: str, index_prefix = 'sitemap'):
        response = self.fetch.request(self.fetch, url=index_url)
        root = ET.fromstring(response.content)
        return root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}' + index_prefix)
        
    def crawl(self, index_url: str, index_prefix = 'sitemap', is_index = True):
        try:
            index = self.__crawl_sitemap_index(index_url, index_prefix)
            locs = [sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for sitemap in index]
            
            if is_index:
                for loc in locs:
                    self.log.info(self.log, message=f'crawling {loc}')
                    self.crawl(index_url=loc, index_prefix='url', is_index=False)
            else:
                self.__add(urls=locs, arr=self.links)
        except Exception as e:
            self.log.error(self.log, message=e)
            
        return self