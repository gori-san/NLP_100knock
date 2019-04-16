import gzip
import sys
import json

with gzip.open(sys.argv[1],'rt',encoding='utf-8') as input_file:
    for line in input_file:
        json_dic = json.loads(line)
        if json_dic['title'] == 'イギリス':
            print(json_dic['text'])
            with open('Britain.txt','w',encoding='utf-8') as output_file:
                output_file.write(json_dic['text'])
