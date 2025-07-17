import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("RECIPIENT_EMAIL")
URL = os.getenv("SEARCH_URL")
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def fetch_products():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('h2 a span')
    return [title.get_text() for title in titles[:5]]

def send_email(products):
    msg = EmailMessage()
    msg['Subject'] = 'New Amazon Products Alert!'
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    body = "\n".join(products)
    msg.set_content(f"Top 5 results:\n\n{body}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
    print("✅ Email sent!")

def main():
    products = fetch_products()
    send_email(products)

if __name__ == '__main__':
    main()