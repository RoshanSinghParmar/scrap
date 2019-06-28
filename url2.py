# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 04:48:56 2019

@author: Roshan
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv






my_url2='https://www.youtube.com/results?search_query=trip+to+london'



client= uReq(my_url2)
pg_html2 = client.read()
client.close()




pg_soup2= soup(pg_html2,"html.parser")




data2=pg_soup2.findAll('div',{"class":"yt-lockup-content"})
csv_file=open("done.csv","a",encoding="utf-8")
csv_writer=csv.writer(csv_file)

for d in data2:

    pid = d.h3.a["href"]
    pid=pid.replace("/watch?v=","")
 
    title = d.h3.a["title"].replace(",","|")
  
    desc=d.div.text
    category = "Travels"
    
     
    csv_writer.writerow([pid,title,desc,category])

csv_file.close()