__author__ = 'vera'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.data.pr4e.org', 80))
s.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0 \n\n')

while True:
    data = s.recv(128)
    if len(data)<1:
        break
    print data

