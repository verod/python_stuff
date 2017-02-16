__author__ = 'vera'

import json
import urllib

SERVICE_URL = 'http://python-data.dr-chuck.net/geojson?'

while True:
    location = raw_input("Enter location: ")
    if len(location)< 1: break

    url = SERVICE_URL + urllib.urlencode({'sensor':'false', 'address':location})
    print 'Retrieving...', url

    data = urllib.urlopen(url).read()
    print 'Retrieved:', len(data), 'characters'

    try:
        js = json.loads(data)
    except:
        print 'Error loading json data'
        js = 'None'

    placeid = js['results'][0]['place_id']
    print 'Place id:', placeid
    #print json.dumps(js, indent=4)