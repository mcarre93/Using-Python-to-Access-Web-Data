import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    print('Count:', len(info))
    # print(info)
    sum = 0
    total = 0
    for item in info['comments']:
        sum += int((item["count"]))
        total += 1

    print('Count:', total)
    print('Sum:', sum)
