str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = str1.split()
ans = []
for word in words:
    ans.append(len(word.strip(".,")))

print(ans)
