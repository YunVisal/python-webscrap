from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

rate_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

book_title = list()
book_cover = list()
book_rate = list()
book_stock_status = list()
book_price = list()
for i in range(1, 51):
    base_url = 'https://books.toscrape.com'
    req = Request(f'{base_url}/catalogue/page-{i}.html', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    bs = BeautifulSoup(webpage, 'html')

    books_html = [i for i in bs.find_all(class_='product_pod')]

    for html in books_html:
        title = html.h3.string
        book_title.append(title)

        cover_url_html = html.find_all('img', class_='thumbnail')[0]
        cover_url = f"{base_url}/{cover_url_html['src'][2:]}"
        book_cover.append(cover_url)

        rate_html = html.find_all('p', class_='star-rating')[0]
        rate = rate_html['class'][1]
        book_rate.append(rate_dict[rate])

        price = html.find_all('p', class_='price_color')[0].string
        book_price.append(price)

        availability_html = html.find_all('p', class_='availability')[0]
        availability = availability_html['class'][0]
        book_stock_status.append(availability)

        print(f'Done: Page{i}-{title}----------------------------------------------')

book_dict = { 'Title': book_title, 'Cover Url': book_cover, 'Rate': book_rate, 'Price': book_price, 'Availability': book_stock_status  }
df = pd.DataFrame.from_dict(book_dict)
df.to_csv('book.csv', sep=',', encoding='utf-8')