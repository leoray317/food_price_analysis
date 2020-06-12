import requests
from bs4 import BeautifulSoup
import lxml
import json
import pandas as pd

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie':'_ga=GA1.3.1401094577.1591692355; _gid=GA1.3.1354790245.1591692355; ASP.NET_SessionId=mjlg2fy3glc5fmrg1fi4vfwy',
'Host': 'agridata.coa.gov.tw',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

total_list=[]

url='https://agridata.coa.gov.tw/api/v1/AgriProductsTransType/?Start_time=107.07.01&End_time=108.05.09'



res = requests.get(url,headers = headers)
soup = BeautifulSoup(res.text,'lxml')
p = soup.find('p')

context_json = json.loads(p.text)
context = context_json['Data']


for g in context:
        l=[]
        if g['CropName'] == "茼蒿" and g['MarketName'] == '台北一':
            l.append(g['TransDate'])
            l.append(g['CropName'])
            l.append(g['Avg_Price'])
            l.append(g['Trans_Quantity'])
            print(l)
            total_list.append(l)
if l == []:
    print('沒茼蒿')
    

