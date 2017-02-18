# -*- coding: utf-8 -*-

import sys

line = sys.stdin.readline()
line = line.strip()

n = int(line)
factorial = 1
for i in xrange(1, n + 1):
    factorial *= i

print factorial

