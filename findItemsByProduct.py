from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError
if __name__ == '__main__':
    try:
        api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

        request = {
            'productId': {
                    '#text': '0190199380615',
                    '@attrs': {
                        'type': 'UPC'
                    }
                },
            'outputSelector': 'SellerInfo',
            'itemFilter': [
                {'name': 'ListingType', 'value': 'FixedPrice'},
                {'name': 'Condition', 'value': 'New',},
                {'name': 'Country', 'value': 'US Only',},
                {'name': 'topRatedListing', 'value': 'true',}
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
            if item.shippingInfo.get('shippingServiceCost'):
                print(f" ID: {id} Title: {item.title}, Price: {item.shippingInfo.shippingServiceCost.value}, Seller:{item.sellerInfo.sellerUserName}")
    except ConnectionError as e:
        print(e)
        print(e.response.ack)