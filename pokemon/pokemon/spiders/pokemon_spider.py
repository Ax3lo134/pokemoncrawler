import scrapy
from ..items import PokemonItem
from slugify import slugify, SLUG_OK

class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    start_urls = [
        'https://pokemondb.net/pokedex/bulbasaur'
    ]

    def parse(self, response):
        items = PokemonItem()

        number = response.css(".vitals-table strong::text").extract()
        img_url = response.css(".span-lg-4 img::attr(src)").extract()
        name = response.css('h1::text').extract()
        types = response.css('.vitals-table .type-icon::text').extract()
        hp = response.css('tr:nth-child(1) th+ .cell-num').css('::text').extract()
        attack = response.css('tr:nth-child(2) th+ .cell-num::text').extract()
        defense = response.css('tr:nth-child(3) th+ .cell-num::text').extract()
        sp_atk = response.css('tr:nth-child(4) th+ .cell-num::text').extract()
        sp_def = response.css('tr:nth-child(5) th+ .cell-num::text').extract()
        speed = response.css('tr:nth-child(6) th+ .cell-num::text').extract()
        total = [str(int(hp[0]) + int(attack[0]) + int(defense[0]) + int(sp_def[0]) + int(sp_atk[0]) + int(speed[0]))]

        items['image_urls'] = img_url
        items['number'] = [number[0]]
        items['name'] = [slugify(name)]
        items['types'] = types[0:2]
        items['hp'] = [hp[0]]
        items['attack'] = [attack[0]]
        items['defense'] = [defense[0]]
        items['sp_atk'] = [sp_atk[0]]
        items['sp_def'] = [sp_def[0]]
        items['speed'] = [speed[0]]
        items['total'] = [total[0]]

        yield items

        next_page = 'https://pokemondb.net/' + response.css(".entity-nav-next::attr(href)").get()

        if response.css(".entity-nav-next::attr(href)").get():
            yield response.follow(next_page, callback=self.parse)
