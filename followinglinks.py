# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Iterate (count) times
for i in range(0, count + 1, 1):
    print("Retrieving: ", url)
    pos_html = urllib.request.urlopen(url, context=ctx).read()
    pos_soup = BeautifulSoup(pos_html, 'html.parser')
    pos_tags = pos_soup('a')
    # Set new position link
    url = pos_tags[position].get("href", None)
