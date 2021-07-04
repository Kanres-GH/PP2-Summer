l1 = input().split()
l2 = input().split()
l3 = []
cnt = 0
for i in range(len(l1)):
    if l1[i] in l2:
        l3.append(l1[i])
print(*sorted(l3))