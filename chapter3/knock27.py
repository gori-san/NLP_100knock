import sys
import re

basic_info = {}
with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    for line in britain_file:
        m = re.match(r'\|(.+?) = (.+)', line)
        if m:
            removed = re.sub(r'\'{2,5}', '', m.group(2))
            removed = re.sub(r'\[\[(.+\|)*(.+?)\]\]', r'\2', removed)
            basic_info[m.group(1)] = removed

print(basic_info)
            