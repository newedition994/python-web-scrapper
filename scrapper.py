import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?crid=MWAMHV1I1182&keywords=sony+alpha+a7iii&qid=1580498985&sprefix=sony+al%2Caps%2C155&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())
