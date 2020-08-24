from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError
if __name__ == '__main__':
    try:
        api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

        request = {
            'productId': {
                    '#text': '9780439784542',
                    '@attrs': {
                        'type': 'ISBN'
                    }
                },
            'outputSelector': 'SellerInfo',
            'itemFilter': [
                {'name': 'ListingType', 'value': 'FixedPrice'},
                {'name': 'Condition', 'value': 'New',},
                {'name': 'Country', 'value': 'US Only',}
            ],
            'paginationInput': {
                'entriesPerPage': 50,
                'pageNumber': 1
            },
            'sortOrder': 'PricePlusShippingLowest'
        }
        response = api.execute('findItemsByProduct', request)
        with open('data_byProductID.xml', 'w') as f:
            f.write(response.text)
        id = 0
        for item in response.reply.searchResult.item:
            id += 1
            print(f" ID: {id} Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}, Seller:{item.sellerInfo.sellerUserName}")
    except ConnectionError as e:
        print(e)
        print(e.response.ack)