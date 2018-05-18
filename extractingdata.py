import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


while True:
    url = input('Enter URL: ')
    if len(url) < 1: break


    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    # Other method of parsing XML tree, equivalent to line 16
    # counts = tree.findall('comments/comment/count')
    countsum = 0
    total = 0
    # Each item is a node and the attribute must be accessed using the dot
    # operator
    for item in counts:
        countsum += int(item.text)
        total += 1
    print("Count:", countsum)
    print("Sum:", total)
