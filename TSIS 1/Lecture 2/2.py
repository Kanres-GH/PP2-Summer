s = input('command = ')
t = ""
ans = ""
d = {"G" : "G", "()" : "o", "(al)" : "al"}
for i in range(len(s)):
    t += s[i]
    if t in d:
        ans += d[t]
        t = ""
print(ans)