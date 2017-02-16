__author__ = 'vera'

import urllib
import re
from BeautifulSoup import *

pos = 0 # position to start
i = 0 # variable to count iteration
count = 0 # number of iterations

#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'

while i <= int(count):
    if i == 0:
        url = raw_input('Enter URL: ')
        pos = raw_input('Enter possition: ')
        count = raw_input('Enter count: ')
    print 'Retrieving: ', url
    name = re.findall('known_by_([a-zA-Z]+)\.html',str(url))
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    href = soup('a')

    url = re.findall('href="(.+)"',str(href[int(pos)-1]))[0]

    if i == int(count):
        print 'Last name in sequence is:',name[0]

    i = i+1