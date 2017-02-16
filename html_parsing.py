__author__ = 'vera'

import urllib
import re

from  BeautifulSoup import *

#html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
url = raw_input('Enter url: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

span = soup('span')

sum = 0
for item in span:
    num = re.findall('([0-9]+)', str(item))
    sum = sum + int(num[0])

print 'Count ', sum

