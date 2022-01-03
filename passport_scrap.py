from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

req = Request('https://www.passportindex.org/byRank.php', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

bs = BeautifulSoup(webpage, 'html')

country_name_html = [i for i in bs.find_all(class_='name_country')]
country_name = list()
for country_html in country_name_html:
    country_name.append(country_html.span.string)

vff_html = [i for i in bs.find_all(class_='name_rank')]
vff = list()
for html in vff_html:
    vff.append(html.span.string)

vf_html = [i for i in bs.find_all(class_='vf')]
vf = list()
for html in vf_html:
    vf.append(html.string)

voa_html = [i for i in bs.find_all(class_='voa')]
voa = list()
for html in voa_html:
    voa.append(html.string)

vr_html = [i for i in bs.find_all(class_='vr')]
vr = list()
for html in vr_html:
    vr.append(html.string)

passportDict = { 'country': country_name, 'VFS': vff, 'rank_vf': vf, 'rank_voa': voa, 'rank_vr': vr }
df = pd.DataFrame.from_dict(passportDict)
print(df.head())