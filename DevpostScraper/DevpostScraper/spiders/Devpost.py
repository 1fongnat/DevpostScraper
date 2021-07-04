import scrapy


class DevpostSpider(scrapy.Spider):
    name = 'Devpost'
    allowed_domains = ['https://init-weekend.devpost.com/']
    start_urls = ['https://init-weekend.devpost.com/']
    def parse(self, response):
        challenges = response.xpath('.//div[@class="small-12 large-6 columns end prize"]')
        

        for challenge in challenges:
            name = challenge.xpath('.//h6/text()').extract()
            description = challenge.xpath('.//p/text()').extract()
            namefilter = str(name[1])
            yield{
                'Name: ': namefilter[13:-11],
                'Description ': description
                }

