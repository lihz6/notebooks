#!/usr/bin/env python3

from sys import stdin
from collections import Counter

c = Counter()

for line in stdin:
    word, count = line.strip().split("\t")
    c.update({word: int(count)})

for word, count in c.items():
    print(word, count, sep="\t")
