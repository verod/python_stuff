__author__ = 'vera'

import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location:")
print "Retrieving...", url
data = urllib.urlopen(url).read()

tree = ET.fromstring(data)
comments = tree.findall('comments')[0].findall('comment')

count = 0
sum = 0
for comment in comments:
    c = comment.find('count').text
    sum = sum + int(c)
    count = count + 1

print 'Count: ', count
print 'Sum: ', sum