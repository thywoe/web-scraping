from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


url_page = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2."

page = urlopen(url_page)

soup = BeautifulSoup(page,"html.parser")

products = "".join([p.text for p in soup.find_all("a",href=True, attrs={'class':"_31qSD5"})])


print(products)  

with open("index.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([products, datetime.now()])


