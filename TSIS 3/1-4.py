n = input().split()
cnt = 0
l = []
for i in range(len(n)):
    n[i] = int(n[i])
    if n[i] == 0:
        cnt += 1
    else:
        l.append(n[i])
print(*l, end = ' ')
print('0 '*cnt)