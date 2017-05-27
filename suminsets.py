a = int(input())
sum = 0
nums = set()
b = input()
nums = b.split()
nums =list(map(int, nums))
nums = set(nums)
print(nums)
for i in nums:
    sum = sum + i
result = sum/len(nums)
print(result)




