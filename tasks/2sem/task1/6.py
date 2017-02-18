# -*- coding: utf-8 -*-

import sys

for i in xrange(1, 101):
    print i,
print
for i in xrange(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print 'BazQux',
    elif i % 3 == 0:
        print 'Baz',
    elif i % 5 == 0:
        print 'Qux',
    else:
        print i,

