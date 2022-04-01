# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class customImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        name = str(item.get('name')[0])
        number = str(item.get('number')[0])
        url_path = {'imagename': number + '_' + name}
        return [Request(u, meta=url_path) for u in urls]

    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url
        img_name = f'{request.meta["imagename"]}.jpg'
        return img_name


class PokemonPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("mypokemons.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS pokemons_tb""")
        self.curr.execute(""" create table pokemons_tb(
                        images blop,
                        number text,
                        name text,
                        type1 text,
                        type2 text,
                        hp text,
                        attack text,
                        defense text,
                        sp_atk text,
                        sp_def text,
                        speed text,
                        total text
                        ) """)

    def process_item(self, item, spider):

        self.store_db(item)
        return item

    def store_db(self,item):

        with open('img/'+ str(item['images'][0]['path']), 'rb') as f:
            data =f.read()

        if len(item['types'])==1:
            self.curr.execute("""insert into pokemons_tb values (?, ? , ?,?,'-', ? , ?,?,?, ? , ?,?)""",(
                data,
                item['number'][0],
                item['name'][0],
                item['types'][0],
                item['hp'][0],
                item['attack'][0],
                item['defense'][0],
                item['sp_atk'][0],
                item['sp_def'][0],
                item['speed'][0],
                item['total'][0]
                ))

            self.conn.commit()

        if len(item['types'])==2:
            self.curr.execute("""insert into pokemons_tb values (?, ? , ?,?,?, ? , ?,?,?, ? , ?,?)""",(
                data,
                item['number'][0],
                item['name'][0],
                item['types'][0],
                item['types'][1],
                item['hp'][0],
                item['attack'][0],
                item['defense'][0],
                item['sp_atk'][0],
                item['sp_def'][0],
                item['speed'][0],
                item['total'][0]
                ))

            self.conn.commit()
