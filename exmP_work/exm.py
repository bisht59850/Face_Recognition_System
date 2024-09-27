s = input()
ans = []
for i in s:
    ans.append(s.count(i))
print(s[ans.index(min(ans))])



