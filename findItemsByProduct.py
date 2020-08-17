from ebaysdk.finding import Connection

if __name__ == '__main__':
    api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

    request = {
        'productId': {
                '#text': '164252608354',
                '@attrs': {
                    'type': 'ReferenceID'
                }
            },
        'outputSelector': 'SellerInfo',
        'itemFilter': [
           
            {'name': 'ListingType', 'value': ['FixedPrice', 'StoreInventory']}
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