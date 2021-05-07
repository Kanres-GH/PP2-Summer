ab = input().split()
a = []
b = []
for i in range(2):
    ab[i] = int(ab[i])
for i in range(ab[0]):
    na = int(input())
    a.append(na)
for i in range(ab[1]):
    nb = int(input())
    b.append(nb)
common = set(a) & set(b)
left_a = set(a) - set(b)
left_b = set(b) - set(a)
print(len(common))
print(*common)
print(len(left_a))
print(*left_a)
print(len(left_b))
print(*left_b)