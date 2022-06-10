import scrapy
import datetime

class MlSpider(scrapy.Spider):
    name = 'ml'
    
    start_urls = ['https://lista.mercadolivre.com.br/pedais-e-acessorios/usado/_PriceRange_0-5000_PublishedToday_YES?page=1']
    
    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="ui-search-layout__item"]'):
            preco = i.xpath('.//span[@class="price-tag-fraction"]//text()').getall()
            titulo = i.xpath('.//h2[@class="ui-search-item__title ui-search-item__group__element"]/text()').get()
            link = i.xpath('./a/@href').get()
            
            yield{
                    'preco' : preco,
                'titulo' : titulo,
                'link' : link,
                }
        next_page = response.xpath('//a[contains(@title, "Seguinte")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)