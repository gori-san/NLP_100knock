import sys
import re

with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    for line in britain_file:
        m = re.match(r'\[\[Category:.*\]\]', line)
        if m: print(line.strip('\n'))
