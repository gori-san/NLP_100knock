from knock30 import load_morpheme

path = 'neko.txt.mecab'
result = load_morpheme(path)

ans = []
for sentence in result:
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            # print(morpheme['base'])
            ans.append(morpheme['base'])

print(ans)