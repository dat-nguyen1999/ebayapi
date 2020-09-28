from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
try:
    ebay_api = Finding(
        domain='svcs.ebay.com',
        config_file=None,
        appid='DatNguye-simpleca-PRD-0c8ee5576-eb7ef499',
        siteid='EBAY-US'
    )
except ConnectionError as e:
    print(e)
    print(e.response.dict())
request = {
            'productId': {
                    '#text': '978043978454',
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
response = ebay_api.execute('findItemsByProduct', request)
with open('data_test.xml', 'w') as f:
    f.write(response.text)
"""
https://svcs.ebay.com/services/search/FindingService/v1?
   OPERATION-NAME=findItemsByProduct&
   SERVICE-VERSION=1.0.0&
   SECURITY-APPNAME=DatNguye-simpleca-PRD-0c8ee5576-eb7ef499&
   RESPONSE-DATA-FORMAT=XML&
   REST-PAYLOAD&
   paginationInput.entriesPerPage=2&
   productId.@type=ReferenceID&
   productId=53039031&
   &itemFilter(0).name=topRatedListing
    &itemFilter(0).value=true




"""