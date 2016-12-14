#!/usr/bin/env python3
import sys
import requests
import re
from bs4 import BeautifulSoup
url=''
url2='&orderby=new'
total_page=60


csv_reader=open('data/100.csv','w+')
for page in range(1,total_page+1):
  res = requests.get(url+str(page)+url2)
  soup=BeautifulSoup(res.text,"html.parser")
  soup1=BeautifulSoup(str(soup.find_all("table",class_="auto-style1")),"html.parser")
  print(page)
  for cont in soup1.find_all("tr")[1:]:
    t=""
    for row in cont.findAll("td"):
      t+=row.text.strip()+","
    t=re.sub('[\s+]','',t)[:-1]
    t=t[:4]+","+t[4:]
    csv_reader.write(t+'\n')

csv_reader.close()
