import re

class ProcessingSearch:
    list_recomend = []
    list_product = []

    def __init__(self, product_walmart, product_chedraui, product_superaki):
        self.product_walmart = product_walmart
        self.product_chedraui = product_chedraui
        self.product_superaki = product_superaki

        print()
        print(product_walmart)
        print()
        print()
        print(product_chedraui)
        print()
        print()
        print(product_superaki)
        print()

    def proccesingProduct(self):
        products = []

        for i in range(len(self.product_walmart)):
            if self.product_walmart[i][1] != "0" and self.product_walmart[i][5] != '':
                products.append(self.product_walmart[i])

        for i in range(len(self.product_chedraui)):
            if self.product_chedraui[i][1] != "0" and self.product_chedraui[i][5] != '':
                products.append(self.product_chedraui[i])

        for i in range(len(self.product_superaki)):
            if self.product_superaki[i][1] != "0" and self.product_superaki[i][5] != '':
                products.append(self.product_superaki[i])

        for i in range(1, len(products)):
            for j in range(0, len(products) - i):

                try:
                    if (float(products[j + 1][5]) < float(products[j][5])):
                        aux = products[j]
                        products[j] = products[j + 1]
                        products[j + 1] = aux

                except:
                    print("Error de conversion")
                    print((products[j + 1][5]) + " -1- " + products[j + 1][5])
                    print((products[j + 1][5]) + " -2- " + products[j][5])

        size = len(products)

        if size > 3 or size == 3:
            if size > 3:
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))
                self.list_product = products

            if size == 3:
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))

        else:
            if size == 2:
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))

            else:
                if size == 1:
                    self.list_recomend.append(products.pop(0))

    def proccesingProductFilter(self, marca, producto, cantidad):
        products = []

        patron_mark = re.compile(r"" + str(marca) + "", re.IGNORECASE)
        patron_product = re.compile(r"" + str(producto) + "", re.IGNORECASE)
        patron_size = re.compile(r"" + str(cantidad) + "", re.IGNORECASE)

        for i in range(len(self.product_walmart)):
            if self.product_walmart[i][1] != "0" and self.product_walmart[i][5] != '':
                data1 = patron_mark.search(str(self.product_walmart[i][0]))
                data2 = patron_product.search(str(self.product_walmart[i][0]))
                data3 = patron_size.search(str(self.product_walmart[i][0]))

                if data1 != None and data2 != None and data3 != None:
                    products.append(self.product_walmart[i])

        for i in range(len(self.product_chedraui)):
            if self.product_chedraui[i][1] != "0" and self.product_chedraui[i][5] != '':
                data1 = patron_mark.search(str(self.product_chedraui[i][0]))
                data2 = patron_product.search(str(self.product_chedraui[i][0]))
                data3 = patron_size.search(str(self.product_chedraui[i][0]))

                if data1 != None and data2 != None and data3 != None:
                    products.append(self.product_chedraui[i])

        for i in range(len(self.product_superaki)):
            if self.product_superaki[i][1] != "0" and self.product_superaki[i][5] != '':
                data1 = patron_mark.search(str(self.product_superaki[i][0]))
                data2 = patron_product.search(str(self.product_superaki[i][0]))
                data3 = patron_size.search(str(self.product_superaki[i][0]))

                if data1 != None and data2 != None and data3 != None:
                    products.append(self.product_superaki[i])

        for i in range(1, len(products)):
            for j in range(0, len(products) - i):

                try:
                    if (float(products[j + 1][5]) < float(products[j][5])):
                        aux = products[j]
                        products[j] = products[j + 1]
                        products[j + 1] = aux

                except:
                    print("Error de conversion")
                    print((products[j + 1][5]) + " -1- " + products[j + 1][5])
                    print((products[j + 1][5]) + " -2- " + products[j][5])

        size = len(products)

        if size > 3 or size == 3:
            if size > 3:
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))
                self.list_product = products

            if size == 3:
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))

        else:
            if size == 2:
                self.list_recomend.append(products.pop(0))
                self.list_recomend.append(products.pop(0))

            else:
                if size == 1:
                    self.list_recomend.append(products.pop(0))

    def clearData(self):
        self.list_recomend = []
        self.list_product = []