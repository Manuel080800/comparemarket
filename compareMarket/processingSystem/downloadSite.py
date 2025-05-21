from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient

class DownloadSite:

    token = "059318f6980445f881323b408c7d9cc0"
    list_product_walmart  = []
    list_product_chedraui = []
    list_product_superaki = []

    def __init__(self, search, page):

        search = search.replace(" ", "%20")
        self.url_walmart = "https://super.walmart.com.mx/productos?Ntt=" + search
        # "https://www.chedraui.com.mx/leche?_q=leche&map=ft&page=1"
        self.url_chedraui = "https://www.chedraui.com.mx/" + search + "?_q=" + search + "&map=ft&page=1"
        print(self.url_chedraui)
        search = search.replace("%20", "+")

        self.url_superaki = "https://www.superaki.mx/search?page=" + str(page) + "&q=" + search + "+super-aki-montejo-suc2"

    def download_walmart(self):

        try:
            download_walmart = ScrapingAntClient(token=self.token)

            page_content_walmart = download_walmart.general_request(self.url_walmart, proxy_country = 'US').content

            soup_walmart = BeautifulSoup(page_content_walmart, features="lxml")
            product_walmart = soup_walmart.find_all("div", class_= "h-100 pb1-xl pr4-xl pv1 ph1")
            print(len(product_walmart))

            for i in range(len(product_walmart)):
                soup_processing = BeautifulSoup(str(product_walmart[i]), features="lxml")
                name = soup_processing.find(attrs={"data-automation-id": "product-title"})
                # data - automation - id = "product-title"
                price = soup_processing.find("div", class_="mr1 mr2-xl lh-copy b black f5 f4-l")
                image = soup_processing.find("img", class_="absolute")
                link = soup_processing.find("a", class_="absolute w-100 h-100 z-1 hide-sibling-opacity")
                self.list_product_walmart.append([name, price, image, link])
                # print("IMPRIMIENDO LO DE IMAGEN")
                # print(image)
                # print("FINALIZA IMPRESION")


        except:
            print("No se encontró la información solicitada en Walmart o se produjo un error.")
            self.list_product_walmart = []


    def download_chedraui(self):

        try:
            download_chedraui = ScrapingAntClient(token=self.token)

            page_content_chedraui = download_chedraui.general_request(self.url_chedraui).content

            soup_chedraui = BeautifulSoup(page_content_chedraui, features="lxml")
            product_chedraui = soup_chedraui.find_all("section", class_="vtex-product-summary-2-x-container")

            for i in range(len(product_chedraui)):
                soup_processing = BeautifulSoup(str(product_chedraui[i]), features="lxml")
                name = soup_processing.find("span", class_="vtex-product-summary-2-x-productBrand")
                price = soup_processing.find("span", class_="vtex-product-summary-2-x-currencyContainer")
                image = soup_processing.find("img", class_="vtex-product-summary-2-x-imageNormal")
                link = soup_processing.find("a", class_="vtex-product-summary-2-x-clearLink")
                self.list_product_chedraui.append([name, price, image, link])
                print([name, price, image, link])
        except:
            print("No se encontró la información solicitada en Chedraui o se produjo un error.")
            self.list_product_chedraui = []

    def download_superaki(self):

        try:
            download_superaki = ScrapingAntClient(token=self.token)

            page_content_superaki = download_superaki.general_request(self.url_superaki).content

            soup_superaki = BeautifulSoup(page_content_superaki, features="lxml")
            product_superaki = soup_superaki.find_all("div", class_="col-12 col-sm-6 col-md-6 col-lg-3 xs-horizontal product-card-shop")

            for i in range(len(product_superaki)):
                soup_processing = BeautifulSoup(str(product_superaki[i]), features="lxml")
                name = soup_processing.find("p", class_="text-normal")
                price = soup_processing.find("div", class_="card-aki-price")
                image = soup_processing.find("div", class_="card-aki-image")
                link = soup_processing.find("p", class_="text-normal")
                self.list_product_superaki.append([name, price, image, link])
            # print(self.list_product_superaki)

        except:
            print("No se encontró la información solicitada en SuperAki o se produjo un error.")
            self.list_product_superaki = []

    def clearData(self):
        self.list_product_walmart = []
        self.list_product_chedraui = []
        self.list_product_superaki = []
