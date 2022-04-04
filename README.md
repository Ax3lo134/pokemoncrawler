This project is a web scraper that generates a database of pokemon listed on https://pokemondb.net. The data are:
name, number, picture, stats of each pokemon.

I created a default scrapy project. in pokemon/pokemon/items.py I have added each item that will receive the data. 
pokemon/pokemon/spiders/pokemon_spider.py is the web crawler itself. For data storage, in pokemon/pokemon/pipelines.py I created a 
custom object for downloading the jpg images. Its names contain the number and name of each pokemon.
I also created a pipeline to send the scraped items in a SQL database.

For a simple view of the data, I chose to create a csv file: pokemon / items.csv.
The SQL database is pokemon / mypokemons.db. It can be accessed on a dedicated software or
in any browser at www.sqliteonline.com. After opening the website, in the left corner find the "file" button -> open db, 
select the downloaded database. After importing the file, write in the code line "SELECT * from 'pokemons_tb';" and click "RUN" button.

Downloaded photos are also saved in pokemon / img if you only want to view the images.
