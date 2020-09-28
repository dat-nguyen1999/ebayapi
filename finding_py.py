from ebaysdk.finding import Connection as Finding

ebay_api = Finding(
                            domain='svcs.ebay.com',
                            config_file=None,
                            appid="DatNguye-simpleca-PRD-0c8ee5576-eb7ef499",
                            siteid="EBAY-US"
                        )
a= ebay_api.execute("findItemsByProduct")
print()
