from hcorp.items import HcorpItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class OneIndiaSpider(CrawlSpider):
    name = 'mahasena'
    allowed_domains = ['hindi.oneindia.com', 'oneindia.com']
    start_urls = ['http://hindi.oneindia.com', 'http://hindi.oneindia.com/news']

    rules = (
             Rule(LinkExtractor(allow=('hindi\.oneindia\.com/*'), restrict_css=()),
                 callback='parse_news', follow=True),)

    def parse_news(self, response):
        item = HcorpItem()

        hsummary = response.css(".ecom-ad-content p::text").extract_first()
        hnews = h = response.css(".ecom-ad-content p::text").extract()[1:]
        heading = response.css(".heading::text").extract_first()
        ptitle = response.xpath('//title/text()').extract_first()
        esumm = response.css(".english_summary_content::text").extract_first()
        news_body = response.css(".ecom-ad-content p").extract()[1:]

        flag = hsummary and hnews and heading and ptitle

        if flag:
            item['link'] = response.url
            item['page_title'] = ptitle.strip()
            item['headline'] = heading.strip()
            item['summ'] = hsummary.strip()
            item['news'] = hnews
            if esumm:
                item['eng_summ'] = esumm.strip()
            else:
                item['eng_summ'] = ''
            item['news_body'] = news_body

            yield item
