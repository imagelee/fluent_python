import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
"""
with open(sys.argv[1], encoding='utf8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # ugly;
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
"""
# use setdefault do the same thing;

with open(sys.argv[1], encoding='utf8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)


# use defaultdict
import collections

index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # bug
            # index.get(word).append(location)
            index[word].append(location)

            # calling __missing__ before __getitem__.
            # __missing__ function deal with the missing key.


# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])




