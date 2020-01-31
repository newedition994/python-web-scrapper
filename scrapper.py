import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?crid=MWAMHV1I1182&keywords=sony+alpha+a7iii&qid=1580498985&sprefix=sony+al%2Caps%2C155&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1700):
        send_mail()

    print(converted_price)
    print(title.strip())


# establish a connection with GMail to send the mail
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # generate a password with you gmail account so you can login
    server.login('', '')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?crid=MWAMHV1I1182&keywords=sony+alpha+a7iii&qid=1580498985&sprefix=sony+al%2Caps%2C155&sr=8-3'

    msg = f"Subject: {subject}\n\n{body|"

    server.sendmail(
        ''  # who the email is from
        ''  # who the email was sent to
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()
