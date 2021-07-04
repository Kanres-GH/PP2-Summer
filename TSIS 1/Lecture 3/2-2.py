l1 = input().split()
l2 = input().split()
cnt = 0
for i in range(len(l1)):
    if l1[i] in l2:
        cnt += 1
print(cnt)