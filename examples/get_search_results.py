#!/usr/bin/env python
import json
import zillow
import pprint
from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')
def output():
    return r.content
if __name__=="__main__":
    key = "X1-ZWz18fo3dwad57_2599m"

    #address = "3400 Pacific Ave., Marina Del Rey, CA"
    #postal_code = "43302"

    #api = zillow.ValuationApi()
    #data = api.GetSearchResults(key, address, postal_code)

    #pp = pprint.PrettyPrinter(indent=4)
    
    #detail_data = api.GetZEstimate(key, data.zpid)

    #comp_data = api.GetComps(key, data.zpid)
    
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    with requests.Session() as s:
        zipcode='43302'
        url = 'https://www.zillow.com/homes/for_sale/'+ zipcode + '_rb/?fromHomePage=true&shouldFireSellPageImplicitClaimGA=false&fromHomePageTab=buy'
        r = s.get(url, headers=req_headers)

    soup = BeautifulSoup(r.content, 'lxml')
    price = soup.find('span', {'class': 'zsg-photo-card-price'}).text
    info = soup.find('span', {'class': 'zsg-photo-card-info'}).text
    address = soup.find('span', {'itemprop': 'address'}).text

    #deep_results = api.GetDeepSearchResults(key, "1920 1st Street South Apt 407, Minneapolis, MN", "55454")
    app.run()