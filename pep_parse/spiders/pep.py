import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            'a.pep.reference.internal::attr(href)').getall()
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number_and_name = response.css(
            'h1.page-title::text').get().split(' – ')
        number_pep = number_and_name[0][4:]
        name_pep = number_and_name[1]
        data = {
            'number': int(number_pep),
            'name': name_pep,
            'status': response.css('dt:contains("Status")+dd ::text').get()
        }
        yield PepParseItem(data)
