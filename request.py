##########################
#
# GET REQUEST
#
##########################

import urllib.request

req = urllib.request.Request(f'https://pythonprogramming.net/', headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)

print(res.read())


##########################
#
# POST REQUEST
#
##########################

import urllib.parse

url = 'https://pythonprogramming.net/'
values = {'q': 'python'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
res = urllib.request.urlopen(req)

print(res.read())