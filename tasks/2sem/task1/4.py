# -*- coding: utf-8 -*-

import sys

interval = [(x*2 + 1)*(1 if x % 2 == 0 else -1) for x in xrange(10)]
sum = 0
for x in interval:
    sum += 4.0/x
print sum

