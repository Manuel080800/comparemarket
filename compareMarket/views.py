from django.shortcuts import render
import time
# Create your views here.

def index(request):
    return render(request, 'compareMarket/index.html')

def search(request):
    search = request.GET.get('productSearch')
    filter = request.GET.get('filterActive')
    filter_W = request.GET.get('searchWalmart')
    filter_C = request.GET.get('searchChedraui')
    filter_S = request.GET.get('searchSuperAki')
    mark = request.GET.get('productBrand')
    product = request.GET.get('productName')
    size = request.GET.get('productAmount')

    if (search == ""):
        search = "None"

    if (filter == None):
        filter = "Off"

    if (filter_W == None):
        filter_W = "Off"

    if (filter_C == None):
        filter_C = "Off"

    if (filter_S == None):
        filter_S = "Off"

    mark = ".*"
    product = ".*"
    size = ".*"

    from compareMarket.processingSystem.downloadSite import DownloadSite
    site = DownloadSite(search, 1)
    site.clearData()

    if filter_W == "on":
        inicio = time.time()
        site.download_walmart()
        print("W 1 - " + str(time.time() - inicio))

    if filter_C == "on":
        inicio = time.time()
        site.download_chedraui()
        print("C 1 - " + str(time.time() - inicio))

    if filter_S == "on":
        inicio = time.time()
        site.download_superaki()
        print("S 1 - " + str(time.time() - inicio))

    from compareMarket.processingSystem.processingSite import ProcessingSite
    processing = ProcessingSite(site.list_product_walmart, site.list_product_chedraui, site.list_product_superaki)
    processing.clearData()

    if filter_W == "on":
        inicio = time.time()
        processing.processingWalmart()
        print("W 2 - " + str(time.time() - inicio))

    if filter_C == "on":
        inicio = time.time()
        processing.processingChedraui()
        print("C 2 - " + str(time.time() - inicio))

    if filter_S == "on":
        inicio = time.time()
        processing.processingSuperAki()
        print("S 2 - " + str(time.time() - inicio))


    from compareMarket.processingSystem.processingSearch import ProcessingSearch
    analizer = ProcessingSearch(processing.processing_product_walmart, processing.processing_product_chedraui,
                                processing.processing_product_superaki)
    analizer.clearData()

    if filter == "Off":

        analizer.proccesingProduct()
        context = {'products': analizer.list_product,
                   'select': analizer.list_recomend,
                   'name': search}

    else:
        analizer.proccesingProductFilter(mark, product, size)
        context = {'products': analizer.list_product,
                   'select': analizer.list_recomend,
                   'name': search}

    return render(request, 'compareMarket/resultados.html', context)