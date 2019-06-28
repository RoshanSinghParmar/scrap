# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 04:45:05 2019

@author: Roshan
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv






my_url ='https://www.youtube.com/results?search_query=science+videos'



client= uReq(my_url)
pg_html = client.read()
client.close()




pg_soup= soup(pg_html,"html.parser")




data=pg_soup.findAll('div',{"class":"yt-lockup-content"})
csv_file=open("done.csv","a",encoding="utf-8")
csv_writer=csv.writer(csv_file)


for d in data:

    pid = d.h3.a["href"]
    pid=pid.replace("/watch?v=","")
 
    title = d.h3.a["title"].replace(",","|")
  
    desc = d.div.next_sibling.next_sibling.text.replace(",","|")
    category = "Science And Technology"
    
     
    csv_writer.writerow([pid,title,desc,category])

csv_file.close()