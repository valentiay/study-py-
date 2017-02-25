# -*- coding: utf-8 -*-

import sys

mac = 0
ubu = 0
win = 0
oth = 0
for line in sys.stdin:
    userAgent = line.split('"')[5]
    if userAgent.find('Windows') != -1:
        win += 1
    elif userAgent.find('Ubuntu') != -1:
        ubu += 1
    elif userAgent.find('Macintosh') != -1:
        mac += 1
    else:
        oth += 1
dic = [(win, "Windows:"), (ubu, "Ubuntu:"), (oth, "Unknown:"), (mac, "OS X: ")]
dic.sort()
for i in dic:
    print i[1], i[0]

