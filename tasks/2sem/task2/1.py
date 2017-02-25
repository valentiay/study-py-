# -*- coding: utf-8 -*-

import sys

counter = 0
for line in sys.stdin:
    if line.split('"')[5] == 'Go-http-client/1.1':
        counter += 1
print counter

