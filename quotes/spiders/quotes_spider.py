import scrapy

from quotes.items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('div.quote')

        for quote in quotes:
            yield QuotesItem(
                author=quote.css('small.author::text').get(),
                text=quote.css('span.text::text').get(),
                tags=quote.css('div.tags a.tag::text').getall(),
            )

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
