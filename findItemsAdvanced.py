from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

try:
    api = Finding(config_file='ebay.yaml')
    response = api.execute('findItemsAdvanced', {'keywords': 'Python'})
    print(response.dict())
except ConnectionError as e:
    print(e)
    print(e.response.dict())