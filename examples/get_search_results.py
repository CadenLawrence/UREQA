#!/usr/bin/env python
import json
import zillow
import pprint
from flask import Flask
from flask import jsonify
from ratelimiter import RateLimiter
import requests
from contextlib import suppress


from bs4 import BeautifulSoup
import scrape as scrape
if __name__=="__main__":
    key = "X1-ZWz18fo3dwad57_2599m"
    postal_code = "43302"
    addresses = scrape.getAddresses()
    api = zillow.ValuationApi()
    
    for address in addresses: 
        
        rate_limiter = RateLimiter(max_calls=1, period=3)
        with rate_limiter:
            try:
                if address:
                    deep_results = api.GetDeepSearchResults(key, address, postal_code)
                    print(deep_results.get_dict().copy())
            except:
                pass
    app.run()