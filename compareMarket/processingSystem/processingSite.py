import re
from bs4 import BeautifulSoup
from compareMarket.processingSystem.downloadSite import DownloadSite


class ProcessingSite:
    processing_product_walmart = []
    processing_product_chedraui = []
    processing_product_superaki = []

    def __init__(self, product_walmart, product_chedraui, product_superaki):
        self.product_walmart = product_walmart
        self.product_chedraui = product_chedraui
        self.product_superaki = product_superaki

    def processingWalmart(self):
        patron_name = re.compile(r"(>.*<)")
        patron_price = re.compile(r"(>.*<)")
        patron_image = re.compile(r"(src=\"https:\/\/.*\" srcset)")
        patron_link = re.compile(r"(href=\".*\"><)")
        patron_price_analizer = re.compile(r"([0-9]*[\,]*[0-9]+[\.0-9]*)")

        for i in range(len(self.product_walmart)):
            name = patron_name.findall(str(self.product_walmart[i][0]))
            price = patron_price.findall(str(self.product_walmart[i][1]))
            price_analizer = patron_price_analizer.findall(str(price))
            image = patron_image.findall(str(self.product_walmart[i][2]))
            link = patron_link.findall(str(self.product_walmart[i][3]))

            name = str(name)

            name = name[3:(len(name) - 3)]

            if (price == None or price == []):
                price = "0"

            else:
                price = str(price)
                price = price[3:(len(price) - 3)]

            price_analizer = str(price_analizer)
            price_analizer = price_analizer[2:(len(price_analizer) - 2)]

            if (image == None or image == []):
                image = "https://www.urveinmobiliaria.es/web_recursos/imagenes/sin_foto.png?auto=compress&cs=tinysrgb&h=650&w=940"

            else:
                image = str(image)
                image = image[7:-9]

            link = str(link)
            link = "https://super.walmart.com.mx" + link[8:(len(link) - 5)]

            price_analizer = price_analizer.replace(",", "")
            self.processing_product_walmart.append([name, price, image, link, "Walmart", str(price_analizer)])

    def processingChedraui(self):
        patron_name = re.compile(r"(>.*<)")
        patron_price = re.compile(r"(>.*<)")
        patron_image = re.compile(r"(src=\".*\" )")
        patron_link = re.compile(r"(href=\".*\"><a)")

        for i in range(len(self.product_chedraui)):
            name = patron_name.findall(str(self.product_chedraui[i][0]))
            price_processing = BeautifulSoup(str(self.product_chedraui[i][1]), features="lxml")
            integer = price_processing.find("span", class_="vtex-product-summary-2-x-currencyInteger")
            fraction = price_processing.find("span", class_="vtex-product-summary-2-x-currencyFraction")

            price_integer = patron_price.findall(str(integer))
            price_fraction = patron_price.findall(str(fraction))

            image = patron_image.findall(str(self.product_chedraui[i][2]))
            link = patron_link.findall(str(self.product_chedraui[i][3]))

            name = str(name)
            name = name[3:(len(name) - 4)]

            if price_integer is None or price_fraction is None:
                price = "0"

            else:
                price = str(price_integer[0][1:-1])
                if len(price_fraction) > 0:
                    price += "." + str(price_fraction[0][1:-1])

            if image == None or image == []:
                image = "https://www.urveinmobiliaria.es/web_recursos/imagenes/sin_foto.png?auto=compress&cs=tinysrgb&h=650&w=940"

            else:
                image = str(image)
                image = "https://www.chedraui.com.mx" + image[7:(len(image) - 4)]

            link = "https://www.chedraui.com.mx" + str(link[0][6:-4])

            self.processing_product_chedraui.append([name, "$" + price, image, link, "Chedraui", price])
            print()
            print([name, "$" + price, image, link, "Chedraui", price])
            print()


    def processingSuperAki(self):
        patron_name = re.compile(r"(\"\">.*<\/a)")
        patron_price = re.compile(r"( \$.*\s)")
        patron_image = re.compile(r"(src=\".*\")")
        patron_link = re.compile(r"(href=\".*\" )")
        patron_price_analizer = re.compile(r"([0-9]*[\,]*[0-9]+[\.0-9]*)")

        for i in range(len(self.product_superaki)):
            name = patron_name.findall(str(self.product_superaki[i][0]))
            price = patron_price.findall(str(self.product_superaki[i][1]))
            price_analizer = patron_price_analizer.findall(str(price))
            image = patron_image.findall(str(self.product_superaki[i][2]))
            link = patron_link.findall(str(self.product_superaki[i][3]))

            name = str(name)
            name = name[5:(len(name) - 5)]

            if (price == None or price == []):
                price = "0"

            else:
                price = str(price)
                price = price[3:(len(price) - 4)]

            price_analizer = str(price_analizer)
            price_analizer = price_analizer[2:(len(price_analizer) - 2)]

            if (image == None or image == []):
                image = "https://www.urveinmobiliaria.es/web_recursos/imagenes/sin_foto.png?auto=compress&cs=tinysrgb&h=650&w=940"

            else:
                image = str(image)
                image = "https://" + image[9:(len(image) - 3)]

            link = str(link)
            link = "https://www.superaki.mx/" + link[8:(len(link) - 4)]

            price_analizer = price_analizer.replace(",", "")
            self.processing_product_superaki.append([name, price, image, link, "SuperAki", str(price_analizer)])


    def clearData(self):
        self.processing_product_walmart = []
        self.processing_product_chedraui = []
        self.processing_product_superaki = []
