from ebaysdk.trading import Connection

if __name__ == '__main__':
    try:
        api = Connection(config_file='ebay.yaml')
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        log.error('Attempting to get an API object failed with %s', e)

    acitvelist = api.execute('GetMyeBaySelling', {'ActiveList': True,
                                              'DetailLevel': 'ReturnAll',
                                              'PageNumber': 1})
    print(acitvelist)