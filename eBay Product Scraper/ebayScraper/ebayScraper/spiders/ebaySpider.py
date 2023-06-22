import csv
import scrapy

Product_Name = input("put product name: ")
File_Name = input("put the file name: ")

class EbayspiderSpider(scrapy.Spider):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={Product_Name}&_sacat=0"
    name = "ebaySpider"
    allowed_domains = ["ebay.com"]
    start_urls = [url]
    dict = {
        "Name": 0,
        "Price": 0,
        "Link": 0,
        "From": 0,
        "Shipping": 0
    }

    with open(f"..\\..\\..\\{File_Name}.csv","w")as file:
        writer = csv.DictWriter(file, fieldnames=dict.keys())
        writer.writeheader()


    def parse(self, response):

        for products in response.css('div.s-item__info.clearfix'):
            if products.css('div.s-item__title span[role="heading"]::text').get() == "Shop on eBay":
                continue
            try:
                dic = {
                    "Name": products.css('div.s-item__title span[role="heading"]::text').get(),
                    "Price":  products.css('span.s-item__price::text').get(),
                    "Link": products.css('a.s-item__link').attrib['href'],
                    "From": products.css('span.s-item__location::text').get(),
                    "Shipping": products.css('span.s-item__shipping::text').get()
                }
                with open(f"..\\..\\..\\{File_Name}.csv", "a", newline='')as file:
                    writer = csv.DictWriter(file, fieldnames=dic.keys())
                    writer.writerow(dic)
            except:
                pass
            next_page = response.css('a.pagination__next.icon-link').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
    print("File created")