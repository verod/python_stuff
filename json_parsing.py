__author__ = 'vera'

import urllib
import json

url = raw_input("Enter location:")
print "Retrieving...", url
jsondata = urllib.urlopen(url).read()
print "Retrieved: ", len(jsondata), " characters"
try:
    data = json.loads(jsondata)

except:
    print "Something went wrong when loading json data"
    exit()

sum = 0
count = 0
for comment in data['comments']:
    sum = sum + int(comment['count'])
    count = count + 1

print "Counts: ", count
print "Sum: ", sum