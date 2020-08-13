# -*- coding: utf-8 -*-
import scrapy, time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True,
             process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"),
             process_request='set_user_agent')
    )

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        time.sleep(2)
        yield {
            'Title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'Release Date': response.xpath("//div[@class='subtext']/a[2]/text()").get(),
            'Duration': response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
            'Genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'Rated': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'Movie Url': response.url,
            'user-agent': response.request.headers['User-Agent'].decode('utf-8')
        }
