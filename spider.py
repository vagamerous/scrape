import scrapy  # vamos usar o scrapy, previamente instalado, para realizar essa extração;
import json  # como o site do qual iremos extrair a informação é estruturado em JSON, devemos importar o módulo json para poder trabalharmos com ele.  

MUSICAS = "https://www.ticketsforfun.com.br/categorias/musica" # colocamos o link da página da qual iremos extrair a informação em uma variável.


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = [MUSICAS]
    headers = {
        'USER_AGENT' : '/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
    }

    def parse(self, response): # para realizar a extração, devemos usar o método parse como uma função da classe criada, utilizando response como parâmetro.
        script = response.xpath("//script[@type='application/json']/text()").get()  # aqui escolhi usar xpath para chegar à informação, mas poderia ter usado css também.
        json_data = json.loads(script)  #  utilizo o json.loads para acessar o script em json, colocando-o em uma variável. 
        json_props = json_data["props"] # para acessar o caminho da informação, utilizo o "shell" no prompt. Com isso, posso ver que ela está no caminho 'props'.
        json_iprops = json_props["initialProps"] # continuo usando o shell para descobrir o caminho da informação;
        json_pprops = json_iprops["pageProps"]
        json_category = json_pprops["category"]
        json_content = json_category["content"]
        json_events = json_content["events"] # esta última varável recebe a lista das informações buscadas;
        for event in json_events: # utiliza-se o for para acessar toda a informação na lista;
            yield {   #  e o yield para extraí-la para um arquivo CSV. Neste exemplo, só foi extraído o nome do evento, mas pode-se extrair quantas informações forem necessárias.
            "Name" : event['title']
            }
