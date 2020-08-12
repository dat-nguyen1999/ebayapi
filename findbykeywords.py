from ebaysdk.finding import Connection

if __name__ == '__main__':
    api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

    request = {
        'keywords': 'lord of the rings',
        'outputSelector': 'SellerInfo',
        'itemFilter': [
            {'name': 'Condition', 'value': 'New'}
        ],
        'paginationInput': {
            'entriesPerPage': 50,
            'pageNumber': 24
        },
        'sortOrder': 'PricePlusShippingLowest'
    }
    response = api.execute('findItemsByKeywords', request)
    with open('data.xml', 'w') as f:
        f.write(response.text)
    id = 0
    for item in response.reply.searchResult.item:
        id += 1
        print(f" ID: {id} Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}, Seller:{item.sellerInfo.sellerUserName}")