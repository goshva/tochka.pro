#!/usr/bin/python3
#import re
#f = open("dict.txt", "r")
#nospace = f.read().strip()
#print(nospace)
#print(f.read())
#filtered = filter(f.strip, lines) 
#print(filtered.readlines())
with open('dict.txt') as infile, open('dictout.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
#print(outfile.read())