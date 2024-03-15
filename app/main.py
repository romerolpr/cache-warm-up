from app.container import Container

class App:
    container = Container()
    
    def run(self, domain: str):
        links = self.container.sitemap.crawl(index_url=f'https://{domain}/sitemap.xml').links

        for link in links:
            self.container.cache.warm_up(link)
            