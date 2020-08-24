from ebaysdk.shopping import Connection


if __name__ == '__main__':
    api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

    request = {
        'ItemID': '274013418704',
        
    }
    response = api.execute('GetSingleItem', request)
    with open('data_byitemID.xml', 'w') as f:
        f.write(response.text)
