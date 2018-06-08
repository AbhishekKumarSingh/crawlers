from livem.items import LivemItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IndianexpressSpider(CrawlSpider):
    name = 'kal-bhairava'
    allowed_domains = ['livemint.com']
    start_urls = ['http://www.livemint.com']

    rules = (
             Rule(LinkExtractor(allow=(), restrict_css=()),
                 callback='parse_news', follow=True),)

    def parse_news(self, response):
        item = LivemItem()

        #hsummary = response.css(".ecom-ad-content p::text").extract_first()
        #hnews = h = response.css(".ecom-ad-content p::text").extract()[1:]
        heading = response.css("section.left-sidebar h1::text").extract_first()
        #ptitle = response.xpath('//title/text()').extract_first()
        esumm = response.css("section.left-sidebar h1 + div::text").extract_first()
        news_body = response.css("div.content p::text").extract()

        flag = heading and esumm and news_body

        if flag:
            item['link'] = response.url
            #item['page_title'] = ptitle.strip()
            item['headline'] = heading.strip()
            item['summ'] = esumm.strip()
            item['news'] = news_body
            #if esumm:
            #    item['eng_summ'] = esumm.strip()
            #else:
            #    item['eng_summ'] = ''
            #item['news_body'] = news_body

            yield item
