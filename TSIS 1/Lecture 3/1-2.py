n = input().split()
l = []
for i in range(len(n)):
    n[i] = int(n[i])
    if n[i] < 0:
        continue
    else:
        l.append(n[i])
print(min(l))