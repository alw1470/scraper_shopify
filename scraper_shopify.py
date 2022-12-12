import requests
import json
import dataset


class  ShopifyScraper():
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def dowloadjson(self, page):
        r = requests.get(self.baseurl + f'products.json?limit=250&page={page}', timeout=5)
        if r.status_code !=200:
            print('Error Status Code: ', r.status_code)
        if len(r.json()['products']):
            data = r.json()['products']
            return data
        else:
            return

    def parsejson(self, jsondata):
        products = []
        for prod in jsondata:
            mainid = prod['id']
            title = prod['title']
            vendor = prod['vendor']
            product_type = prod['product_type']
            for v in prod['variants']:
                item = {
                    'id': mainid,
                    'title': title,
                    'vendor': vendor,
                    'product_type': product_type,
                    'varid': v['id'],
                    'vartitle': v['title'],
                    'sku': v['sku'],
                    'price': v['price'],
                    'option1': v['option1'],
                    'option2': v['option2'],
                    'option3': v['option3'],
                    'product_id': v['product_id'],
                    'available': v['available'],
                }
                products.append(item)
        return products

    def main():
        url = ShopifyScraper('#Aqui cambias la url de Shopify')
        results = []
        for page in range(1,47): ## Aqui se debe cambiar el rango en base a las páginas
            data = url.dowloadjson(page)
            print('Paginas: ', page)
            try:
                results.append(url.parsejson(data))
            except:
                print(f'Completado, total de páginas = {page -1 }')
        return results

    if __name__ == '__main__':
        db = dataset.connect('sqlite:///scraper.db') ### Aqui hay que poner una base de datos que se quiera.
        table = db.create_table('scraper', primary_id = 'varid')
        products = main()
        totals = [ item for i in products for item in i ]

        for p in totals:
            if not table.find_one(varid=p['varid']):
                table.insert(p)
                print('Producto nuevo añadido')                    







            
