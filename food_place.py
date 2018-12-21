from flask import Flask,render_template ,request
import requests
import time
import json
from bs4 import BeautifulSoup as bs

url = "https://map.naver.com/search2/local.nhn?query=강남역+맛집&page=3&type=SITE_1&queryRank=0&re=1&siteSort=0&menu=location&searchCoord=&sm=clk&mpx=09680640:37.4982913,127.0279173:Z11:0.0163771,0.0136893"


headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0",
        "Referer":"https://map.naver.com/?query=%EA%B0%95%EB%82%A8%EC%97%AD+%EB%A7%9B%EC%A7%91&type=SITE_1&queryRank=0"
        }
headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01"
    "Accept-Encoding" : "gzip, deflate, br"
    "Accept-Language" : "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    "Connection" : "keep-alive"
    "Cookie" : "NNB=Q2L2UGV63MNFY; npic=0kShEp…11A3AC2226A7F66CF323F6855114B"
    "Host" : "map.naver.com"
    "Referer" : "https://map.naver.com/?query=%…%A7%91&type=SITE_1&queryRank=0"
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
    "X-Requested-With" : "XMLHttpRequest"}    

    
response = requests.get(url,headers = headers).text

print(response)