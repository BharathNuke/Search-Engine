class page:
    
    def __init__(self,url,rank=10**-9):
        from urllib.request import urlopen
        self.uo = urlopen
        self._rank = rank
        self._url = url
        self._html = self.get_html(url)
        self._outlinks = self.crawl_html(self._html)
        self._inlinks = []

    def get_links(self):
        return self._outlinks

    def get_rank(self):
        return self._rank

    def get_html(self,url):
        return str(self.uo(self.format_url(url)).read())

    def format_url(self,url):
        if url.startswith('/'):
            return self._url+url
        return url
        

    def crawl_html(self,html):
        #html = str(html)
        links = []
        while True:
            pos = html.find('<a href')
            if pos == -1:
                break
            html = html[pos+8:]
            start = html.find('"')
            links.append(html[start+1:html.find('"',start+1)])
        return links
    def __str__(self):
        return self._url

#p = page('http://google.co.in')
#l = p.get_links()
