import sys
import re

basic_info = {}
with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    for line in britain_file:
        m = re.match(r'\|(.+?) = (.+)', line)
        if m:
            basic_info[m.group(1)] = re.sub(r'\'{2,5}', '', m.group(2))

print(basic_info)
            