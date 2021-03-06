from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import xml.etree.ElementTree as ET
try:
    api = Finding(config_file='ebay.yaml')
    request = {
        'keywords': 'Lenovo Legion Y540 15.6 i7-9750H 16GB RAM 256GB SSD GTX 1660Ti 6GB',
        'categoryId': '177',
        'outputSelector': 'SellerInfo',
        'itemFilter': [
            {'name': 'ListingType', 'value': 'FixedPrice'},
            {'name': 'Condition', 'value': 'New' },
            {'name': 'Country', 'value': 'US Only'}
        ],
        'paginationInput': {
            'entriesPerPage': 50,
            'pageNumber': 1
        },
        'sortOrder': 'PricePlusShippingLowest'
    }
    response = api.execute('findItemsAdvanced', request)
    #print(response.dict())
    root = ET.fromstring(response.text)
    tree = ET.ElementTree(root)
    tree.write("data_advanced.xml")
    # with open('data_advanced.xml', 'w') as f:
    #     f.write(response.text)
except ConnectionError as e:
    print(e)
    print(e.response.dict())