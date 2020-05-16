from requests.utils import quote
from pyquery import PyQuery as pq
from src.utils import get_page


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print(f'成功获取到代理({callback})', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_kuaidaili(self):
        """
        获取Kuaidaili
        :return: 代理
        """
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        for i in range(1, 5):
            print(f'Crawling: {start_url.format(i)}')
            html = get_page(start_url.format(i))
            if html:
                doc = pq(html)
                trs = doc('tbody tr').items()
                for tr in trs:
                    ip = tr.find('td[data-title="IP"]').text().strip()
                    port = tr.find('td[data-title="PORT"]').text().strip()
                    yield f'{ip}:{port}'

    def crawl_freeip(self):
        """
        获取freeip.top
        :return: 代理
        """
        start_url = 'https://www.freeip.top/?page=%s&country=%s'
        for i in range(8):
            print(f'Crawling: {start_url % (i, quote("中国"))}')
            html = get_page(start_url % (i, quote('中国')))
            if html:
                doc = pq(html)
                trs = doc('tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text().strip()
                    port = tr.find('td:nth-child(2)').text().strip()
                    yield f'{ip}:{port}'
