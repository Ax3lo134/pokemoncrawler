# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    types = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    sp_atk = scrapy.Field()
    sp_def = scrapy.Field()
    speed = scrapy.Field()
    total = scrapy.Field()
    pass
