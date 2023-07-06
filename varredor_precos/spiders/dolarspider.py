import scrapy
from datetime import datetime
from utils.email_sender import Emailer


class PriceScraperSpider(scrapy.Spider):
    # identidade
    name = 'dolarbot'
    # Request

    def start_requests(self):
        urls = ['https://www.investing.com/currencies/usd-brl']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        dolar = response.xpath(
            "//span[@data-test='instrument-price-last']/text()")[0].get()

        if float(dolar) > 4.90:
            email = Emailer('machado.david.developer@gmail.com',
                            'mtiqjlxrkrzhmdxn')
            lista_de_contatos = ['machadodavid32@gmail.com']
            email.definir_conteudo('Dolár está subindo', 'machadodavid32@gmail.com', lista_de_contatos,f'O dólar acabou de subir para {dolar}, favor verificar se agora é um bom momento para comprar dólar.')

            email.enviar_email(30)

"""
EMAIL_ADDRESS = 'machado.david.developer@gmail.com'
EMAIL_PASSWORD = 'mtiqjlxrkrzhmdxn'"""