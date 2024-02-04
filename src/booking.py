import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import boto3
from botocore.exceptions import NoCredentialsError

list1 = ["Mont Saint Michel",
"St Malo",
"Bayeux",
"Le Havre",
"Rouen",
"Paris",
"Amiens",
"Lille",
"Strasbourg",
"Chateau du Haut Koenigsbourg",
"Colmar",
"Eguisheim",
"Besancon",
"Dijon",
"Annecy",
"Grenoble",
"Lyon",
"Gorges du Verdon",
"Bormes les Mimosas",
"Cassis",
"Marseille",
"Aix en Provence",
"Avignon",
"Uzes",
"Nimes",
"Aigues Mortes",
"Saintes Maries de la mer",
"Collioure",
"Carcassonne",
"Ariege",
"Toulouse",
"Montauban",
"Biarritz",
"Bayonne",
"La Rochelle"]

class BookingSpider(scrapy.Spider):
    # Name of your spider
    name = "booking"

    # Starting URL
    start_urls = ['https://www.booking.com/index.fr.html']

        # Parse function for form request
    def parse(self, response):
        for el in list1 :
            yield scrapy.FormRequest.from_response(
                response,
                formdata={'ss': el
                          },
                callback=self.after_search,
                meta = {'city':el} # Saving the city to symplify analysis
            )

    def after_search(self, response):
        for i in range (3,60,2): 
            urls = response.xpath(f'//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[{i}]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a')
            for url in urls:
                yield scrapy.Request(url.attrib["href"], callback=self.after_url, meta=response.meta) 

    def after_url(self, response):
        yield {
            'Address' : response.xpath('//*[@id="showMap2"]/span[1]/text()').get(),
            'ville' :  response.meta['city'],
            'name' : response.xpath('//*[@id="hp_hotel_name"]/div/h2/text()').get(),
            'description' : response.xpath('//*[@id="property_description_content"]/div/p/text()').get(),
            'latlong' : response.xpath('//*[@id="hotel_sidebar_static_map"]').attrib["data-atlas-latlng"],
            'note' : response.xpath('//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div[1]/text()').get(),
            "url" : response.request.url
        }



# Name of the file where the results will be saved
filename = "hotels.json"

# If file already exists, delete it before crawling (because Scrapy will concatenate the last and new results otherwise)
if filename in os.listdir('src/'):
    os.remove('src/' + filename)

# Declare a new CrawlerProcess with some settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/120.0.0.0',
    'LOG_LEVEL': logging.INFO,
    "AUTOTHROTTLE_ENABLED": True,
    'DOWNLOAD_DELAY': 5,
    "COOKIES_ENABLED": False,
    "FEEDS": {
        'src/' + filename: {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(BookingSpider)
process.start()