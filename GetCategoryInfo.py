from ebaysdk.shopping import Connection


if __name__ == '__main__':
    api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

    request = {
        'CategoryID': '171219',
        
    }
    response = api.execute('GetCategoryInfo', request)
    with open('data_byCategoryID.xml', 'w') as f:
        f.write(response.text)
