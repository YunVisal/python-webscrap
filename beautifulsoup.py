import bs4 as bs
import urllib.request

req = urllib.request.Request(f'https://pythonprogramming.net/', headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)

soup = bs.BeautifulSoup(res, 'html')

print(soup)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)

print(soup.find_all('a'))
for url in soup.find_all('a'):
    print(url.get('href'))

footer = soup.footer
print(footer.find_all('a', class_="grey-text"))