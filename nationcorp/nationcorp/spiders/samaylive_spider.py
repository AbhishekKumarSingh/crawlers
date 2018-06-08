from nationcorp.items import NationcorpItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SamayLiveSpider(CrawlSpider):
    name = 'devsena'
    allowed_domains = ['samaylive.com']
    start_urls = ['http://www.samaylive.com']

    rules = (
             Rule(LinkExtractor(allow=(), restrict_css=()),
                 callback='parse_news', follow=True),)

    def parse_news(self, response):
        item = NationcorpItem()

        headline = response.css("div#printTitle h1::text").extract_first()
        hsynopsis = response.css("div.article_text p b::text").extract_first()
        #esumm = response.css(".english_summary_content::text").extract_first()
        #news_body = response.css(".ecom-ad-content p").extract()[1:]

        flag = headline and hsynopsis

        if flag:
            item['link'] = response.url
            item['headline'] = headline.strip()
            item['synopsis'] = hsynopsis.strip()
            #item['news_body'] = news_body

            yield item
