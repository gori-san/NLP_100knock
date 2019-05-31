import leveldb

db = leveldb.LevelDB('knock60_DB')
ans = 0

for key, value in db.RangeIter():
    # print(key, value)
    if value.decode('utf-8') == 'Japan':
        ans += 1

print(ans)
