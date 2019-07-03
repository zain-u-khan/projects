from lxml import html
import requests
from bs4 import BeautifulSoup
import itertools
import csv


for s in range(100):
    r=requests.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax&page={}".format(s))
    soup=BeautifulSoup(r.text,'html.parser')
    name_box=soup.findAll('div',attrs={"class":"_1vC4OE _2rQ-NK"})
    name1_box=soup.findAll('div',attrs={"class":"_3wU53n"})
    for (th,th1) in zip(name_box,name1_box):
        a=th.text.strip()
        b=th1.text.strip()
        print(b,a)
        with open('flipkart.csv','a') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow([a,b])


