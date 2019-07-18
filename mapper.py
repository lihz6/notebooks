#!/usr/bin/env python3

from sys import stdin
from collections import Counter

c = Counter()

for line in stdin:
    c.update(line.strip().split())

for word, count in c.items():
    if word and count:
        print(word, count, sep="\t")
