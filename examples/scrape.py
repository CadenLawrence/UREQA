import requests
import sys
from bs4 import BeautifulSoup
def getAddresses():
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    addresses = []
    newaddresses = []
    prices = []
    newprices = []
    with requests.Session() as s:
        url = 'https://www.zillow.com/homes/for_sale/Marion-OH-43302/'
        r = s.get(url, headers=req_headers)
        print(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    pages = soup.find('li',{'class': 'zsg-pagination-ellipsis'}).find_next('li').contents[0].text
    pages= int(pages)
    page_num=2
    for li in soup.find_all('div', {'class': 'zsg-photo-card-caption'}):
            try:
                address = li.find('span', {'class': 'zsg-photo-card-address'}).text
                price = li.find('span', {'class': 'zsg-photo-card-price'}).text
                price = price.strip('$')
                price = price.replace(',','')
                price = int(price)
                if(address!='Sign in for details'):
                    if(price<=65000):
                        addresses.append(address)             
            except:
                pass
                #print('An error occured')
    while page_num != pages:
        with requests.Session() as s:
            url2 = 'https://www.zillow.com/homes/for_sale/Marion-OH-43302/'+ str(page_num) +'_p'
            r = s.get(url2, headers=req_headers)
            print(url2)
        soup2 = BeautifulSoup(r.content, 'html.parser')
        page_num = page_num + 1
        for li in soup2.find_all('div', {'class': 'zsg-photo-card-caption'}):
            try:
                address = li.find('span', {'class': 'zsg-photo-card-address'}).text
                price = li.find('span', {'class': 'zsg-photo-card-price'}).text
                price = price.strip('$')
                price = price.replace(',','')
                price = int(price)
                if(address!='Sign in for details'):
                    if(price<=65000):
                        addresses.append(address)
            except:
                pass
                #print('An error occured')
    with open('C:\\Users\\balle\\Desktop\\python-zillow\\examples\\listfile.txt', 'r+') as text:
        for address in addresses:
            if not any(address in line for line in text):
                text.write(address+"\n")
                newaddresses.append(address)
            else:
                print("Not unique")
    return newaddresses