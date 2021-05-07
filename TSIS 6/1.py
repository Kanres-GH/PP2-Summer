def maxfrom3(l):
    return max(l)
nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(maxfrom3(nums))