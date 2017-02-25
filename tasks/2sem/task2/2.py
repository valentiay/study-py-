# -*- coding: utf-8 -*-

import sys

c200 = 0
c300 = 0
cOther = 0
for line in sys.stdin:
    code = int(line.split('"')[2][1:4])
    if code == 200:
        c200 += 1
    elif code in xrange(300, 310):
        c300 += 1
    else:
        cOther += 1
print c200
print c300
print cOther
print c200 + c300 + cOther

