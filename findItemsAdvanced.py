from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

try:
    api = Finding(config_file='ebay.yaml')
    request = {
        'keywords': 'harry potter and the half blood prince',
        'categoryId': '171219',
        'outputSelector': 'SellerInfo',
        'itemFilter': [
           
            {'name': 'ListingType', 'value': 'FixedPrice'}
        ],
        'paginationInput': {
            'entriesPerPage': 10,
            'pageNumber': 1
        },
        'sortOrder': 'PricePlusShippingLowest'
    }
    
    response = api.execute('findItemsAdvanced', request)
    #print(response.dict())
    with open('data_advanced.xml', 'w') as f:
        f.write(response.text)
except ConnectionError as e:
    print(e)
    print(e.response.dict())