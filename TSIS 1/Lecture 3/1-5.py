n = input().split()
r = int(input())
print(*(n[r-1:] + n[:r-1]))