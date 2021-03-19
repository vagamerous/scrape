import scrapy
import json

MUSICAS = "https://www.ticketsforfun.com.br/categorias/musica"


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = [MUSICAS]
    headers = {
        'USER_AGENT' : '/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
    }

    def parse(self, response):
        script = response.xpath("//script[@type='application/json']/text()").get()
        json_data = json.loads(script)
        json_props = json_data["props"]
        json_iprops = json_props["initialProps"]
        json_pprops = json_iprops["pageProps"]
        json_category = json_pprops["category"]
        json_content = json_category["content"]
        json_events = json_content["events"]
        for event in json_events:
            yield {
            "Name" : event['title']
            }