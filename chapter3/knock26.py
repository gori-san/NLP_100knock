import sys
import re

pattern = re.compile(r'^\|(.+?)\s=\s(.+?)(?=\n(\||\}))', re.MULTILINE | re.DOTALL)
pattern_emphasis = re.compile(r'\'{2,5}', re.MULTILINE | re.DOTALL)

basic_info = {}
with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    text = britain_file.read()
    for m in pattern.finditer(text):
        removed = pattern_emphasis.sub('',m.group(2))
        basic_info[m.group(1)] = removed

print(basic_info)